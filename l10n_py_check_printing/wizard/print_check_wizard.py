# For copyright and license notices, see __manifest__.py file in module root

from odoo import models, fields


class PrintCheckWizard(models.TransientModel):
    """Checks to print"""
    _name = "print.check.wizard"
    _description = __doc__

    def print_checks(self):
        # cheques seleccionados de account.check
        ids = self.env.context['active_ids']

        # dado el cheque buscar el pago
        ap = self.env['account.payment'].search([])
        ap = ap.filtered(lambda x: x.check_id.id in ids)

        check_report = self.env['ir.actions.report'].search(
            [('report_name', '=', 'l10n_py_check_printing.print_check')])

        return check_report.report_action(ap)
