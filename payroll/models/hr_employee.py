# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"
    _description = "Employee"

    slip_ids = fields.One2many(
        "hr.payslip", "employee_id", string="Payslips", readonly=True
    )
    payslip_count = fields.Integer(
        compute="_compute_payslip_count",
        groups="payroll.group_payroll_user",
    )

    bank_account_ids = fields.One2many(
        'res.partner.bank',
        "employee_id",
        string="Bank Accounts"
    )
    mol_id = fields.Char(string="MOL ID")

    def _compute_payslip_count(self):
        for employee in self:
            employee.payslip_count = len(employee.slip_ids)

class ResPartnerBank(models.Model):
    _inherit = 'res.partner.bank'

    employee_id = fields.Many2one('hr.employee', string="Employee")
    branch_name = fields.Char(string="Branch Name")
    iban = fields.Char(string="IBAN")
    routing_code = fields.Integer(string="Routing Code")
    is_default = fields.Boolean(string="Default Bank Account")