from odoo import models, fields, api, _


class Test1(models.Model):
    _inherit = ['account.invoice']

    #credito = fields.Float(string="Credito")
    #estadodeuda = fields.Char(string="Estado", readonly = True)

    #@api.depends('partner_id')
    #def _compute_cantidad_vencida(self):
    #    for record in self:
    #        record.credito = 0
    #    return
