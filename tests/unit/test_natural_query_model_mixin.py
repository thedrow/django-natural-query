#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.test import SimpleTestCase
from mock import patch, call

from natural_query.mixins import NaturalQueryModelMixin, NaturalQueryFieldMixin
from tests.common.support.models import TestModel


class NaturalQueryMixinTestCase(SimpleTestCase):
    def test_when_mixing_in_the_natural_query_mixin_all_the_fields_are_present(self):
        with patch('natural_query.mixins._mixin'):
            NaturalQueryModelMixin.__mixin__(TestModel)

        fields = dict(TestModel._meta.get_fields_with_model()).keys()

        actual_field_names = set([str(field.name) for field in fields])
        actual_attribute_names = set(dir(TestModel))
        self.assertTrue(actual_field_names.issubset(actual_attribute_names))

    def test_when_mixing_in_the_natural_query_mixin_all_the_fields_are_subclasses_of_natural_query_field_mixin(self):
        with patch('natural_query.mixins._mixin') as mocked_mixin:
            NaturalQueryModelMixin.__mixin__(TestModel)

        fields = dict(TestModel._meta.get_fields_with_model()).keys()
        for field in fields:
            self.assertIn(call(field, NaturalQueryFieldMixin), mocked_mixin.call_args_list)