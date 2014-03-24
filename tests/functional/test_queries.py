#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from django.db.models import F, Q
from django.test import TransactionTestCase

from tests.common.support.models import TestModel


class QueriesTestCase(TransactionTestCase):
    def setUp(self):
        TestModel.objects.create(foo=1)
        TestModel.objects.create(foo=2)
        TestModel.objects.create(foo=3)

    def test_can_fetch_a_record_equal_to_1(self):
        expected = TestModel.objects.get(foo=1)
        actual = TestModel.objects.get(TestModel.foo == 1)

        self.assertEqual(actual, expected)

    def test_can_fetch_records_greater_than_1(self):
        expected = TestModel.objects.filter(foo__gt=1)
        actual = TestModel.objects.filter(TestModel.foo > 1)

        self.assertEqual(list(actual), list(expected))

    def test_can_fetch_records_lower_than_2(self):
        expected = TestModel.objects.filter(foo__lt=2)
        actual = TestModel.objects.filter(TestModel.foo < 2)

        self.assertEqual(list(actual), list(expected))

    def test_can_fetch_records_greater_or_equal_to_bar_plus_one(self):
        expected = TestModel.objects.filter(foo__gte=F('bar') + 1)
        actual = TestModel.objects.filter(TestModel.foo >= TestModel.bar + 1)

        self.assertEqual(list(actual), list(expected))

    def test_can_fetch_records_with_foo_greater_than_one_and_bar_equal_to_one(self):
        expected = TestModel.objects.filter(foo__gt=1, bar=1)
        actual = TestModel.objects.filter((TestModel.foo > 1) & (TestModel.bar == 1))

        self.assertEqual(list(actual), list(expected))