# -*- coding: utf-8 -*-
{
    'name': "IDITA KOSTAN",

    'summary': """
        Pemesanan Properti Kostan""",

    'description': """
        Pemesanan Properti Kostan di daerah Kota Bekasi
    """,

    'author': "Ahmad Yulian Dinata",
    'website': "https://www.linkedin.com/in/ahmaddyd/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/kamar_kostan_views.xml',
        'views/partner_views.xml',
        'views/pegawai_kostan_views.xml',
        'views/order_kostan_views.xml',
        'views/views.xml',
        'views/templates.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
