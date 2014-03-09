from django.db.models import Field

from natural_query.query import NaturalQueryDescriptor


class NaturalQueryField(Field):
    query_descriptor = NaturalQueryDescriptor

    def contribute_to_class(self, cls, name, virtual_only=False):
        super(NaturalQueryField, self).contribute_to_class(cls, name, virtual_only)

        if not hasattr(cls, name):
            setattr(cls, name, self.query_descriptor(name))