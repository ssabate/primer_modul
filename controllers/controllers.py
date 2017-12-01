# -*- coding: utf-8 -*-
from odoo import http

# class PrimerModul(http.Controller):
#     @http.route('/primer_modul/primer_modul/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/primer_modul/primer_modul/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('primer_modul.listing', {
#             'root': '/primer_modul/primer_modul',
#             'objects': http.request.env['primer_modul.primer_modul'].search([]),
#         })

#     @http.route('/primer_modul/primer_modul/objects/<model("primer_modul.primer_modul"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('primer_modul.object', {
#             'object': obj
#         })