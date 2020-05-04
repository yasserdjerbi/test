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
    # TODO no se puede tener un modulo de odoo excluido, no pasa los tests
    "excludes": ['account_check_printing'],
    'data': [
        'report/print_check.xml',
        'security/ir.model.access.csv',
        'views/account_check_view.xml',
        'views/check_layout_view.xml',
        'views/account_checkbook_view.xml',
        # TODO Revisar porque no anda, se modifica en el repo ADHOC
        # 'views/res_config_settings_view.xml',
        'data/py_check_printing.xml',
        'data/check_layout_data.xml',
        'wizard/print_check_wizard_view.xml',
    ],
    'external_dependencies': {
        'python': [
            'num2words',
        ],
    },
    # TODO este modul no esta testeado
    'installable': False,
    'auto_install': False,
    'license': 'AGPL-3',
}
