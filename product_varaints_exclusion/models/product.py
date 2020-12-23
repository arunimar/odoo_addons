from odoo import models, api


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.model_create_multi
    def create(self, vals_list):
        exclusion_params = self._context.get('exclusion_params')
        if exclusion_params:
            variants_to_exclude = exclusion_params.get('variants_to_exclude')
            vals_list = [product for product in vals_list if product not in variants_to_exclude]
        return super(ProductProduct, self).create(vals_list)
