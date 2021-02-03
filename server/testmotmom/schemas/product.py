from marshmallow_jsonapi import Schema, fields


class ProductSchema(Schema):
    id = fields.String(dump_only=True)
    name = fields.String(required=True)
    count = fields.String(required=True)
    price = fields.String(required=True)
    date_add = fields.String(required=True)

    class Meta:
        type_ = 'products'