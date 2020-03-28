# For copyright and license notices, see __manifest__.py file in module root

from odoo import fields, models, _, api
from odoo.exceptions import UserError

import logging
from num2words import num2words

_logger = logging.getLogger(__name__)


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    check_amount_in_words = fields.Char(
        compute="_compute_amount_in_words"
    )

    def _compute_amount_in_words(self):
        for rec in self:
            rec.check_amount_in_words = num2words(rec.amount,
                                         lang=self.env.user.lang[:2]).upper()

    def do_print_checks(self):
        checkbook = self.mapped('checkbook_id')
        # si todos los cheques son de la misma chequera entonces buscamos
        # reporte específico para esa chequera o mandamos el standard.
        report_name = len(checkbook) == 1 and  \
            checkbook.report_template.report_name \
            or 'l10n_py_check_printing.print_check'

        if not checkbook.layout_id:
            raise UserError('Debe definir un Diseño de cheque para la '
                            'chequera '
                            'del banco %s' % checkbook.journal_id.name)

        check_report = self.env['ir.actions.report'].search(
            [('report_name', '=', report_name)], limit=1).report_action(self)



        return check_report
