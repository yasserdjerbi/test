# For copyright and license notices, see __manifest__.py file in module root

from odoo import fields, models, _, api
import logging

_logger = logging.getLogger(__name__)


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    def do_print_checks(self):

        checkbook = self.mapped('checkbook_id')
        # si todos los cheques son de la misma chequera entonces buscamos
        # reporte específico para esa chequera
        report_name = len(checkbook) == 1 and  \
            checkbook.report_template.report_name \
            or 'l10n_py_check_printing.print_check'
        check_report = self.env['ir.actions.report'].search(
            [('report_name', '=', report_name)], limit=1).report_action(self)

        return check_report
