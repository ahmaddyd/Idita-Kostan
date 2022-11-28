from odoo import _, api, fields, models
import datetime
import random
from odoo.exceptions import ValidationError


class OrderHotel(models.Model):
    _name = 'idita.order_kostan'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = 'Order Kostan'

    name = fields.Many2one('res.partner', string='Nama Penyewa', required=True, domain="[('is_customernya','=',True)]")
    tanggal_masuk_kostan = fields.Date(string='Tanggal Masuk Kostan', default=fields.Datetime.now, required=True)
    tanggal_keluar_kostan = fields.Date(string='Tanggal Selesai Kostan', required=True)

    detailorder_ids = fields.One2many('idita.detail_order_kostan', 'order_ids', string='Detail Order')

    jumlah_hari = fields.Integer(compute="_compute_jumlah_hari", string='Total Hari', readonly=True, store=True)

    @api.depends('tanggal_masuk_kostan', 'tanggal_keluar_kostan')
    def _compute_jumlah_hari(self):
        for record in self:
            if record.tanggal_keluar_kostan and record.tanggal_masuk_kostan:
                to_date = fields.Datetime.to_datetime(record.tanggal_keluar_kostan)
                from_date = fields.Datetime.to_datetime(record.tanggal_masuk_kostan)
                record.jumlah_hari = int(((to_date - from_date)).days)

    jumlah_harga = fields.Integer(compute='_compute_jumlah_harga', string='Total Harga')

    @api.model
    def _compute_jumlah_harga(self):
        for record in self:
            total = sum(
                self.env['idita.detail_order_kostan'].search([('order_ids', '=', record.id)]).mapped('total_harga'))
            record.jumlah_harga = total

    tagihan = fields.Integer(compute='_compute_tagihan', string='Total Tagihan')

    @api.depends('jumlah_harga', 'jumlah_hari')
    def _compute_tagihan(self):
        for record in self:
            record.tagihan = record.jumlah_hari * record.jumlah_harga

    kode_konfirmasi = fields.Char(string='Kode Konfirmasi', readonly=True, store=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Dikonfirmasi'),
        ('pay', 'Menunggu Konfirmasi Pembayaran'),
        ('done', 'Terkonfirmasi'),
        ('not_confirm', 'Ditolak Pembayaran Anda'),
        ('cancel', 'Dibatalkan'),
    ], string='States', default='draft', tracking=True)

    def action_draft(self):
        self.state = 'draft'

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'
        code = True
        while code:
            random_code = random.sample(range(1000, 1999), 1)
            code_random = "CST" + str(random_code[0])
            search_code = self.env['idita.order_kostan'].search([('no_confirm', '=', code_random)])
            if len(search_code) < 1:
                self.no_confirm = code_random
                break

    def action_cancel(self):
        self.state = 'cancel'

    def action_pay(self):
        self.state = 'pay'

    def action_not_confirm(self):
        self.state = 'not_confirm'


class DetailOrder(models.Model):
    _name = 'idita.detail_order_kostan'
    _description = 'Detail Order Kamar Kostan'

    name = fields.Char(string='Kode Order')
    models_id = fields.Many2one('idita.kamar_kostan', string='Tipe Kamar Kostan')
    order_ids = fields.One2many(comodel_name='idita.order_kostan', inverse_name='name', string='Order Ruangan')
    jumlah_kamar = fields.Integer(string='Jumlah Kamar', default=1)
    harga = fields.Integer(compute='_compute_harga_kamar', string='Harga per bulan')
    total_harga = fields.Integer(compute='_compute_total_harga', string='Total Harga')

    @api.depends('harga', 'jumlah_kamar')
    def _compute_total_harga(self):
        for record in self:
            record.total_harga = record.jumlah_kamar * record.harga

    @api.depends('models_id')
    def _compute_harga_kamar(self):
        for record in self:
            record.harga = record.models_id.harga
