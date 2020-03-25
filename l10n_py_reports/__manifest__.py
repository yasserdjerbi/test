{
    'name': 'Reportes Paraguay',
    'version': '13.0.0.0.3',
    'category': 'Localizacion',
    'sequence': 14,
    'author': 'Tecnopro',
    'website': 'tecnopro.com.py',
    'license': 'OEEL-1',
    'summary': 'Reportes, Facturas, Notas de credito, Recibos',
    "development_status": "Beta",  # "Alpha|Beta|Production/Stable|Mature"
    'depends': [
        'account',
        'l10n_py_invoice_document',
        'account_payment_group'
    ],
    'external_dependencies': {
        'python': [
            'num2words',
        ],
    },
    'data': [
        'templates/report_invoice.xml',
        'data/report_paperformat_data.xml',
        'data/receipt_book_data.xml',
        'templates/report_payment_receipt.xml',
    ],
    'installable': True,
}
