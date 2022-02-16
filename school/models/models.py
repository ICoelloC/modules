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

    def _get_password(self):
        password = secrets.token_urlsafe(12)
        _logger.warning('\033[94m'+str(student)+'\033[0m')
        return password

    password = fields.Char(default=lambda p: secrets.token_urlsafe(12))

    birth_year = fields.Integer()
    description = fields.Text()

    inscription_date = fields.Date(default = lambda d: fields.Date.today())

    last_login = fields.Datetime(default = lambda l:fields.Datetime.now())
    is_student = fields.Boolean()
    photo = fields.Image()

    classroom = fields.Many2one(
        'school.classroom', ondelete='set null', help="Clase a la que pertenece el alumno")
    teachers = fields.Many2many(
        'school.teacher', related='classroom.teachers', readonly=True, help='Profesores de la clase')


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
