# Copyright 2020 jeo Software Jorge Obiols <jorge.obiols@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests.common import Form
from odoo.tests.common import SingleTransactionCase
import logging

_logger = logging.getLogger(__name__)


class TestPy(SingleTransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # setear la compañia paraguaya en el usuario
        cls.company_py = cls.env.ref('l10n_py.company_py')
        cls.env.user.company_ids += cls.company_py
        cls.env.user.company_id = cls.company_py

        cls.partner_py = cls.env.ref('l10n_py.partner_py')

        # partners
        # ---

        # products
        cls.product_iva_10 = cls.env.ref('product.product_product_6')

        # instalar la localizacion paraguay
        act_obj = cls.env['account.chart.template']
        act = act_obj.search(
            [('name', '=', 'Plan contable generico Paraguay')])
        act.try_loading_for_current_company(cls.company_py)

    def _create_journal(self, data=None):
        data = data or {}

        values = {'name': 'VENTAS 01',
                  'type': 'sale',
                  'code': 'V01',
                  'l10n_latam_use_documents': True,
                  'company_id': self.env.company.id
                  }
        values.update(data)
        return self.env['account.journal'].create(values)

    def _create_invoice(self, data=None, invoice_type='out_invoice'):
        data = data or {}
        with Form(self.env['account.move'].with_context(
                default_type=invoice_type)) as invoice_form:

            invoice_form.partner_id = data.pop('partner', self.partner)
            if 'in_' not in invoice_type:
                invoice_form.journal_id = data.pop('journal', self.journal)

            invoice_form.l10n_latam_document_type_id = data.pop(
                'document_type',
                self.env.ref('l10n_py_invoice_document.dc_fac'))

            if data.get('document_number'):
                invoice_form.l10n_latam_document_number = data.pop(
                    'document_number')

            if data.get('incoterm'):
                invoice_form.invoice_incoterm_id = data.pop('incoterm')

            if data.get('currency'):
                invoice_form.currency_id = data.pop('currency')

            if data.get('timbrado'):
                invoice_form.timbrado_id = data.get('timbrado')
                self.assertTrue(invoice_form.timbrado_id,
                                'Timbrado must be assingned')

            for line in data.get('lines', [{}]):
                with invoice_form.invoice_line_ids.new() as invoice_line_form:
                    invoice_line_form.product_id = line.get(
                        'product', self.product_iva_10)
                    invoice_line_form.quantity = line.get('quantity', 1)
                    invoice_line_form.price_unit = line.get('price_unit', 100)

        invoice = invoice_form.save()
        return invoice
