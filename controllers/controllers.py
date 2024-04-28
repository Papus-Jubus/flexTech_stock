# -*- coding: utf-8 -*-
# from odoo import http


# class FlextechInventaire(http.Controller):
#     @http.route('/flextech_inventaire/flextech_inventaire', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/flextech_inventaire/flextech_inventaire/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('flextech_inventaire.listing', {
#             'root': '/flextech_inventaire/flextech_inventaire',
#             'objects': http.request.env['flextech_inventaire.flextech_inventaire'].search([]),
#         })

#     @http.route('/flextech_inventaire/flextech_inventaire/objects/<model("flextech_inventaire.flextech_inventaire"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('flextech_inventaire.object', {
#             'object': obj
#         })

