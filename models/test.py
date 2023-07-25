from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Test1(models.Model):
    _inherit = ['account.invoice']

    credito = fields.Float("Credito")
