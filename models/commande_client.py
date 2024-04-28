from odoo import models, fields

class CommandeClient(models.Model):
    _name = 'commande.client'
    _description = 'Commande Client'

    date_commande = fields.Date('Date de commande', required=True)
    client_id = fields.Many2one('res.partner', string='Client', required=True)
    article_ids = fields.Many2many('article.model_article', string='Articles')
    quantite = fields.Float('Quantité')
    
