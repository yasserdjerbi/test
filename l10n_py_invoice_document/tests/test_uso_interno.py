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

from .common import TestPy


class InternalDocumentTestCase(TestPy):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # Force user to be loggin in "Paraguayan company"
        # context = dict(cls.env.context, allowed_company_ids=[
        #               cls.company_py.id])
        # cls.env = cls.env(context=context)

        cls.journal = cls._create_journal(cls)
        cls.partner = cls.partner_py

        # buscar el timbrado activarlo y salvarlo
        cls.timbrado = cls.env.ref('l10n_py_invoice_document.timbrado_1')
        cls.timbrado.action_activate()

        cls.assertTrue(cls.timbrado, 'Timbrado not found')

    def test_uso_interno(self):
        """ Verifica factura de uso interno
        """
        data = dict()

        # verificar que el usuario esta logeado en paraguay
        self.assertEqual(self.env.user.company_id.name,
                         'Your Paraguayan Company',
                         'must be the paraguayan company')

        # chequear si existe una de las cuentas de paraguay
        domain = [('code', '=', '131000'),
                  ('company_id', '=', self.company_py.id)]
        _ = self.env['account.account'].search(domain)
        self.assertTrue(_, 'account not found, is localization installed?')

        data['timbrado'] = self.timbrado
        invoice = self._create_invoice(data)

        return invoice

    def test_2(self):
        self.assertEqual(1, 1)
