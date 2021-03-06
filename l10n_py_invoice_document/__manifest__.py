{
    'name': 'Paraguayan Invoice Documents',
    'version': '13.0.0.0.10',
    'category': 'Localization',
    'author': 'Tecnopro',
    'website': 'http://tecnopro.com.py',
    'license': 'AGPL-3',
    'summary': 'Invoices, Credit notes, Stamped management',
    "development_status": "Beta",  # "Alpha|Beta|Production/Stable|Mature"
    'depends': [
        'base',
        'l10n_py',
        'account',
        'l10n_latam_invoice_document'
    ],
    'external_dependencies': {
    },
    'data': [
        'data/partner_type_data.xml',
        'data/payment_terms.xml',
        'data/l10n_latam.document.type.csv',
        'views/l10n_latam_document_type_view.xml',
        'views/account_journal_view.xml',
        'views/timbrado_views.xml',
        'security/ir.model.access.csv',
        'views/account_move_view.xml',
        'data/ir_cron_data.xml',
        'views/res_partner_view.xml',
        'views/partner_type_view.xml',
        'views/product_template_view.xml',
        'views/product_category_view.xml',
    ],
    'demo': [
        'demo/account_timbrado_demo.xml',
        'demo/res_partner_demo.xml'
    ],
    'installable': True,
    'auto_install': True,
    'sequence': 1
}
