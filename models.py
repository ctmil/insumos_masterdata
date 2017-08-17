# -#- coding: utf-8 -#-

from openerp import tools, models, fields, api, _
from openerp.osv import osv
from openerp.exceptions import except_orm, ValidationError
from StringIO import StringIO
import urllib2, httplib, urlparse, gzip, requests, json
import openerp.addons.decimal_precision as dp
import logging
import datetime
import time
from openerp.fields import Date as newdate
from datetime import datetime,date,timedelta

class res_partner(models.Model):
        _inherit = 'res.partner'

	fecha_ultima_compra = fields.Date('Fecha Ult Compra')
	city_2 = fields.Char('Ciudad 2')
	state_id_2 = fields.Many2one('res.country.state','Provincia 2')
