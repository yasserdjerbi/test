# -*- coding: utf-8 -*-

from odoo import models
from odoo.tools.misc import format_date


class report_print_check(models.Model):
    _inherit = 'account.payment'

    def _check_build_page_info(self, i, p):
        page = super(report_print_check, self)._check_build_page_info(i, p)
        page.update({
            'date_label': self.company_id.account_check_printing_date_label,
            'payment_date_paraguay': format_date(self.env, self.payment_date, date_format='dd-MM-yyyy'),
        })
        return page
