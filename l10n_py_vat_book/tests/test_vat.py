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
#   oe -Q l10n_py_vat_book -c test13 -d test13_test
#

from odoo.tests.common import TransactionCase


class DocumentTestCase(TransactionCase):
    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)

        journals = self.env['account.journal'].search([])
        for journal in journals:
            journal.write({'l10n_latam_use_documents': True})

    def test_01_check(self):
        """
        """

        invoices = self.env['account.move'].search([])
        self.assertEqual(len(invoices), 4, 'Debe haber solo cuatro registros')

        # Validar todas las facturas
        for invoice in invoices:
            invoice.action_post()

        #        import wdb;        wdb.set_trace()

        print()
        avl = self.env['account.ar.vat.line'].search([])
        for line in avl:
            print('{} {} IVA10={:8} BASE10={:5} IVA5={:8} BASE5={:5}'.format(
                line.date, line.move_name, line.vat_10, line.base_10, line.vat_5, line.base_5))
        print()
