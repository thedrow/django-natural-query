#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db.models import Model
from django.test import SimpleTestCase
from natural_query.mixins import _mixin, NaturalQueryMixin


class MixinTestCase(SimpleTestCase):
    def test_mixin_is_added_to_the_list_of_base_classes(self):
        expected = NaturalQueryMixin

        _mixin(Model, expected)
        actual = Model.__bases__

        self.assertIn(expected, actual)