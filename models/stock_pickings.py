from odoo import api,fields,models,_
class StockPickings(models.Model):
    _inherit = "stock.move"
    x_projects = fields.Char(string=u"项目号",readonly=False,compute="_get_projects")

    def _get_projects(self):
        att_model = self.env['purchase.order.line']
        query = []
        for obj in self.search([("origin","ilike","p")]):
            for i in att_model.search(query):
                if obj.product_id ==i.product_id:
                    obj.x_projects=i.x_projects
