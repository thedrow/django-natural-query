#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.db.models import Field
from django.db.models.loading import get_apps, get_models

from natural_query.mixins import _mixin, NaturalQueryModelMixin, NaturalQueryFieldMixin


class NaturalQueryConfig(AppConfig):
    name = 'natural_query'

    def ready(self):
        _mixin(Field, NaturalQueryFieldMixin)

        for app in get_apps():
            for model in get_models(app):
                _mixin(model, NaturalQueryModelMixin)