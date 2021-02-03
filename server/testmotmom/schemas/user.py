from marshmallow_jsonapi import Schema, fields


class UserSchema(Schema):
    id = fields.String(dump_only=True)
    email = fields.String(required=True)
    password = fields.String(required=True)

    class Meta:
        type_ = 'users'