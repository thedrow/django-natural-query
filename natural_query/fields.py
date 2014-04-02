from django.db.models import Field, DateField, DateTimeField

from natural_query.query import NaturalQueryDescriptor, DateNaturalQueryDescriptor, DateTimeNaturalQueryDescriptor


class NaturalQueryField(Field):
    query_descriptor = NaturalQueryDescriptor

    def contribute_to_class(self, cls, name, virtual_only=False):
        super(NaturalQueryField, self).contribute_to_class(cls, name, virtual_only)

        if not hasattr(cls, name):
            setattr(cls, name, self.query_descriptor(name))


class DateNaturalQueryField(DateField, NaturalQueryField):
    query_descriptor = DateNaturalQueryDescriptor


class DateTimeNaturalQueryField(DateTimeField, NaturalQueryField):
    query_descriptor = DateTimeNaturalQueryDescriptor


class ForeignKeyNaturalQueryField(NaturalQueryField):
    query_descriptor = NaturalQueryDescriptor

    def contribute_to_class(self, cls, name, virtual_only=False):
        super(ForeignKeyNaturalQueryField, self).contribute_to_class(cls, name, virtual_only)

        relation_id_attribute_name = '%s_id' % name
        if not hasattr(cls, relation_id_attribute_name):
            setattr(cls, relation_id_attribute_name, self.query_descriptor(relation_id_attribute_name))