#!/usr/bin/env python
# -*- coding: utf-8 -*-


def _mixin(model_class, *mixins):
    model_class.__bases__ += mixins

    for mixin in mixins:
        mixin.__mixin__(model_class)


class NaturalQueryMixin(object):
    @classmethod
    def __mixin__(cls, model_class):
        pass