{
    'name': 'Tipos de documentos Paraguay',
    'version': '13.0.0.0.1',
    'category': 'Localizacion',
    'sequence': 14,
    'author': 'TecnoproPy',
    'website': 'TecnoproPy.com',
    'license': 'Other OSI approved licence',
    'summary': 'Definicion de tipos de documento',
    "development_status": "Alpha",  # "Alpha|Beta|Production/Stable|Mature"
    'depends': [
        'base',
        'account',
        'l10n_latam_invoice_document'
    ],
    'external_dependencies': {
    },
    'data': [
        'data/payment_terms.xml',
        'data/l10n_latam.document.type.csv',
        'views/l10n_latam_document_type_view.xml',
        'views/account_journal_view.xml',
        'views/timbrado_views.xml',
        'security/ir.model.access.csv',
        'views/account_move_view.xml',
        'data/ir_cron_data.xml',
        'views/res_partner_view.xml'
    ],
    'demo': [
        'demo/account_timbrado_demo.xml',
        'demo/base_res_partner.xml'
    ],
    'installable': True,
}
