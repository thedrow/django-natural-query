#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db.models import Model, Field
from django.test import SimpleTestCase
from mock import patch
from natural_query.mixins import _mixin, NaturalQueryModelMixin, NaturalQueryFieldMixin


class MixinTestCase(SimpleTestCase):
    def setUp(self):
        self.model_bases = Model.__bases__
        self.field_bases = Field.__bases__

    def tearDown(self):
        Model.__bases__ = self.model_bases
        Field.__bases__ = self.field_bases

    def test_natural_query_model_mixin_is_added_to_the_list_of_base_classes(self):
        sut = expected = NaturalQueryModelMixin

        with patch.object(sut, '__mixin__'):
            _mixin(Model, expected)

        actual = Model.__bases__

        self.assertIn(expected, actual)

    def test_natural_query_field_mixin_is_added_to_the_list_of_base_classes(self):
        expected = NaturalQueryFieldMixin

        _mixin(Field, expected)

        actual = Field.__bases__

        self.assertIn(expected, actual)

    def test_cannot_add_the_same_mixin_twice(self):
        sut = NaturalQueryModelMixin

        with patch.object(sut, '__mixin__') as mocked_mixin:
            _mixin(Model, sut)
            _mixin(Model, sut)

        mocked_mixin.assert_called_once_with(Model)

    def test_mixin_special_method_is_called(self):
        sut = NaturalQueryModelMixin
        with patch.object(sut, '__mixin__') as mocked_mixin:
            _mixin(Model, sut)

        mocked_mixin.assert_called_once_with(Model)
