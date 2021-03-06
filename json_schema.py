from marshmallow import Schema, fields


class GigSchema(Schema):
    website = fields.Str(required=False)
    category = fields.Str(required=False)
    id = fields.Int(dump_only=True)
    website_supplied_id = fields.Str(required=False)
    name = fields.Str(required=False)
    url = fields.Str(required=False)
    location = fields.Str(required=False)
    datetime = fields.Str(required=False)
    details = fields.Str(required=False)
