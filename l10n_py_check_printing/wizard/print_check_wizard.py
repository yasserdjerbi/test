# For copyright and license notices, see __manifest__.py file in module root

from odoo import models, fields


class PrintCheckWizard(models.TransientModel):
    _name = "print.check.wizard"

    def print_checks(self):

        # cheques seleccionados
        ids = self.env.context['active_ids']
        ap = self.env['account.payment'].search([])

        # dado el cheque buscar el pago
        ap = ap.filtered(lambda x: x.check_id.id in ids)

        #import wdb;wdb.set_trace()
        # imprimir los datos del cheque que estan en los pagos
        ap.print_checks()
