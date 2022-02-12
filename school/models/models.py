# -*- coding: utf-8 -*-

from odoo import models, fields, api
import secrets
import logging

_logger = logging.getLogger(__name__)

class student(models.Model):
    _name = 'school.student'
    _description = 'school.student'

    name = fields.Char(string="Nombre", readonly=False,
                       required=True, help="Este es el nombre")

    password = fields.Char(compute='_get_password', store=True)

    birth_year = fields.Integer()
    description = fields.Text()
    inscription_date = fields.Date()
    last_login = fields.Datetime()
    is_student = fields.Boolean()
    photo = fields.Image()

    classroom = fields.Many2one(
        'school.classroom', ondelete='set null', help="Clase a la que pertenece el alumno")
    teachers = fields.Many2many(
        'school.teacher', related='classroom.teachers', readonly=True, help='Profesores de la clase')

    @api.depends('name') # se va a crear la pass cuando el campo name cambie, esto se hace con el depends
    def _get_password(self):
        for student in self:
            student.password = secrets.token_urlsafe(12)
            _logger.warning('\033[94m'+str(student)+'\033[0m')


class classroom(models.Model):
    _name = 'school.classroom'
    _description = 'Las clases'

    name = fields.Char()

    students = fields.One2many(string='Alumnos', comodel_name='school.student', inverse_name='classroom')
    teachers = fields.Many2many(comodel_name='school.teacher', relation='teachers_classroom', column1='classroom_id', column2='teacher_id')

    teachers_last_year = fields.Many2many(comodel_name='school.teacher', relation='teachers_classroom_ly', column1='classroom_id', column2='teacher_id')
    coordinator = fields.Many2one(comodel_name='school.teacher', compute='_get_coordinator')
    all_teachers = fields.Many2many(comodel_name='school.teacher', compute='_get_all_teachers')

    def _get_coordinator(self):
        for classroom in self:
            if len(classroom.teachers) > 0:
                classroom.coordinator = classroom.teachers[0].id

    def _get_all_teachers(self):
        for classroom in self:
            classroom.all_teachers = classroom.teachers + classroom.teachers_last_year

class teacher(models.Model):
    _name = 'school.teacher'
    _description = 'Los profesores'

    name = fields.Char()
    classrooms = fields.Many2many(comodel_name='school.classroom',
                                  relation='teachers_classroom', column1='teacher_id', column2='classroom_id')
    students = fields.Many2many('school.student')

    classrooms_last_year = fields.Many2many(
        comodel_name='school.classroom', relation='teachers_classroom_ly', column1='teacher_id', column2='classroom_id')
