from django.db.models import Model
from natural_query.query import PrimaryKeyNaturalQueryDescriptor


class NaturalQueryModel(Model):
    class Meta:
        abstract = True

    pk = PrimaryKeyNaturalQueryDescriptor()