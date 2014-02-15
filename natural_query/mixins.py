#!/usr/bin/env python
# -*- coding: utf-8 -*-
import operator
from django.db.models import Q
from django.db.models.lookups import default_lookups


def _mixin(model_or_field_class, *mixins):
    model_or_field_class.__bases__ += mixins

    for mixin in mixins:
        try:
            mixin.__mixin__(model_or_field_class)
        except AttributeError as e:
            if str(e) == "'%s' object has no attribute '__mixin'" % mixin.__name__:
                pass


class NaturalQueryFieldMixin(object):
    def __eq__(self, other):
        constructed_lookup = self.construct_lookup('exact')
        return Q(**{constructed_lookup: other})

    def construct_lookup(self, lookup_type):
        return '%s__%s' % (self.name, lookup_type)


class NaturalQueryModelMixin(object):
    @classmethod
    def __mixin__(cls, model_class):
        fields = dict(model_class._meta.get_fields_with_model()).keys()
        for field in fields:
            _mixin(field, NaturalQueryFieldMixin)
            setattr(model_class, field.name, field)