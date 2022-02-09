# -*- coding: utf-8 -*-

from odoo import models, fields, api


class student(models.Model):
    _name = 'school.student'
    _description = 'school.student'

    name = fields.Char(string="Nombre", readonly=False,
                       required=True, help="Este es el nombre")
    birth_year = fields.Integer()
    description = fields.Text()
    inscription_date = fields.Date()
    last_login = fields.Datetime()
    is_student = fields.Boolean()
    photo = fields.Image()

    classroom = fields.Many2one('school.classroom', string="Clase")
    teachers = fields.Many2many('school.teacher')


class classroom(models.Model):
    _name = 'school.classroom'
    _description = 'Las clases'

    name = fields.Char()

    students = fields.One2many('school.student','classroom')
    teachers = fields.Many2many('school.teacher')

class teacher(models.Model):
    _name = 'school.teacher'
    _description = 'Los profesores'

    name = fields.Char()
    classrooms = fields.Many2many('school.classroom')
    students = fields.Many2many('school.student')