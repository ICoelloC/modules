# -*- coding: utf-8 -*-

from odoo import models, fields, api


class developer(models.Model):
    _name = 'dev_meet.developer'
    _description = 'Developers'

    name = fields.Char(string='Nombre', required=True,
                       help='Nombre del desarrollador')
    nickname = fields.Char(string='Apellidos', required=True,
                           help='Apellidos del desarrollador')
    dni = fields.Char(string='DNI', required=True, help='DNI')
    email = fields.Char(string='Email', help='Correo electrónico')
    phone = fields.Char(string='Teléfono', help='Teléfono móvil')

    technologies_learned = fields.Many2many(name='Lenguajes aprendidos', comodel_name='dev_meet.technology', help='Tecnpologías aprendidas')



class technology(models.Model):
    _name = 'dev_meet.technology'
    _description = 'Developers'

    name = fields.Char(string='Nombre', required=True,
                       help='Nombre de la tecnología')
    logo = fields.Image(string='Logo', help='Logo de la tecnología')
    official_web = fields.Char(
        string='Página oficial', help='Página web oficial')

    developers = fields.Many2many(comodel_name='dev_meet.developer')


class event(models.Model):
    _name = 'dev_meet.event'
    _description = 'Events'

    name = fields.Char(string='Nombre', required=True, help='Nombre del evento')
    
