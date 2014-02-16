#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db.models.signals import class_prepared
from natural_query.mixins import _mixin, NaturalQueryModelMixin


def naturify(sender=None, **kwargs):
    _mixin(sender, NaturalQueryModelMixin)

class_prepared.connect(naturify)