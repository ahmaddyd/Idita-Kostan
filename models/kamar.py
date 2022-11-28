from odoo import _, api, fields, models


class KamarKostan(models.Model):
    _name = 'idita.kamar_kostan'
    _description = 'Tipe Kamar Kostan'

    name = fields.Selection([('standar', 'Standar'), ('double', 'Double'), ('vip', 'VIP')], string='Tipe Kamar',
                            required=True)
    harga = fields.Integer(string='Harga per bulan', required=True)
    deskripsi = fields.Text(string='Deskripsi')
