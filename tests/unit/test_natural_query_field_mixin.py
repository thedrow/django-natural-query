#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db.models import Q

from django.test import SimpleTestCase
from mock import sentinel

from natural_query.mixins import NaturalQueryFieldMixin


class NaturalQueryFieldMixinTestCase(SimpleTestCase):
        @property
        def system_under_test(self):
            sut = NaturalQueryFieldMixin()
            sut.name = 'field'

            return sut

        def test_equals_operator_generates_the_right_expression_for_the_exact_lookup(self):
            sut = self.system_under_test
            expected = str(Q(field__exact=sentinel.VALUE))

            actual = str(sut == sentinel.VALUE)

            self.assertEqual(str(actual), str(expected))



