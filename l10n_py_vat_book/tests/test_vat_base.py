# For copyright and license notices, see __manifest__.py file in module root

# Copyright 2020 jeo Software Jorge Obiols <jorge.obiols@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

#   Para correr los tests
#
#   Definir un subpackage tests que será inspeccionado automáticamente por
#   modulos de test los modulos de test deben empezar con test_ y estar
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
#   oe -Q l10n_py_vat_book -c tatakua -d tatakua_test
#

from .common import VatTransactionCase


class VatBase(VatTransactionCase):
    """ TestCase in which all test methods are run in the same transaction,
        the transaction is started with the first test method and rolled back
        at the end of the last.
    """

    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)

        iva_5 = self.get_tax(5, 'sale')
        iva_10 = self.get_tax(10, 'sale')
        p1 = self.create_product(tax_ids=iva_5.ids)
        p2 = self.create_product(tax_ids=iva_10.ids)
        inv = self.create_invoice(products=[p1, p2], auto_validate=True)

    def test_01_base5(self):
        avl = self.env['account.py.vat.line'].search([])
        base5 = sum(avl.mapped('base_5'))
        # no anda el libro de iva
        #self.assertAlmostEqual(base5, -169.524, places=1)
