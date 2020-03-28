# -*- coding: utf-8 -*-
{
    'name': 'Diseño de cheques Paraguay',
    'version': '13.0.0.0.0',
    'author': 'Tecnopro',
    'category': 'Accounting/Accounting',
    'summary': 'Impresión de Cheques PY',
    'website': 'tecnopro.com.py',
    'depends': [
        'account_check'
    ],
    "excludes": ['account_check_printing'],
    'data': [
        'report/print_check.xml',
        'security/ir.model.access.csv',
        'views/account_check_view.xml',
        'views/check_layout_view.xml',
        'views/account_checkbook_view.xml',
        #'views/res_config_settings_view.xml', no se porque no anda. se modifica en origen.
        'data/py_check_printing.xml',
        'data/check_layout_data.xml',
        'wizard/print_check_wizard_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'OEEL-1',
}
