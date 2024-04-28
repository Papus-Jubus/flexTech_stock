from odoo import models, fields

class Emplacement(models.Model):
    _name = 'emplacement.model_emplacement'
    _description = 'Emplacement'

    name = fields.Char('Nom', required=True)
    description = fields.Text('Description')
    code = fields.Char('Code', required=True)
    capacity = fields.Float('Capacité')
    
