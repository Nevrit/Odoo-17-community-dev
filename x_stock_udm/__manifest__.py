# -*- coding: utf-8 -*-
{
    'name': "x_stock_udm",

    'summary': """
        From this module, we can see udm in kg instead of g
        """,

    'description': """
        From this module, we can see udm in kg instead of g
    """,

    'author': "Nevrit Ahua",
    'website': "http://www.nevritahua.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Stock Management',
    'version': '17.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/x_stock_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'LGPL-3',
}
