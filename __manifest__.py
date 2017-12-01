# -*- coding: utf-8 -*-
{
    'name': "primer_modul",

    'summary': """
        LLista de tasques per realitzar""",

    'description': """
        LLista de tasques per realitzar en possibilitat d'afegir, completar i eliminar
    """,

    'author': "2n DAM",
    'website': "http://www.iesebre.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Employees',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/todo_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}