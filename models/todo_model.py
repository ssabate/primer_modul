# -*- coding: utf-8 -*-
from odoo import models, fields, api

class TodoTask(models.Model):
    _name = 'todo.task'
    name = fields.Char('Descripció', required=True)
    is_done = fields.Boolean('Feta?')
    active = fields.Boolean('Activa?')

    @api.one
    def do_toggle_done(self):
        self.is_done = not self.is_done
        return True

    @api.multi
    def do_clear_done(self):
        done_recs = self.search([('is_done', '=', True)])
        done_recs.write({'active': False})
        return True

