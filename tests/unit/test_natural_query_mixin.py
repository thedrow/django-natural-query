#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.test import SimpleTestCase

from natural_query.mixins import NaturalQueryModelMixin
from tests.common.support.models import TestModel


class NaturalQueryMixinTestCase(SimpleTestCase):
    def test_when_mixing_in_the_natural_query_mixin_all_the_fields_are_present(self):
        NaturalQueryModelMixin.__mixin__(TestModel)

        fields = dict(TestModel._meta.get_fields_with_model()).keys()

        actual_field_names = set([str(field.name) for field in fields])
        actual_attribute_names = set(dir(TestModel))
        self.assertTrue(actual_field_names.issubset(actual_attribute_names))