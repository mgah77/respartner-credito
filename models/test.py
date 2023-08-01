from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Test1(models.Model):
    _inherit = ['account.invoice']

    credito = fields.Float(string="Credito", compute="_compute_cantidad_vencida")
    estadodeuda = fields.Char(string="Estado", readonly = True)

    @api.depends('partner_id')
    def _compute_cantidad_vencida(self):
        Invoice = self.env['account.invoice']
        for record in self:
            record.credito = 0
        return
