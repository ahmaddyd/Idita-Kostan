from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Partner(models.Model):
    _inherit = 'res.partner'

    is_pegawainya = fields.Boolean(string='Pegawai', default=False)
    is_customernya = fields.Boolean(string='Penyewa', default=False)
