from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Add_credit(models.Model):
    _inherit = ['account.invoice']

    credito = fields.Float(string="Credito", compute='_compute_cantidad_vencida')
    estado = fields.Selection([('active','Activo'),('deudor','Moroso'),('tope','Excede Credito')], string="Estado", default='active')

    @api.depends('partner_id')
    def _compute_cantidad_vencida(self):
        Invoice = self.env['account.invoice']
        for record in self:
            if record.partner_id:
                pre_total = Invoice.search([('partner_id', '=', record.partner_id.id),('type', '=', 'out_invoice'),('state', '=', 'open')])
                total = sum(factura.amount_total for factura in pre_total)
                record.credito = total
            else:
                record.credito = 0
        return
