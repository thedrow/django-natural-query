#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db.models import Q, Field, F


def _mixin(model_or_field_class, *mixins):
    model_or_field_class.__bases__ += mixins

    for mixin in mixins:
        try:
            mixin.__mixin__(model_or_field_class)
        except AttributeError as e:
            if str(e) == "'%s' object has no attribute '__mixin'" % mixin.__name__:
                pass


def get_value_or_field(other):
    if isinstance(other, Field):
        other = F(other.name)
    return other


def create_query_object(constructed_lookup, other):
    return Q(**{constructed_lookup: other})


class NaturalQueryFieldMixin(object):
    def __eq__(self, other):
        return self.transform_operator_to_query_object('exact', other)

    def __gt__(self, other):
        return self.transform_operator_to_query_object('gt', other)

    def __ge__(self, other):
        return self.transform_operator_to_query_object('gte', other)
    
    def __lt__(self, other):
        return self.transform_operator_to_query_object('lt', other)

    def __le__(self, other):
        return self.transform_operator_to_query_object('lte', other)

    def __ne__(self, other):
        return ~self.transform_operator_to_query_object('exact', other)

    def transform_operator_to_query_object(self, lookup_type, other):
        other = get_value_or_field(other)
        constructed_lookup = self.construct_lookup(lookup_type)
        return create_query_object(constructed_lookup, other)

    def construct_lookup(self, lookup_type):
        return '%s__%s' % (self.name, lookup_type)


class NaturalQueryModelMixin(object):
    @classmethod
    def __mixin__(cls, model_class):
        fields = dict(model_class._meta.get_fields_with_model()).keys()
        for field in fields:
            _mixin(field, NaturalQueryFieldMixin)
            setattr(model_class, field.name, field)