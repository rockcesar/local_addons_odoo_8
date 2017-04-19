# -*- coding: utf-8 -*-
{
    'name': "POS debranding",
    'version': '1.0.0',
    'author': 'César Cordero',
    'license': 'GPL-3',
    'category': 'Debranding',
    'website': 'dev-rockcesar.blogspot.com',
    'depends': ['point_of_sale'],
    'data': [
        'views.xml',
    ],
    'qweb': [
        'static/src/xml/pos_debranding.xml',
    ],
    'installable': True,
}
