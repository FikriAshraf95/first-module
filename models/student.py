# -*- coding: utf-8 -*-

from odoo import models, fields, api,  _
from odoo.exceptions import Warning

class Student(models.Model):
    _name = 'student.student'
    _description = 'Model for Student'

    name = fields.Char(String="Name")
    age = fields.Integer(String="Age")
    email = fields.Char(String="Email")
    join_date = fields.Date(String="Join Date")
    school_id = fields.Many2one('school.school', string="School")
    option_ids = fields.Many2many('student.option', string="Options")

    address = fields.Char(String="Adress")
    city = fields.Char(String="City")

    note_1 = fields.Float(String="Note 1")
    note_2 = fields.Float(String="Note 2")
    note_3 = fields.Float(String="Note3")
    note_4 = fields.Float(String="Note4")

    average = fields.Float(String="Average", compute='_get_average_student')

    status = fields.Selection([('new', 'New'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='new')

    student_inscription_ids = fields.Char(String="Inscription Id")

    # @api.multi
    # def notify(self):


    @api.model
    def create(self, vals):
        vals['student_inscription_ids'] = self.env['ir.sequence'].next_by_code('student.sequence')
        result = super(Student, self).create(vals)
        return result

    @api.depends('note_1','note_2','note_3','note_4')
    def _get_average_student(self):
        self.env.user.notify_success(message='Changed')
        self.average = (self.note_1 + self.note_2 + self.note_3 + self.note_4) / 4

    def set_student_to_new(self):
        self.status = 'new'
        print("New")
    def set_student_to_accepted(self):
        self.status = 'accepted'
        # self.env.user.notify_success(message='Accepted')
        self.env.user.notify_success(message='My success message')
        print("accept")
        # self.env.user.notify_success(message='Accepted')
    def set_student_to_rejected(self):
        self.status = 'rejected'
        print("reject")
        self.env.user.notify_success(message='Rejected')

    # @api.onchange('status')
    # def notify(self):
    #     stat = self.status
    #     if stat == 'accepted':
    #         print("Accepted")
    #         # self.env.user.notify_success(message='Accepted')
    #     elif stat == "rejected":
    #         print("Rejected")
    #         # self.env.user.notify_success(message='Rejected')
    #     else:
    #         print("Reset")
    #         # self.env.user.notify_success(message='Reset')

class School(models.Model):
    _name = 'school.school'
    _description = 'Model for Schools'

    name = fields.Char(String="Name")
    student_ids = fields.One2many('student.student', 'school_id', string="Students")

class StudentOption(models.Model):
    _name = 'student.option'
    _description = 'Model for Student Options'

    name = fields.Char(String="Name")
