# -*- coding: utf-8 -*-

# from odoo import models, fields, api

# _name LE INDICA A ODOO QUE SEBE CREAR UNA TABLA QUE SE LLAMA ESQUELETO


# class esqueleto(models.Model):
#     _name = 'esqueleto.esqueleto'
#     _description = 'esqueleto.esqueleto'

# ATRIBUTOS DE LA CLASE

#     name = fields.Char()
#     value = fields.Integer()
# ATRIBUTO CON VALOR CALCULADO, DEPENDE DE LA FUNCION _value_pc Y SE DEBE ALMACENAR EN LA BD
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
# METODOS @api.depends es un decorador, este esta pendiente de los cambios del atributo value si hay cambios ejecuta la funcion
#     @api.depends('value')
#       #este self le llegara una lista con todo lo que ha cambiado    
#       def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

