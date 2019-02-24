from odoo import models, api

class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.multi
    def _is_public(self):
        self.ensure_one()
        return self.has_group('base.group_public')
