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
import datetime


class DocumentTestCase(SavepointCase):
    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)

    def test_ruc(self):
        """ Verifica chequeo de ruc
        """
        partner = self.env['res.partner']
        good_ruc = '80025405-8'
        bad_ruc1 = '80025405-3'
        bad_ruc2 = '800254053'
        bad_ruc3 = 'AB-C800254053'

        self.assertTrue(partner._check_ruc(good_ruc))
        self.assertFalse(partner._check_ruc(bad_ruc1))
        self.assertFalse(partner._check_ruc(bad_ruc2))
        self.assertFalse(partner._check_ruc(bad_ruc3))
        self.assertTrue(partner._check_ruc(False))

    def test_calc_dv(self):
        """ Verifica calculo del digito verificador
        """
        partner = self.env['res.partner']
        self.assertEqual(partner._calc_dv('80028764'), 9)

