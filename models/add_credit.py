from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Add_credit(models.Model):
    _inherit = ['account.invoice']

    notification_message = fields.Char(string="Mensajes", readonly=True)
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
                message = _("Este cliente tiene facturas vencidas.")
                self.notification_message = message
                self.estado = 'deudor'  # Cambiar el estado a "Deudor"
                return {
                    'warning': {
                        'title': _('Aviso'),
                        'message': message,
                    }
                }
            else:
                self.estado = 'active'  # Restaurar el estado a "Activo" si no hay facturas vencidas

        self.notification_message = False



class Add_credit_venta(models.Model):
    _inherit = ['sale.order']

    notification_message = fields.Char(string="Mensajes", readonly=True)
    credito = fields.Float(string="Credito", compute='_compute_cantidad_vencida')
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
                message = _("Este cliente tiene facturas vencidas.")
                self.notification_message = message
                self.estado = 'deudor'  # Cambiar el estado a "Deudor"
                return {
                    'warning': {
                        'title': _('Aviso'),
                        'message': message,
                    }
                }
            else:
                self.estado = 'active'  # Restaurar el estado a "Activo" si no hay facturas vencidas

        self.notification_message = False