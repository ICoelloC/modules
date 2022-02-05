# -*- coding: utf-8 -*-
{
    'name': "school",

    'summary': """
        Aquí en este repositorio tendremos todos los módulos que vayamos a dessarrollar en clase""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ivan Coello Cortés",
    'website': "https://github.com/ICoelloC",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Educacion',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
