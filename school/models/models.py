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

    classroom = fields.Many2one('school.classroom', ondelete='set null', help="Clase a la que pertenece el alumno")
    teachers = fields.Many2many('school.teacher', related='classroom.teachers', readonly=True, help='Profesores de la clase')


class classroom(models.Model):
    _name = 'school.classroom'
    _description = 'Las clases'

    name = fields.Char()

    students = fields.One2many(string='Alumnos', comodel_name='school.student', inverse_name='classroom')
    teachers = fields.Many2many(comodel_name='school.teacher', relation='teachers_classroom', column1='classroom_id', column2='teacher_id')

    teachers_last_year = fields.Many2many(comodel_name='school.teacher', relation='teachers_classroom_ly', column1='classroom_id', column2='teacher_id')

class teacher(models.Model):
    _name = 'school.teacher'
    _description = 'Los profesores'

    name = fields.Char()
    classrooms = fields.Many2many(comodel_name='school.classroom', relation='teachers_classroom', column1='teacher_id', column2='classroom_id')
    students = fields.Many2many('school.student')

    classrooms_last_year = fields.Many2many(comodel_name='school.classroom', relation='teachers_classroom_ly', column1='teacher_id', column2='classroom_id')