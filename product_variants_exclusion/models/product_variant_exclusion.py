from odoo import fields, models, api


class ProductVariantExclusion(models.Model):
    _name = 'product.variant.exclusion'
    _description = 'Exclude Product Variants'

    product_tmpl_id = fields.Many2one('product.template', string='Product Template', ondelete='cascade', required=True,
                                      index=True)
    attribute_id = fields.Many2one('product.attribute', string='Attribute', ondelete='restrict', required=True,
                                   index=True)
    value_ids = fields.Many2many('product.attribute.value', string='Attribute Values')

