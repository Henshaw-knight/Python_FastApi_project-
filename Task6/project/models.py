from tortoise import fields
from tortoise.models import Model


class Task(Model):
    id = fields.UUIDField(pk=True)
    title = fields.CharField(max_length = 300)
    description = fields.CharField(max_length= 400)
    created_at = fields.DatetimeField(auto_now_add=True)
    is_completed = fields.CharField(max_length = 400)
    