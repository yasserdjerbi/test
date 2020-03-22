# Copyright 2020 jeo Software Jorge Obiols <jorge.obiols@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

#   Para correr los tests
#
#   Definir un subpackage tests que será inspeccionado automáticamente por
#   modulos de test los modulos de test deben enpezar con test_ y estar
#   declarados en el __init__.py, como en cualquier package.
#
#   Hay que crear una base de datos para testing como sigue:
#   - Nombre sugerido: [nombre cliente]_test
#   - Debe ser creada con Load Demostration Data chequeado
#   - Usuario admin y password admin
#   - El modulo que se quiere testear debe estar instalado.
#
#   Arrancar el test con:
#
#   oe -Q l10n_py_invoice_document -c tatakua -d tatakua_test
#

from odoo.tests.common import SavepointCase


class DocumentTestCase(SavepointCase):
    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)

    def create_refund(self, prod):
        vals = {
            'type': 'out_refund',
            'partner_id': self.env.ref('base.res_partner_1').id,
            'invoice_line_ids': [(0, 0, {
                'product_id': prod.id,
                'quantity': 1,
                'price_unit': 42,
            })],
        }
        return self.env['account.move'].create(vals)

    def create_invoice(self, prod):
        vals = {
            'type': 'out_invoice',
            'partner_id': self.env.ref('base.res_partner_1').id,
            'invoice_line_ids': [(0, 0, {
                'product_id': prod.id,
                'quantity': 1,
                'price_unit': 42,
            })],
        }
        return self.env['account.move'].create(vals)

    def test_devolucion_product(self):
        """ Verifica que se usa la cuenta de devolucion en la NC cuando la
            ponemos en el producto
        """
        # ponerle al producto las cuentas de factura y nc
        prod = self.env.ref('product.product_product_4')
        return_account = self.env.ref('l10n_py.1_expense_rd')
        normal_account = self.env.ref('l10n_py.1_income')
        prod.property_account_income_return_id = return_account
        prod.property_account_income_id = normal_account

        # chequeo la nota de credito
        nc = self.create_refund(prod)
        invoice_account = nc.invoice_line_ids.account_id
        self.assertEqual(invoice_account, return_account)

        # chequeo la factura
        fa = self.create_invoice(prod)
        invoice_account = fa.invoice_line_ids.account_id
        self.assertEqual(invoice_account, normal_account)

    def test_devolucion_product_categ(self):
        """ Verifica que se usa la cuenta de devolucion en la NC cuando la
            ponemos en la categoria
        """

        # ponerle a la categoria la cuenta de retorno
        prod = self.env.ref('product.product_product_4')
        prod.categ_id = self.env.ref('product.product_category_all')
        return_account = self.env.ref('l10n_py.1_expense_rd')
        normal_account = self.env.ref('l10n_py.1_income')
        prod.categ_id.property_account_income_categ_return_id = return_account
        prod.categ_id.property_account_income_categ_id = normal_account

        nc = self.create_refund(prod)

        # chequeo la nota de credito
        invoice_account = nc.invoice_line_ids.account_id
        self.assertEqual(invoice_account, return_account)

        # chequeo la factura
        fa = self.create_invoice(prod)
        invoice_account = fa.invoice_line_ids.account_id
        self.assertEqual(invoice_account, normal_account)

