# -*- coding: utf-8 -*-

{
    'name': 'Product Variants Exclusion',
    'version': '12.0.0.0',
    'category': 'Product Variant',
    'sequence': 1,
    'summary': 'Exclude Product Variants',
    'description': """
        User can choose the attribute values that will be excluded and restrict them from creating .
        It is also possible for user  to add an exclusion for an existing product template and that will delete/archive
        if a variant containing that excluded combination already exist.
        """,
    'author': 'Arunima P',
    'depends': ['product'],
    'license': 'Other proprietary',
    'data': [
        'views/product_template_views.xml',
        'security/ir.model.access.csv'
    ],
    'demo': [],
    'css': [],
    'images': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
