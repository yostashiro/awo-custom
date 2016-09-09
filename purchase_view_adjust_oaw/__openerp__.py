# -*- coding: utf-8 -*-
#    Odoo, Open Source Management Solution
#    Copyright (C) 2016 Rooms For (Hong Kong) Limited T/A OSCG
#    <https://www.odoo-asia.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

{
    'name': 'Purchase View Adjust',
    'summary': "",
    'version': "8.0.0.5.1",
    'category': 'Purchases',
    'website': 'https://www.odoo-asia.com',
    'author': 'Rooms For (Hong Kong) Limited T/A OSCG',
    'license': "AGPL-3",
    'description': """
* Adjust purchase related views.
    """,
    'application': False,
    'installable': True,
    'depends': [
        "purchase",
        "sale_line_quant_extended",
    ],
    'data': [
        'purchase_view.xml',
    ],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
