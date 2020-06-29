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
#   oe -Q partner_ruc_unique -c tatakua -d tatakua_test
#

from odoo.tests.common import SavepointCase
from odoo.exceptions import ValidationError


class TestCIUnique(SavepointCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # crear partner con ruc valido
        cls.partner = cls.env['res.partner'].create({
            'name': 'Test partner',
            'ruc': '80025405-8'
        })
        # crear partner con ruc consolidado
        cls.partner1 = cls.env['res.partner'].create({
            'name': 'Second partner',
            'ruc': '88888801-5'
        })
        # crear partner ci
        cls.partner2 = cls.env['res.partner'].create({
            'name': 'Test partner',
            'ci': '123456789'
        })

    def test_duplicated_ci_creation(self):
        """ Intento crear otro partner con ci existente, debe fallar
        """
        with self.assertRaises(ValidationError):
            self.env['res.partner'].with_context(test_ruc=True).create({
                'name': 'Second partner',
                'ci': '123456789'
            })

    def test_no_duplicated_ci_creation(self):
        """ Intento crear otro partner con ci existente, debe fallar
        """
        self.env['res.partner'].with_context(test_ruc=True).create({
            'name': 'Third partner',
            'ci': '123456780'
        })

    def test_duplicate_partner(self):
        """ Si duplico el partner no debe copiar el ci
        """
        partner_copied = self.partner2.copy()
        self.assertFalse(partner_copied.ci)
