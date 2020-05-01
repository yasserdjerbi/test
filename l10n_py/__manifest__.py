# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Contabilidad Paraguay',
    'version': '13.0.0.0.3',
    'author': 'Tecnopro',
    'category': 'Localizacion',
    "development_status": "Beta",  # "Alpha|Beta|Production/Stable|Mature"
    'license': 'AGPL-3',
    'website': 'tecnopro.com.py',
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
        # TODO esta vista hace fallar los chequeos de odoo.sh
        #'data/account_chart_template_data.xml',
    ],
    'demo': [],
    'uninstall_hook': 'uninstall_hook',
    'installable': True,
}
