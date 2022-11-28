from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Partner(models.Model):
    _inherit = 'res.partner'

    penyewa = fields.Boolean(string='Penyewa', default=False)
