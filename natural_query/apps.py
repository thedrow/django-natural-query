#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.apps import AppConfig, apps
import itertools
from natural_query.fields import NaturalQueryField
from natural_query.query import NaturalQueryDescriptor


class NaturalQueryConfig(AppConfig):
    name = 'natural_query'

    def ready(self):
        """
        Temporary code that monkeypatches the model classes.
        """
        app_configs = apps.get_app_configs()
        models = itertools.chain.from_iterable(app_config.get_models() for app_config in app_configs)

        for model in models:
            non_natural_fields = [field for field in model._meta.fields if
                                  not isinstance(field, NaturalQueryField)]

            for field in non_natural_fields:
                if not hasattr(model, field.name):
                    setattr(model, field.name, NaturalQueryDescriptor(field.name))