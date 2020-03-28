# For copyright and license notices, see __manifest__.py file in module root

from odoo import fields, models, _, api


class AccountCheck(models.Model):
    _inherit = 'account.check'

    def post_payment_check(self, payment):
        """
        TODO WARNING, hay que ver si esto funcina !!! Revisar los asientos
        """
        payment.post()
