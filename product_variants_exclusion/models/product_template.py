import itertools

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    exclusion_line_ids = fields.One2many('product.variant.exclusion', 'product_tmpl_id', string='Product Exclusion')

    @api.multi
    def create_variant_ids(self):
        variants_to_exclude = []
        params = self._context.get('params')
        for tmpl_id in self.with_context(active_test=False):
            all_exclusions = itertools.product(*(
                line.value_ids.ids for line in tmpl_id.exclusion_line_ids
            ))
            # Set containing existing `product.attribute.value` combination
            existing_variants = {
                frozenset(variant.attribute_value_ids.ids)
                for variant in tmpl_id.product_variant_ids
            }
            for value_ids in all_exclusions:
                values = frozenset(value_ids)
                if values in existing_variants:
                    product = self.env['product.product'].search(
                        [('attribute_value_ids', 'in', value_ids), ('product_tmpl_id', '=', tmpl_id.id)])
                    if product:
                        product.unlink()
                variants_to_exclude.append({
                    'product_tmpl_id': tmpl_id.id,
                    'attribute_value_ids': [(6, 0, list(values))],
                    'active': tmpl_id.active,
                })
            context = self._context.copy()
            if context.get('exclusion_params'):
                context['exclusion_params'].update({'variants_to_exclude': variants_to_exclude})
            else:
                context['exclusion_params'] = {'variants_to_exclude': variants_to_exclude}
            self.env.context = context
            if params:
                params.update({'variants_to_exclude': variants_to_exclude})
        return super(ProductTemplate, self).create_variant_ids()

    @api.multi
    def write(self, vals):
        res = super(ProductTemplate, self).write(vals)
        if 'exclusion_line_ids' in vals:
            self.create_variant_ids()
        return res
