{
    'name': 'Reportes Paraguay',
    'version': '13.0.0.0.4',
    'category': 'Localizacion',
    'sequence': 14,
    'author': 'Tecnopro',
    'website': 'tecnopro.com.py',
    'license': 'AGPL-3',
    'summary': 'Reportes, Facturas, Notas de credito, Recibos',
    "development_status": "Alpha",  # "Alpha|Beta|Production/Stable|Mature"
    'depends': [
        'account',
        'l10n_py_invoice_document',
    ],
    'external_dependencies': {
        'python': [
            'num2words',
        ],
    },
    'data': [
        'security/ir.model.access.csv',
        'templates/report_invoice.xml',
        'data/report_paperformat_data.xml',
        'data/receipt_book_data.xml',
        'views/account_payment_view.xml'
#        'templates/report_payment_receipt.xml',
    ],
    'installable': True,
}
