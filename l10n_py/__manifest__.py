# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Contabilidad Paraguay',
    'version': '13.0.0.0.3',
    'author': 'Tecnopro',
    'category': 'Localizacion',
    "development_status": "Beta",  # "Alpha|Beta|Production/Stable|Mature"
    'license': 'AGPL-3',
    'website': 'http://tecnopro.com.py',
    'summary': 'Modulo base para la localizacion Paraguaya',
    'depends': [
        'account',
        'l10n_latam_invoice_document',
    ],
    'data': [
        'data/l10n_py.xml',
        'data/account.account.template.csv',
        'data/account_tax_group.xml',
        'data/l10n_py_post.xml',
    ],
    'demo': [
        'demo/demo_data.xml'
# TODO si instalo la localizacion en modo demo tambien fallan los test sh en account
#        'demo/install_localization.xml'
    ],
    'uninstall_hook': 'uninstall_hook',
    'installable': True,
    'sequence': 1
}
