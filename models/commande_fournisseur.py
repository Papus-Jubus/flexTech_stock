from odoo import models, fields

class CommandeFournisseur(models.Model):
    _name = 'commande.fournisseur'
    _description = 'Commande Fournisseur'

    date_commande = fields.Date('Date de commande', required=True)
    fournisseur_id = fields.Many2one('fournisseur.model_fournisseur', string='Fournisseur', required=True)
    article_ids = fields.Many2many('article.model_article', string='Articles')
    quantite = fields.Float('Quantité')
    
