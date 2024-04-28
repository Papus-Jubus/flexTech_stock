from odoo import models, fields

class Fournisseur(models.Model):
    _name = 'fournisseur.model_fournisseur'
    _description = 'Fournisseur'

    name = fields.Char('Nom', required=True)
    adresse = fields.Char('Adresse')
    contact = fields.Char('Contact')
    conditions_paiement = fields.Text('Conditions de paiement')
   
