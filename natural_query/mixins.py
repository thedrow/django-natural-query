#!/usr/bin/env python
# -*- coding: utf-8 -*-


def _mixin(model_or_field_class, *mixins):
    model_or_field_class.__bases__ += mixins

    for mixin in mixins:
        try:
            mixin.__mixin__(model_or_field_class)
        except AttributeError as e:
            if str(e) == "'%s' object has no attribute '__mixin'" % mixin.__name__:
                pass


class NaturalQueryFieldMixin(object):
    pass


class NaturalQueryModelMixin(object):
    @classmethod
    def __mixin__(cls, model_class):
        fields = dict(model_class._meta.get_fields_with_model()).keys()
        for field in fields:
            _mixin(field, NaturalQueryFieldMixin)
            setattr(model_class, field.name, field)