from odoo import models, fields

class RetourService(models.Model):
    _name = 'retour.service'
    _description = 'Retour en Réparation / Service Après-Vente'

    date_demande = fields.Date('Date de demande', required=True)
    article_id = fields.Many2one('article.model_article', string='Article', required=True)
    description_probleme = fields.Text('Description du problème')
    client_id = fields.Many2one('res.partner', string='Client')
    statut = fields.Selection([
        ('en_attente', 'En attente'),
        ('en_cours', 'En cours de traitement'),
        ('resolu', 'Résolu'),
    ], string='Statut', default='en_attente')
    technicien_id = fields.Many2one('technicien.model_technicien', string='Technicien en charge')
    couts_associes = fields.Float('Coûts associés')
    
