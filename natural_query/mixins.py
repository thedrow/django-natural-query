#!/usr/bin/env python
# -*- coding: utf-8 -*-


def _mixin(model_class, *mixins):
    model_class.__bases__ += mixins

    for mixin in mixins:
        mixin.__mixin__(model_class)


class NaturalQueryFieldMixin(object):
    pass


class NaturalQueryModelMixin(object):
    @classmethod
    def __mixin__(cls, model_class):
        fields = dict(model_class._meta.get_fields_with_model()).keys()
        for field in fields:
            setattr(model_class, field.name, field)