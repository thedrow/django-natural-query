#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db.models import F, Q
from django.test import TransactionTestCase

from tests.common.support.models import TestModel


class PrimaryKeyQueriesTestCase(TransactionTestCase):
    def setUp(self):
        TestModel.objects.create(id=1)
        TestModel.objects.create(id=2)
        TestModel.objects.create(id=3)
        TestModel.objects.create(id=4)

    def test_can_fetch_a_record_equal_to_1(self):
        expected = TestModel.objects.get(pk=1)
        actual = TestModel.objects.get(TestModel.pk == 1)

        self.assertEqual(actual, expected)

    def test_pk_is_1_when_fetching_a_record_with_pk_that_is_equal_to_1(self):
        expected = 1
        actual = TestModel.objects.get(TestModel.pk == 1).pk

        self.assertEqual(actual, expected)

    def test_can_fetch_records_greater_than_1(self):
        expected = TestModel.objects.filter(pk__gt=1)
        actual = TestModel.objects.filter(TestModel.pk > 1)

        self.assertEqual(list(actual), list(expected))

    def test_can_fetch_records_lower_than_2(self):
        expected = TestModel.objects.filter(pk__lt=2)
        actual = TestModel.objects.filter(TestModel.pk < 2)

        self.assertEqual(list(actual), list(expected))

    def test_can_fetch_records_greater_or_equal_to_bar_plus_one(self):
        expected = TestModel.objects.filter(pk__gte=F('bar') + 1)
        actual = TestModel.objects.filter(TestModel.pk >= TestModel.bar + 1)

        self.assertEqual(list(actual), list(expected))

    def test_can_fetch_records_with_pk_greater_than_one_and_bar_equal_to_one(self):
        expected = TestModel.objects.filter(pk__gt=1, bar=1)
        actual = TestModel.objects.filter((TestModel.pk > 1) & (TestModel.bar == 1))

        self.assertEqual(list(actual), list(expected))

    def test_can_fetch_records_with_pk_greater_than_one_or_bar_equal_to_one(self):
        expected = TestModel.objects.filter(Q(pk__gt=1) | Q(bar=1))
        actual = TestModel.objects.filter((TestModel.pk > 1) | (TestModel.bar == 1))

        self.assertEqual(list(actual), list(expected))