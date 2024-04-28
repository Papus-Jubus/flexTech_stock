from odoo import models, fields

class Technicien(models.Model):
    _name = 'technicien.model_technicien'
    _description = 'Technicien'

    name = fields.Char('Nom', required=True)
    specialite = fields.Char('Spécialité')
    
