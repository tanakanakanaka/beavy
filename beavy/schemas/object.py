from marshmallow_jsonapi import Schema, fields
from beavy.common.morphing_schema import MorphingSchema

from .user import BaseUser


class BaseObject(Schema):
    class Meta:
        type_ = "object"

    id = fields.Integer()
    created_at = fields.DateTime()
    owner = fields.Nested(BaseUser)
    belongs_to_id = fields.Integer()  # don't leak
    type = fields.String(attribute="discriminator")


class ObjectField(MorphingSchema):
    FALLBACK = BaseObject
    registry = {}
