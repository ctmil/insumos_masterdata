# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
#
##############################################################################

import math
import re
import time

from openerp import api, tools, SUPERUSER_ID
from openerp.osv import osv, fields, expression
from openerp.tools.translate import _
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT

import openerp.addons.decimal_precision as dp
from openerp.tools.float_utils import float_round, float_compare

class product_product(osv.osv):
	_inherit = 'product.product'

	def search(self, cr, uid, args, offset=0, limit=None, order=None, context=None, count=False):
        	if context is None:
	        	context = {}
		new_args = []
		new_args_1 = []
		if args:
			for arg in args:
				if arg[0] == 'default_code' and arg[1] == '=':
					new_args = ('detalles','ilike',arg[2])
					new_args_1 = ('modelo','ilike',arg[2])
		if new_args != []:
			if '|' not in args:
				args.insert(0,'|')
			args.append(new_args)		
			args.append(new_args_1)		
        	if context.get('search_default_categ_id'):
	        	args.append((('categ_id', 'child_of', context['search_default_categ_id'])))
        	return super(product_product, self).search(cr, uid, args, offset=offset, limit=limit, order=order, context=context, count=count)

