# -*- coding: utf-8 -*-
{
    'name': "training_module",

    'summary': """
    Module is intended as a practice run for the LMS system.
        """,

    'description': """
    Custom designed training module
    """,

    'author': "Elite Metal Finishing",
    'website': "elitemetalfinishing.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'installable': True,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
