from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Test1(models.Model):
    _inherit = 'account.invoice'

    credito = fields.Float("Credito")

    @api.model
    def create(self ,vals):
        res = super(Test1, self).create(vals)
        if res.partner_id:
            credito = res.partner_id.credit_limit
            res.update({
                "credito": credito
            })
        return res
    
    @api.onchange("partner_id")
    def onchange_partner_credit(self):
        if self.partner_id:
            credito = self.partner_id.credit_limit
            invoice_obj = self.env["account.invoice"].sudo().search([("name", "=", self.name)])
            if invoice_obj:
                invoice_obj.write({
                    "credito": credito
                })
        else
            self.credito = False
