# -*- coding: utf-8 -*-
{
    'name': "flextech_inventaire",

    'summary': "FlexTech est une entreprise informatique",

    'description': """
Long description of module's purpose
    """,

    'author': "flexTech",
    'website': "flextech2023.web.app",
    'application': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/article_views.xml',
        'views/emplacement_views.xml',
        'views/fournisseur_views.xml',
        'views/commande_client_views.xml',
        'views/commande_fournisseur_views.xml',
        'views/retour_service_views.xml',
        'views/technicien_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

