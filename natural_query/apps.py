#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools

from django.apps import AppConfig, apps
from django.db.models import DateField, DateTimeField
from django.db.models.fields.related import RelatedField, ReverseSingleRelatedObjectDescriptor

from natural_query.fields import NaturalQueryField
from natural_query.query import NaturalQueryDescriptor, DateNaturalQueryDescriptor, DateTimeNaturalQueryDescriptor, \
    PrimaryKeyNaturalQueryDescriptor, ReverseSingleRelatedObjectNaturalQueryDescriptor


class NaturalQueryConfig(AppConfig):
    name = 'natural_query'

    def naturalize_model(self, model):
        if not isinstance(model.pk, PrimaryKeyNaturalQueryDescriptor):
            model.pk = PrimaryKeyNaturalQueryDescriptor()
        non_natural_fields = [field for field in model._meta.fields if
                              not isinstance(field, NaturalQueryField)]
        for field in non_natural_fields:
            if not hasattr(model, field.name):
                if isinstance(field, DateTimeField):
                    setattr(model, field.name, DateTimeNaturalQueryDescriptor(field.name))
                elif isinstance(field, DateField):
                    setattr(model, field.name, DateNaturalQueryDescriptor(field.name))
                else:
                    setattr(model, field.name, NaturalQueryDescriptor(field.name))
        non_natural_foreign_key_fields = [field for field in model._meta.fields if
                                          isinstance(field, RelatedField)]
        for field in non_natural_foreign_key_fields:
            relation_id_attribute_name = '%s_id' % field.name
            if not hasattr(model, relation_id_attribute_name):
                setattr(model, relation_id_attribute_name, NaturalQueryDescriptor(relation_id_attribute_name))

    def naturalize_model_relationships(self, model):
        non_natural_foreign_key_fields = [field for field in model._meta.fields if
                                          isinstance(field, RelatedField)]
        for field in non_natural_foreign_key_fields:
            if isinstance(getattr(model, field.name), ReverseSingleRelatedObjectDescriptor):
                descriptor = ReverseSingleRelatedObjectNaturalQueryDescriptor(field)

                setattr(model, field.name, descriptor)

    def ready(self):
        """
        Temporary code that monkeypatches the model classes.
        """
        app_configs = apps.get_app_configs()
        models = tuple(itertools.chain.from_iterable(app_config.get_models() for app_config in app_configs))

        for model in models:
            self.naturalize_model(model)

        for model in models:
            self.naturalize_model_relationships(model)