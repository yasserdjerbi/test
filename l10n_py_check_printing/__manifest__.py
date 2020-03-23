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
#        'account_check_printing',
#        'l10n_py'
    ],
    'data': [
        'views/account_check_view.xml',
        'views/account_checkbook_view.xml',
        'views/check_layout_view.xml',
        'data/py_check_printing.xml',
        'report/print_check.xml',
#        'report/print_check_top.xml',
#        'report/print_check_middle.xml',
#        'report/print_check_bottom.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'OEEL-1',
}
