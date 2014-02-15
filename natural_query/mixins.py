#!/usr/bin/env python
# -*- coding: utf-8 -*-


def _mixin(model_class, *mixins):
    model_class.__bases__ += mixins


class NaturalQueryMixin(object):
    pass