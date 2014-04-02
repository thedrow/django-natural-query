#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db.models import F, Q
from django.test import TransactionTestCase

from tests.common.support.models import TestModel, TestModel2


class PrimaryKeyQueriesTestCase(TransactionTestCase):
    def setUp(self):
        test_model_2_1 = TestModel2.objects.create(id=1)
        test_model_2_2 = TestModel2.objects.create(id=2)

        TestModel.objects.create(id=1, test_model_2=test_model_2_1)
        TestModel.objects.create(id=2, test_model_2=test_model_2_2)
        TestModel.objects.create(id=3, test_model_2=test_model_2_2)
        TestModel.objects.create(id=4)

    def test_can_fetch_a_record_equal_to_1(self):
        expected = TestModel.objects.get(test_model_2_id=1)
        actual = TestModel.objects.get(TestModel.test_model_2_id == 1)

        self.assertEqual(actual, expected)

    def test_test_model_2_id_is_1_when_fetching_a_record_with_test_model_2_id_that_is_equal_to_1(self):
        expected = 1
        actual = TestModel.objects.get(TestModel.test_model_2_id == 1).test_model_2_id

        self.assertEqual(actual, expected)

    def test_can_fetch_records_greater_than_1(self):
        expected = TestModel.objects.filter(test_model_2_id__gt=1)
        actual = TestModel.objects.filter(TestModel.test_model_2_id > 1)

        self.assertEqual(list(actual), list(expected))

    def test_can_fetch_records_lower_than_2(self):
        expected = TestModel.objects.filter(test_model_2_id__lt=2)
        actual = TestModel.objects.filter(TestModel.test_model_2_id < 2)

        self.assertEqual(list(actual), list(expected))

    def test_can_fetch_records_greater_or_equal_to_bar_plus_one(self):
        expected = TestModel.objects.filter(test_model_2_id__gte=F('bar') + 1)
        actual = TestModel.objects.filter(TestModel.test_model_2_id >= TestModel.bar + 1)

        self.assertEqual(list(actual), list(expected))

    def test_can_fetch_records_with_test_model_2_id_greater_than_one_and_bar_equal_to_one(self):
        expected = TestModel.objects.filter(test_model_2_id__gt=1, bar=1)
        actual = TestModel.objects.filter((TestModel.test_model_2_id > 1) & (TestModel.bar == 1))

        self.assertEqual(list(actual), list(expected))

    def test_can_fetch_records_with_test_model_2_id_greater_than_one_or_bar_equal_to_one(self):
        expected = TestModel.objects.filter(Q(test_model_2_id__gt=1) | Q(bar=1))
        actual = TestModel.objects.filter((TestModel.test_model_2_id > 1) | (TestModel.bar == 1))

        self.assertEqual(list(actual), list(expected))