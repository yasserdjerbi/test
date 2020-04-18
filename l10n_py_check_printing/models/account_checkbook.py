# For copyright and license notices, see __manifest__.py file in module root

from odoo import fields, models


class AccountCheckbook(models.Model):
    _inherit = 'account.checkbook'

    layout_id = fields.Many2one(
        'check.layout',
        string="Diseño de cheque"
    )
