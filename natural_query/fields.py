from django.db.models import DateField, DateTimeField, ForeignKey, OneToOneField

from natural_query.query import NaturalQueryDescriptor, DateNaturalQueryDescriptor, DateTimeNaturalQueryDescriptor


class NaturalQueryField(object):
    def __init__(self, name):
        self.name = name

    query_descriptor = NaturalQueryDescriptor


class DateNaturalQueryField(DateField, NaturalQueryField):
    query_descriptor = DateNaturalQueryDescriptor


class DateTimeNaturalQueryField(DateTimeField, NaturalQueryField):
    query_descriptor = DateTimeNaturalQueryDescriptor


class ForeignKeyNaturalQueryField(ForeignKey):
    query_descriptor = NaturalQueryDescriptor


class OneToOneNaturalQueryField(OneToOneField):
    query_descriptor = NaturalQueryDescriptor