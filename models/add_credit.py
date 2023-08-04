from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Add_credit(models.Model):
    _inherit = ['account.invoice']

    notification_message = fields.Char(string="Notification Message", readonly=True)
    credito = fields.Float(string="Credito")
    estado = fields.Selection([('active','Activo'),('deudor','Cliente Moroso'),('tope','Excede Credito')], string="Estado", default='active', readonly=True)

    @api.onchange('partner_id')
    def _check_partner_status(self):
        if self.partner_id:
            Invoice = self.env['account.invoice']
            pre_total = Invoice.search_count([
                ('partner_id', '=', self.partner_id.id),
                ('type', '=', 'out_invoice'),
                ('state', '=', 'open'),
                ('date_due', '<', fields.Date.today())
            ])
            if pre_total > 0:
                self.notification_message = _("Este cliente tiene facturas vencidas.")
            else:
                self.notification_message = False
        else:
            self.notification_message = False

class Add_credit_venta(models.Model):
    _inherit = ['sale.order']

    credito = fields.Float(string="Credito", compute='_compute_cantidad_vencida')
    estado = fields.Selection([('active','Activo'),('deudor','Cliente Moroso'),('tope','Excede Credito')], string="Estado", default='active', readonly=True)

    @api.depends('partner_id')
    def _compute_cantidad_vencida(self):
        Invoice = self.env['account.invoice']
        for record in self:
            if record.partner_id:
                pre_total = Invoice.search_count([('partner_id', '=', record.partner_id.id),('type', '=', 'out_invoice'),('state', '=', 'open'),('date_due', '<', fields.Date.today())])
                #total = sum(factura.amount_total for factura in pre_total)
                if (pre_total > 0):
                    record.estado = 'deudor'
                    record.state = 'cancel'
                else:
                    record.estado = 'active'  
                    record.state = 'draft'  
                record.credito = pre_total
            else:
                record.credito = 0
        return
