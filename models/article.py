from odoo import models, fields, api

class Article(models.Model):
    _name = 'article.model_article'
    _description = 'Article'

    name = fields.Char('Nom', required=True)
    description = fields.Text('Description')
    code = fields.Char('Code', required=True)
    category_id = fields.Many2one('article.category', string='Catégorie')
    price = fields.Char('prix')
    quantity_available = fields.Float('Quantité en stock', default=0.0)
    reorder_point = fields.Float('Seuil de réapprovisionnement')

class ArticleCategory(models.Model):
    _name = 'article.category'
    _description = 'Catégorie d\'article'

    name = fields.Char('Nom', required=True)
    description = fields.Text('Description')
