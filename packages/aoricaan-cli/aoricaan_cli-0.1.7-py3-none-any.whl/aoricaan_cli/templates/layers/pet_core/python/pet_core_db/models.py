from peewee import CharField, DateTimeField, SQL
from pet_core_db.base_model import BaseModel

SCHEMA = 'petcare'

__all__ = [
    "Users"
]


class Users(BaseModel):
    names = CharField()
    first_name = CharField()
    last_name = CharField(null=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT now()")], null=True)

    class Meta:
        table_name = 'users'
        schema = SCHEMA
