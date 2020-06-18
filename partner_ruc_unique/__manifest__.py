# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Partner RUC unique',
    'version': '13.0.0.0.1',
    'author': 'Tecnopro',
    'category': 'Localizacion',
    "development_status": "Production/Stable",
    'license': 'AGPL-3',
    'website': 'http://tecnopro.com.py',
    'summary': 'Evita la duplicacion de RUC en la localizacion Paraguay',
    'depends': [
        'base',
        'l10n_py_invoice_document'
    ],
    'data': [
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': True,
    'sequence': 1
}
