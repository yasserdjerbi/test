# For copyright and license notices, see __manifest__.py file in module root


from odoo import fields, models


class AccountPayment(models.Model):
    _inherit = "account.payment"

    receiptbook_id = fields.Many2one(
        'report.receiptbook'
    )
