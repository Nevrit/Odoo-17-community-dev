# -*- coding: utf-8 -*-
{
    'name': "x_sale_customer_qty",

    'summary': """
        This module allow us to add another sale line called customer_qty.
        """,

    'description': """
        This module allow us to add another sale line called 'customer_qty'.
        This line shows ordered qty by the customer. It's also what the customer see.
    """,

    'author': "Nevrit Ahua",
    'website': "http://www.nevritahua.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sale Management',
    'version': '17.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'LGPL-3',
}
