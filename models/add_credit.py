from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Add_credit(models.Model):
    _inherit = ['account.invoice']

    credito = fields.Float(string="Credito")
