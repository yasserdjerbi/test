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

from odoo.tests.common import TransactionCase
import datetime


class DocumentTestCase(TransactionCase):
    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)
        self.vals = {
            "name": "12345677",
            "validity_start": "2019-05-01",
            "validity_end": "2019-06-15",
            "trade_code": "001",
            "shipping_point": "001",
            "document_type_id": self.env.ref(
                'l10n_py_invoice_document.dc_fac').id,
            "start_number": 1,
            "end_number": 100,
            "print_system": "auto_printer"
        }
        timbrado_obj = self.env['timbrado.data']
        timbrados = timbrado_obj.search([])
        timbrados.unlink()

        timbrado_obj.create(self.vals)

        self.vals['name'] = '12345678'
        self.vals['validity_start'] = '2019-12-01'
        self.vals['validity_end'] = '2019-12-15'
        self.vals['document_type_id'] = self.env.ref(
            'l10n_py_invoice_document.dc_nc').id,
        timbrado_obj.create(self.vals)

        self.vals['name'] = '12345679'
        self.vals['validity_start'] = '2020-01-01'
        self.vals['validity_end'] = '2020-02-15'
        self.vals['document_type_id'] = self.env.ref(
            'l10n_py_invoice_document.dc_nd').id,
        timbrado_obj.create(self.vals)

        self.timbrados = timbrado_obj.search([])

    def test_01(self):
        """ verifica que no se puede repetir el numero de timbrado
        """
        vals = self.vals
        with self.assertRaises(Exception):
            self.timbrados.create(vals)

    def test_02_timbrado(self):
        """ Activar un timbrado para que cree la secuencia
            Verificar que la secuencia fue creada
        """
        date = datetime.date(2019, 6, 1)
        timbrado = self.timbrados[0]
        timbrado._button_activate(date)
        seq = timbrado.document_type_id.sequence_id
        self.assertTrue(len(seq), 1)

    def test_03_timbrado(self):
        """ Verifica que no se puede activar un timbrado si ya existe otro igual
        """
        date = datetime.date(2019, 6, 1)

        # activo el timbrado de la factura
        tim1 = self.timbrados[0]
        tim1._button_activate(date)

        vals = tim1.copy_data()[0]
        vals['name'] = "12345699"
        # creo el segundo timbrado en borrador, es igual salvo en numero de timbrado
        tim2 = self.timbrados.create(vals)

        # como el primero esta activado no deja activar el segundo
        with self.assertRaises(Exception):
            tim2._button_activate(date)

    def test_04_timbrado_check(self):
        """ Verifica que se testee la validez de los timbrados
        """
        date = datetime.date(2019, 12, 5)
        self.timbrados.validate_timbrado_all(date)

        self.assertEqual(self.timbrados[0].state, 'no_active')
        self.assertEqual(self.timbrados[1].state, 'active')
        self.assertEqual(self.timbrados[2].state, 'no_active')
