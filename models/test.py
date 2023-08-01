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
            if record.cliente:
                vencido = Invoice.search([('partner_id', '=', record.partner_id),('type', '=', 'out_invoice'),('state', '=', 'open')])
                total_vencido = sum(factura.amount_total for factura in vencido)
                record.credito = total_vencido
            else:
                record.credito = 0
        return
