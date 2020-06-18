# For copyright and license notices, see __manifest__.py file in module root
from odoo.tests.common import SingleTransactionCase #noqa


class VatTransactionCase(SingleTransactionCase):
    """ TestCase in which all test methods are run in the same transaction,
        the transaction is started with the first test method and rolled back
        at the end of the last.
    """

    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)

        # agregar datos necesarios al partner
        self.partner_agrolait_id = self.env.ref('base.res_partner_2')
        _ = 'l10n_py_invoice_document.partner_type_data_1'
        self.partner_agrolait_id.partner_type_sale_id = self.env.ref(_)
        self.partner_agrolait_id.ruc = '3970756-3'

        # cargar localizacion paraguay
        chart = self.env.ref('l10n_py.py_chart_template')
        chart.try_loading_for_current_company()

        # activar el timbrado
        self.timbrado = self.env.ref('l10n_py_invoice_document.timbrado_1')
        self.timbrado.action_activate()

        # definir el tipo de factura
        self.invoice_type_fac = self.env.ref('l10n_py_invoice_document.dc_fac')

        # crear journal
        self.sale_journal = self.env['account.journal'].create({
            'name': 'Demo VAT Journal',
            'code': 'DVJ',
            'type': 'sale',
        })
        self.sale_journal.l10n_latam_use_documents = True

    def create_product(self, name='test_product', lst_price=100,
                       standard_price=None, tax_ids=None, sale_account=None):
        product = self.env['product.template'].create({
            'type': 'consu',
            'taxes_id': [(5, 0, 0)] if not tax_ids else [(6, 0, tax_ids)],
            'name': name,
            'lst_price': lst_price,
            'standard_price': standard_price if standard_price else 0.0,
        })

        if sale_account:
            product.property_account_income_id = sale_account
        return product

    def get_tax(self, amount, type):
        return self.env['account.tax'].search([('amount', '=', amount),
                                               ('type_tax_use', '=', type)])

    def create_invoice(self, type='out_invoice', invoice_amount=50,
                       currency_id=None, partner_id=None, date_invoice=None,
                       payment_term_id=False, auto_validate=False,
                       products=False):

        line_ids = []
        for pt in products:
            domain = [('product_tmpl_id', '=', pt.id)]
            pp = self.env['product.product'].search(domain)
            line_ids.append((0, 0, {
                'product_id': pp.id,
                'tax_ids': [(4, pp.taxes_id.id)]
            }))

        # pongo la fecha factura dentro de la validez del timbrado
        date_invoice = self.timbrado.validity_start

        invoice_vals = {
            'type': type,
            'partner_id': partner_id or self.partner_agrolait_id,
            'invoice_date': date_invoice,
            'l10n_latam_document_type_id': self.invoice_type_fac,
            'date': date_invoice,
            'invoice_line_ids': line_ids,
            'journal_id': self.sale_journal.id,
            'timbrado_id': self.timbrado
        }

        if payment_term_id:
            invoice_vals['invoice_payment_term_id'] = payment_term_id

        if currency_id:
            invoice_vals['currency_id'] = currency_id

        invoice = self.env['account.move'].with_context(
            default_type=type).create(invoice_vals)

        if auto_validate:
            invoice.action_post()

        return invoice
