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

    def _create_partner(self, vals):
        if not vals.get('name'):
            vals['name'] = 'Test Partner'
        return self.env['res.partner'].create(vals)

    def test_duplicated_ci_creation(self):
        """ Intento crear partner con ci duplicado
        """
        self._create_partner({'ci': '123456789'})
        with self.assertRaises(ValidationError):
            self._create_partner({'ci': '123456789'})

    def test_duplicate_partner(self):
        """ Si duplico el partner no debe copiar el ci
        """
        partner_1 = self._create_partner({'ci': '123456789'})
        partner_copied = partner_1.copy()
        self.assertFalse(partner_copied.ci)

    def test_no_duplicated_ci_creation(self):
        """ Creacion de partner sin ci
        """
        self._create_partner({})

    def test_no_ci_multiple_partners(self):
        """ Creacion de varios partners con ci=False
        """
        self._create_partner({'ci': False})
        self._create_partner({'ci': False})
