# -*- coding: utf-8 -*-
# from odoo import http


# class Iditakostan(http.Controller):
#     @http.route('/iditakostan/iditakostan/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/iditakostan/iditakostan/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('iditakostan.listing', {
#             'root': '/iditakostan/iditakostan',
#             'objects': http.request.env['iditakostan.iditakostan'].search([]),
#         })

#     @http.route('/iditakostan/iditakostan/objects/<model("iditakostan.iditakostan"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('iditakostan.object', {
#             'object': obj
#         })
