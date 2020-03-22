# -*- coding: utf-8 -*-
{
    'name': 'Diseño de cheques Paraguay',
    'version': '13.0.0.0.0',
    'author': 'Tecnopro',
    'category': 'Accounting/Accounting',
    'summary': 'Impresion de Cheques PY',
    'website': 'tecnopro.com.py',
    'depends': ['account_check_printing', 'l10n_py'],
    'data': [
        'data/py_check_printing.xml',
        'report/print_check.xml',
        'report/print_check_top.xml',
        'report/print_check_middle.xml',
        'report/print_check_bottom.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'OEEL-1',
}
