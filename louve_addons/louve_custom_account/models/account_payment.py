# -*- coding: utf-8 -*-
# Copyright (C) 2017-Today: La Louve (<http://www.lalouve.net/>)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
#          Julien Weste
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, models, fields


class account_payment(models.Model):
    _inherit = 'account.payment'

    partner_code = fields.Integer(
        related='partner_id.barcode_base', store=True)

    @api.multi
    def cancel_payment(self):
        super(account_payment, self).cancel()
        return True

    @api.multi
    def post_payment(self):
        super(account_payment, self).post()
        return True
