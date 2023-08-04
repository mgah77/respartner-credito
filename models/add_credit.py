from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Add_credit(models.Model):
    _inherit = ['account.invoice']

    credito = fields.Float(string="Credito", compute='_compute_cantidad_vencida')
    estado = fields.Selection([('active','Activo'),('deudor','Moroso'),('tope','Excede Credito')], string="Estado", default='active', readonly=True)

    @api.depends('partner_id')
    def _compute_cantidad_vencida(self):
        Invoice = self.env['account.invoice']
        for record in self:
            if record.partner_id:
                pre_total = Invoice.search_count([('partner_id', '=', record.partner_id.id),('type', '=', 'out_invoice'),('state', '=', 'open'),('date_due', '<', fields.Date.today())])
                #total = sum(factura.amount_total for factura in pre_total)
                if (pre_total > 0):
                    record.estado = 'deudor'
                else:
                    record.estado = 'active'    
                record.credito = pre_total
            else:
                record.credito = 0
        return
