{
    'name': 'Reportes Paraguay',
    'version': '13.0.0.0.8',
    'category': 'Localizacion',
    'author': 'Tecnopro',
    'website': 'http://tecnopro.com.py',
    'license': 'AGPL-3',
    'summary': 'Reportes, Facturas, Notas de credito, Recibos',
    "development_status": "Beta",  # "Alpha|Beta|Production/Stable|Mature"
    'depends': [
        'account',
        'l10n_py_invoice_document',
    ],
    'external_dependencies': {
        'python': [
            'num2words',
            'openupgradelib'
        ],
    },
    'data': [
        'data/receipt_book_data.xml',
        'data/report_paperformat_data.xml',
        'security/ir.model.access.csv',
        'templates/report_preprinted_invoice.xml',
        'templates/report_invoice.xml',
        'templates/report_payment_receipt_template.xml',
        'wizard/adjust_sequence_number_view.xml',
        'views/account_payment_view.xml',
        'views/account_payment_receiptbook_view.xml',
    ],
    'installable': True,
    'auto_install': True,
    'sequence': 1
}
