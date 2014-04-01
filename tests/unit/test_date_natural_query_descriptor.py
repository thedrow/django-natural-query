from unittest import skip

from django.db.models import Q, F
from django.test import SimpleTestCase
from mock import sentinel

from natural_query.query import DateNaturalQueryDescriptor
from tests.unit.support import assertQObjectsEqual


class DateNaturalQueryDescriptorTestCase(SimpleTestCase):
    def setUp(self):
        self.addTypeEqualityFunc(Q, assertQObjectsEqual)

    @property
    def system_under_test(self):
        sut = DateNaturalQueryDescriptor('field')

        return sut

    @property
    def field(self):
        return DateNaturalQueryDescriptor(name='field2')

    def test_equals_operator_generates_the_right_expression_for_the_exact_year_lookup(self):
        sut = self.system_under_test
        expected = Q(field__year=sentinel.VALUE)

        actual = sut.year == sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_concated_equals_operator_generates_the_right_expression_for_the_exact_year_lookup(self):
        sut = self.system_under_test
        expected = Q(field__year=sentinel.VALUE)

        actual = sentinel.VALUE == sut.year == sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_equals_operator_generates_the_right_expression_for_the_exact_year_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__year=F('field2'))

        actual = sut.year == self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_greater_than_operator_generates_the_right_expression_for_the_gt_year_lookup(self):
        sut = self.system_under_test
        expected = Q(field__year__gt=sentinel.VALUE)

        actual = sut.year > sentinel.VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_greater_than_operator_generates_the_right_expression_for_the_gt_year_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__year__gt=F('field2'))

        actual = sut.year > self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_greater_than_or_equal_operator_generates_the_right_expression_for_the_gte_year_lookup(self):
        sut = self.system_under_test
        expected = Q(field__year__gte=sentinel.VALUE)

        actual = sut.year >= sentinel.VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_greater_than_or_equal_operator_generates_the_right_expression_for_the_gte_year_lookup_when_comparing_to_another_field(

            self):
        sut = self.system_under_test
        expected = Q(field__year__gte=F('field2'))

        actual = sut.year >= self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_less_than_operator_generates_the_right_expression_for_the_lt_year_lookup(self):
        sut = self.system_under_test
        expected = Q(field__year__lt=sentinel.VALUE)

        actual = sut.year < sentinel.VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_less_than_operator_generates_the_right_expression_for_the_lt_year_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__year__lt=F('field2'))

        actual = sut.year < self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_less_than_or_equal_operator_generates_the_right_expression_for_the_lte_year_lookup(self):
        sut = self.system_under_test
        expected = Q(field__year__lte=sentinel.VALUE)

        actual = sut.year <= sentinel.VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_less_than_or_equal_operator_generates_the_right_expression_for_the_lte_year_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__year__lte=F('field2'))

        actual = sut.year <= self.field

        self.assertEqual(actual, expected)

    def test_not_equal_operator_generates_the_right_negated_expression_for_the_exact_year_lookup(self):
        sut = self.system_under_test
        expected = ~Q(field__year=sentinel.VALUE)

        actual = sut.year != sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_not_equal_operator_generates_the_right_negated_expression_for_the_exact_year_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = ~Q(field__year=F('field2'))

        actual = sut.year != self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_concated_gte_operator_generates_the_right_expression_for_the_greater_than_or_equal_year_lookup(self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__year__gte=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE <= sut.year >= sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_concated_gt_operator_generates_the_right_expression_for_the_greater_than_year_lookup(self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__year__gt=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE < sut.year > sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_concated_gte_and_gt_operator_generates_the_right_expression_for_the_greater_than_year_lookup(self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__year__gt=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE <= sut.year > sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_concated_gt_and_gte_operator_generates_the_right_expression_for_the_greater_than_or_equal_year_lookup(
            self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__year__gte=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE < sut.year >= sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    def test_can_and_expressions_when_braces_are_present(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__year=sentinel.VALUE1, field2__year=sentinel.VALUE2)

        actual = (field1.year == sentinel.VALUE1) & (field2.year == sentinel.VALUE2)

        self.assertEqual(actual, expected)

    def test_can_or_expressions_when_braces_are_present(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__year=sentinel.VALUE1) | Q(field2__year=sentinel.VALUE2)

        actual = (field1.year == sentinel.VALUE1) | (field2.year == sentinel.VALUE2)

        self.assertEqual(actual, expected)

    def test_can_add_to_field_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__year=F('field__year') + sentinel.VALUE)

        actual = sut.year == sut.year + sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_substract_from_field_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__year=F('field__year') - sentinel.VALUE)

        actual = sut.year == sut.year - sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_multiply_field_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__year=F('field__year') * sentinel.VALUE)

        actual = sut.year == sut.year * sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_divide_field_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__year=F('field__year') / sentinel.VALUE)

        actual = sut.year == sut.year / sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_raise_to_power_field_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__year=pow(F('field__year'), sentinel.VALUE))

        actual = sut.year == pow(F('field__year'), sentinel.VALUE)

        self.assertEqual(actual, expected)

    def test_can_mod_field_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__year=F('field__year') % sentinel.VALUE)

        actual = sut.year == sut.year % sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_add_value_to_field_and_compare(self):
        sut = self.system_under_test

        # For some reason this test fails with a sentinel. I used a real value instead.
        expected = Q(field__year=1 + F('field'))

        actual = sut.year == 1 + sut

        self.assertEqual(actual, expected)

    def test_can_substract_value_from_field_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__year=sentinel.VALUE - F('field'))

        actual = sut.year == sentinel.VALUE - sut

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iexact_generates_the_right_expression_for_the_iexact_year_lookup(self):
        sut = self.system_under_test

        expected = Q(field__year__iexact=sentinel.VALUE)

        actual = sut.year.iexact(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iexact_generates_the_right_expression_for_the_iexact_year_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__year__iexact=F('field2'))

        actual = field1.year.iexact(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_contains_generates_the_right_expression_for_the_contains_year_lookup(self):
        sut = self.system_under_test

        expected = Q(field__year__contains=sentinel.VALUE)

        actual = sut.year.contains(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_contains_generates_the_right_expression_for_the_contains_year_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__year__contains=F('field2'))

        actual = field1.year.contains(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_icontains_generates_the_right_expression_for_the_icontains_year_lookup(self):
        sut = self.system_under_test

        expected = Q(field__year__icontains=sentinel.VALUE)

        actual = sut.year.icontains(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_icontains_generates_the_right_expression_for_the_icontains_year_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__year__icontains=F('field2'))

        actual = field1.year.icontains(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_startswith_generates_the_right_expression_for_the_startswith_year_lookup(self):
        sut = self.system_under_test

        expected = Q(field__year__startswith=sentinel.VALUE)

        actual = sut.year.startswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_startswith_generates_the_right_expression_for_the_startswith_year_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__year__startswith=F('field2'))

        actual = field1.year.startswith(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_istartswith_generates_the_right_expression_for_the_istartswith_year_lookup(self):
        sut = self.system_under_test

        expected = Q(field__year__istartswith=sentinel.VALUE)

        actual = sut.year.istartswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_istartswith_generates_the_right_expression_for_the_istartswith_year_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__year__istartswith=F('field2'))

        actual = field1.year.istartswith(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_endswith_generates_the_right_expression_for_the_endswith_year_lookup(self):
        sut = self.system_under_test

        expected = Q(field__year__endswith=sentinel.VALUE)

        actual = sut.year.endswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_endswith_generates_the_right_expression_for_the_endswith_year_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__year__endswith=F('field2'))

        actual = field1.year.endswith(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iendswith_generates_the_right_expression_for_the_iendswith_year_lookup(self):
        sut = self.system_under_test

        expected = Q(field__year__iendswith=sentinel.VALUE)

        actual = sut.year.iendswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iendswith_generates_the_right_expression_for_the_iendswith_year_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__year__iendswith=F('field2'))

        actual = field1.year.iendswith(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_search_generates_the_right_expression_for_the_search_year_lookup(self):
        sut = self.system_under_test

        expected = Q(field__year__search=sentinel.VALUE)

        actual = sut.year.search(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_search_generates_the_right_expression_for_the_search_year_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__year__search=F('field2'))

        actual = field1.year.search(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_regex_generates_the_right_expression_for_the_regex_year_lookup(self):
        sut = self.system_under_test

        expected = Q(field__year__regex=sentinel.VALUE)

        actual = sut.year.regex(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_regex_generates_the_right_expression_for_the_regex_year_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__year__regex=F('field2'))

        actual = field1.year.regex(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iregex_generates_the_right_expression_for_the_iregex_year_lookup(self):
        sut = self.system_under_test

        expected = Q(field__year__iregex=sentinel.VALUE)

        actual = sut.year.iregex(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iregex_generates_the_right_expression_for_the_iregex_year_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__year__iregex=F('field2'))

        actual = field1.year.iregex(field2)

        self.assertEqual(actual, expected)

    def test_equals_operator_generates_the_right_expression_for_the_exact_month_lookup(self):
        sut = self.system_under_test
        expected = Q(field__month=sentinel.VALUE)

        actual = sut.month == sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_concated_equals_operator_generates_the_right_expression_for_the_exact_month_lookup(self):
        sut = self.system_under_test
        expected = Q(field__month=sentinel.VALUE)

        actual = sentinel.VALUE == sut.month == sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_equals_operator_generates_the_right_expression_for_the_exact_month_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__month=F('field2'))

        actual = sut.month == self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_greater_than_operator_generates_the_right_expression_for_the_gt_month_lookup(self):
        sut = self.system_under_test
        expected = Q(field__month__gt=sentinel.VALUE)

        actual = sut.month > sentinel.VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_greater_than_operator_generates_the_right_expression_for_the_gt_month_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__month__gt=F('field2'))

        actual = sut.month > self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_greater_than_or_equal_operator_generates_the_right_expression_for_the_gte_month_lookup(self):
        sut = self.system_under_test
        expected = Q(field__month__gte=sentinel.VALUE)

        actual = sut.month >= sentinel.VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_greater_than_or_equal_operator_generates_the_right_expression_for_the_gte_month_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__month__gte=F('field2'))

        actual = sut.month >= self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_less_than_operator_generates_the_right_expression_for_the_lt_month_lookup(self):
        sut = self.system_under_test
        expected = Q(field__month__lt=sentinel.VALUE)

        actual = sut.month < sentinel.VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_less_than_operator_generates_the_right_expression_for_the_lt_month_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__month__lt=F('field2'))

        actual = sut.month < self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_less_than_or_equal_operator_generates_the_right_expression_for_the_lte_month_lookup(self):
        sut = self.system_under_test
        expected = Q(field__month__lte=sentinel.VALUE)

        actual = sut.month <= sentinel.VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_less_than_or_equal_operator_generates_the_right_expression_for_the_lte_month_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__month__lte=F('field2'))

        actual = sut.month <= self.field

        self.assertEqual(actual, expected)

    def test_not_equal_operator_generates_the_right_negated_expression_for_the_exact_month_lookup(self):
        sut = self.system_under_test
        expected = ~Q(field__month=sentinel.VALUE)

        actual = sut.month != sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_not_equal_operator_generates_the_right_negated_expression_for_the_exact_month_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = ~Q(field__month=F('field2'))

        actual = sut.month != self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_concated_gte_operator_generates_the_right_expression_for_the_greater_than_or_equal_month_lookup(self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__month__gte=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE <= sut.month >= sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_concated_gt_operator_generates_the_right_expression_for_the_greater_than_month_lookup(self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__month__gt=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE < sut.month > sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_concated_gte_and_gt_operator_generates_the_right_expression_for_the_greater_than_month_lookup(self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__month__gt=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE <= sut.month > sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_concated_gt_and_gte_operator_generates_the_right_expression_for_the_greater_than_or_equal_month_lookup(
            self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__month__gte=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE < sut.month >= sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    def test_can_and_expressions_referring_to_year_when_braces_are_present(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__month=sentinel.VALUE1, field2__month=sentinel.VALUE2)

        actual = (field1.month == sentinel.VALUE1) & (field2.month == sentinel.VALUE2)

        self.assertEqual(actual, expected)

    def test_can_or_expressions_referring_to_year_when_braces_are_present(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__month=sentinel.VALUE1) | Q(field2__month=sentinel.VALUE2)

        actual = (field1.month == sentinel.VALUE1) | (field2.month == sentinel.VALUE2)

        self.assertEqual(actual, expected)

    def test_can_add_to_field_year_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__month=F('field__month') + sentinel.VALUE)

        actual = sut.month == sut.month + sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_substract_from_field_year_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__month=F('field__month') - sentinel.VALUE)

        actual = sut.month == sut.month - sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_multiply_field_year_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__month=F('field__month') * sentinel.VALUE)

        actual = sut.month == sut.month * sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_divide_field_year_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__month=F('field__month') / sentinel.VALUE)

        actual = sut.month == sut.month / sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_raise_to_power_field_year_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__month=pow(F('field__month'), sentinel.VALUE))

        actual = sut.month == pow(F('field__month'), sentinel.VALUE)

        self.assertEqual(actual, expected)

    def test_can_mod_field_year_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__month=F('field__month') % sentinel.VALUE)

        actual = sut.month == sut.month % sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_add_value_to_field_year_and_compare(self):
        sut = self.system_under_test

        # For some reason this test fails with a sentinel. I used a real value instead.
        expected = Q(field__month=1 + F('field'))

        actual = sut.month == 1 + sut

        self.assertEqual(actual, expected)

    def test_can_substract_value_from_field_year_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__month=sentinel.VALUE - F('field'))

        actual = sut.month == sentinel.VALUE - sut

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iexact_generates_the_right_expression_for_the_iexact_month_lookup(self):
        sut = self.system_under_test

        expected = Q(field__month__iexact=sentinel.VALUE)

        actual = sut.month.iexact(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iexact_generates_the_right_expression_for_the_iexact_month_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__month__iexact=F('field2'))

        actual = field1.month.iexact(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_contains_generates_the_right_expression_for_the_contains_month_lookup(self):
        sut = self.system_under_test

        expected = Q(field__month__contains=sentinel.VALUE)

        actual = sut.month.contains(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_contains_generates_the_right_expression_for_the_contains_month_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__month__contains=F('field2'))

        actual = field1.month.contains(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_icontains_generates_the_right_expression_for_the_icontains_month_lookup(self):
        sut = self.system_under_test

        expected = Q(field__month__icontains=sentinel.VALUE)

        actual = sut.month.icontains(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_icontains_generates_the_right_expression_for_the_icontains_month_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__month__icontains=F('field2'))

        actual = field1.month.icontains(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_startswith_generates_the_right_expression_for_the_startswith_month_lookup(self):
        sut = self.system_under_test

        expected = Q(field__month__startswith=sentinel.VALUE)

        actual = sut.month.startswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_startswith_generates_the_right_expression_for_the_startswith_month_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__month__startswith=F('field2'))

        actual = field1.month.startswith(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_istartswith_generates_the_right_expression_for_the_istartswith_month_lookup(self):
        sut = self.system_under_test

        expected = Q(field__month__istartswith=sentinel.VALUE)

        actual = sut.month.istartswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_istartswith_generates_the_right_expression_for_the_istartswith_month_lookup_when_comparing_to_a_field(
            self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__month__istartswith=F('field2'))

        actual = field1.month.istartswith(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_endswith_generates_the_right_expression_for_the_endswith_month_lookup(self):
        sut = self.system_under_test

        expected = Q(field__month__endswith=sentinel.VALUE)

        actual = sut.month.endswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_endswith_generates_the_right_expression_for_the_endswith_month_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__month__endswith=F('field2'))

        actual = field1.month.endswith(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iendswith_generates_the_right_expression_for_the_iendswith_month_lookup(self):
        sut = self.system_under_test

        expected = Q(field__month__iendswith=sentinel.VALUE)

        actual = sut.month.iendswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iendswith_generates_the_right_expression_for_the_iendswith_month_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__month__iendswith=F('field2'))

        actual = field1.month.iendswith(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_search_generates_the_right_expression_for_the_search_month_lookup(self):
        sut = self.system_under_test

        expected = Q(field__month__search=sentinel.VALUE)

        actual = sut.month.search(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_search_generates_the_right_expression_for_the_search_month_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__month__search=F('field2'))

        actual = field1.month.search(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_regex_generates_the_right_expression_for_the_regex_month_lookup(self):
        sut = self.system_under_test

        expected = Q(field__month__regex=sentinel.VALUE)

        actual = sut.month.regex(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_regex_generates_the_right_expression_for_the_regex_month_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__month__regex=F('field2'))

        actual = field1.month.regex(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iregex_generates_the_right_expression_for_the_iregex_month_lookup(self):
        sut = self.system_under_test

        expected = Q(field__month__iregex=sentinel.VALUE)

        actual = sut.month.iregex(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iregex_generates_the_right_expression_for_the_iregex_month_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__month__iregex=F('field2'))

        actual = field1.month.iregex(field2)

        self.assertEqual(actual, expected)

    def test_equals_operator_generates_the_right_expression_for_the_exact_day_lookup(self):
        sut = self.system_under_test
        expected = Q(field__day=sentinel.VALUE)

        actual = sut.day == sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_concated_equals_operator_generates_the_right_expression_for_the_exact_day_lookup(self):
        sut = self.system_under_test
        expected = Q(field__day=sentinel.VALUE)

        actual = sentinel.VALUE == sut.day == sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_equals_operator_generates_the_right_expression_for_the_exact_day_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__day=F('field2'))

        actual = sut.day == self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_greater_than_operator_generates_the_right_expression_for_the_gt_day_lookup(self):
        sut = self.system_under_test
        expected = Q(field__day__gt=sentinel.VALUE)

        actual = sut.day > sentinel.VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_greater_than_operator_generates_the_right_expression_for_the_gt_day_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__day__gt=F('field2'))

        actual = sut.day > self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_greater_than_or_equal_operator_generates_the_right_expression_for_the_gte_day_lookup(self):
        sut = self.system_under_test
        expected = Q(field__day__gte=sentinel.VALUE)

        actual = sut.day >= sentinel.VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_greater_than_or_equal_operator_generates_the_right_expression_for_the_gte_day_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__day__gte=F('field2'))

        actual = sut.day >= self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_less_than_operator_generates_the_right_expression_for_the_lt_day_lookup(self):
        sut = self.system_under_test
        expected = Q(field__day__lt=sentinel.VALUE)

        actual = sut.day < sentinel.VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_less_than_operator_generates_the_right_expression_for_the_lt_day_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__day__lt=F('field2'))

        actual = sut.day < self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_less_than_or_equal_operator_generates_the_right_expression_for_the_lte_day_lookup(self):
        sut = self.system_under_test
        expected = Q(field__day__lte=sentinel.VALUE)

        actual = sut.day <= sentinel.VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_less_than_or_equal_operator_generates_the_right_expression_for_the_lte_day_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__day__lte=F('field2'))

        actual = sut.day <= self.field

        self.assertEqual(actual, expected)

    def test_not_equal_operator_generates_the_right_negated_expression_for_the_exact_day_lookup(self):
        sut = self.system_under_test
        expected = ~Q(field__day=sentinel.VALUE)

        actual = sut.day != sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_not_equal_operator_generates_the_right_negated_expression_for_the_exact_day_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = ~Q(field__day=F('field2'))

        actual = sut.day != self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_concated_gte_operator_generates_the_right_expression_for_the_greater_than_or_equal_day_lookup(self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__day__gte=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE <= sut.day >= sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_concated_gt_operator_generates_the_right_expression_for_the_greater_than_day_lookup(self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__day__gt=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE < sut.day > sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_concated_gte_and_gt_operator_generates_the_right_expression_for_the_greater_than_day_lookup(self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__day__gt=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE <= sut.day > sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_concated_gt_and_gte_operator_generates_the_right_expression_for_the_greater_than_or_equal_day_lookup(self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__day__gte=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE < sut.day >= sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    def test_can_and_expressions_referring_to_day_when_braces_are_present(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__day=sentinel.VALUE1, field2__day=sentinel.VALUE2)

        actual = (field1.day == sentinel.VALUE1) & (field2.day == sentinel.VALUE2)

        self.assertEqual(actual, expected)

    def test_can_or_expressions_referring_to_day_when_braces_are_present(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__day=sentinel.VALUE1) | Q(field2__day=sentinel.VALUE2)

        actual = (field1.day == sentinel.VALUE1) | (field2.day == sentinel.VALUE2)

        self.assertEqual(actual, expected)

    def test_can_add_to_field_day_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__day=F('field__day') + sentinel.VALUE)

        actual = sut.day == sut.day + sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_substract_from_field_day_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__day=F('field__day') - sentinel.VALUE)

        actual = sut.day == sut.day - sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_multiply_field_day_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__day=F('field__day') * sentinel.VALUE)

        actual = sut.day == sut.day * sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_divide_field_day_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__day=F('field__day') / sentinel.VALUE)

        actual = sut.day == sut.day / sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_raise_to_power_field_day_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__day=pow(F('field__day'), sentinel.VALUE))

        actual = sut.day == pow(F('field__day'), sentinel.VALUE)

        self.assertEqual(actual, expected)

    def test_can_mod_field_day_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__day=F('field__day') % sentinel.VALUE)

        actual = sut.day == sut.day % sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_add_value_to_field_day_and_compare(self):
        sut = self.system_under_test

        # For some reason this test fails with a sentinel. I used a real value instead.
        expected = Q(field__day=1 + F('field'))

        actual = sut.day == 1 + sut

        self.assertEqual(actual, expected)

    def test_can_substract_value_from_field_day_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__day=sentinel.VALUE - F('field'))

        actual = sut.day == sentinel.VALUE - sut

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iexact_generates_the_right_expression_for_the_iexact_day_lookup(self):
        sut = self.system_under_test

        expected = Q(field__day__iexact=sentinel.VALUE)

        actual = sut.day.iexact(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iexact_generates_the_right_expression_for_the_iexact_day_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__day__iexact=F('field2'))

        actual = field1.day.iexact(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_contains_generates_the_right_expression_for_the_contains_day_lookup(self):
        sut = self.system_under_test

        expected = Q(field__day__contains=sentinel.VALUE)

        actual = sut.day.contains(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_contains_generates_the_right_expression_for_the_contains_day_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__day__contains=F('field2'))

        actual = field1.day.contains(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_icontains_generates_the_right_expression_for_the_icontains_day_lookup(self):
        sut = self.system_under_test

        expected = Q(field__day__icontains=sentinel.VALUE)

        actual = sut.day.icontains(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_icontains_generates_the_right_expression_for_the_icontains_day_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__day__icontains=F('field2'))

        actual = field1.day.icontains(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_startswith_generates_the_right_expression_for_the_startswith_day_lookup(self):
        sut = self.system_under_test

        expected = Q(field__day__startswith=sentinel.VALUE)

        actual = sut.day.startswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_startswith_generates_the_right_expression_for_the_startswith_day_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__day__startswith=F('field2'))

        actual = field1.day.startswith(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_istartswith_generates_the_right_expression_for_the_istartswith_day_lookup(self):
        sut = self.system_under_test

        expected = Q(field__day__istartswith=sentinel.VALUE)

        actual = sut.day.istartswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_istartswith_generates_the_right_expression_for_the_istartswith_day_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__day__istartswith=F('field2'))

        actual = field1.day.istartswith(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_endswith_generates_the_right_expression_for_the_endswith_day_lookup(self):
        sut = self.system_under_test

        expected = Q(field__day__endswith=sentinel.VALUE)

        actual = sut.day.endswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_endswith_generates_the_right_expression_for_the_endswith_day_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__day__endswith=F('field2'))

        actual = field1.day.endswith(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iendswith_generates_the_right_expression_for_the_iendswith_day_lookup(self):
        sut = self.system_under_test

        expected = Q(field__day__iendswith=sentinel.VALUE)

        actual = sut.day.iendswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iendswith_generates_the_right_expression_for_the_iendswith_day_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__day__iendswith=F('field2'))

        actual = field1.day.iendswith(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_search_generates_the_right_expression_for_the_search_day_lookup(self):
        sut = self.system_under_test

        expected = Q(field__day__search=sentinel.VALUE)

        actual = sut.day.search(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_search_generates_the_right_expression_for_the_search_day_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__day__search=F('field2'))

        actual = field1.day.search(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_regex_generates_the_right_expression_for_the_regex_day_lookup(self):
        sut = self.system_under_test

        expected = Q(field__day__regex=sentinel.VALUE)

        actual = sut.day.regex(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_regex_generates_the_right_expression_for_the_regex_day_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__day__regex=F('field2'))

        actual = field1.day.regex(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iregex_generates_the_right_expression_for_the_iregex_day_lookup(self):
        sut = self.system_under_test

        expected = Q(field__day__iregex=sentinel.VALUE)

        actual = sut.day.iregex(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iregex_generates_the_right_expression_for_the_iregex_day_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__day__iregex=F('field2'))

        actual = field1.day.iregex(field2)

        self.assertEqual(actual, expected)

    def test_equals_operator_generates_the_right_expression_for_the_exact_week_day_lookup(self):
        sut = self.system_under_test
        expected = Q(field__week_day=sentinel.VALUE)

        actual = sut.week_day == sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_concated_equals_operator_generates_the_right_expression_for_the_exact_week_day_lookup(self):
        sut = self.system_under_test
        expected = Q(field__week_day=sentinel.VALUE)

        actual = sentinel.VALUE == sut.week_day == sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_equals_operator_generates_the_right_expression_for_the_exact_week_day_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__week_day=F('field2'))

        actual = sut.week_day == self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_greater_than_operator_generates_the_right_expression_for_the_gt_week_day_lookup(self):
        sut = self.system_under_test
        expected = Q(field__week_day__gt=sentinel.VALUE)

        actual = sut.week_day > sentinel.VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_greater_than_operator_generates_the_right_expression_for_the_gt_week_day_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__week_day__gt=F('field2'))

        actual = sut.week_day > self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_greater_than_or_equal_operator_generates_the_right_expression_for_the_gte_week_day_lookup(self):
        sut = self.system_under_test
        expected = Q(field__week_day__gte=sentinel.VALUE)

        actual = sut.week_day >= sentinel.VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_greater_than_or_equal_operator_generates_the_right_expression_for_the_gte_week_day_lookup_when_comparing_to_another_field(

            self):
        sut = self.system_under_test
        expected = Q(field__week_day__gte=F('field2'))

        actual = sut.week_day >= self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_less_than_operator_generates_the_right_expression_for_the_lt_week_day_lookup(self):
        sut = self.system_under_test
        expected = Q(field__week_day__lt=sentinel.VALUE)

        actual = sut.week_day < sentinel.VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_less_than_operator_generates_the_right_expression_for_the_lt_week_day_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__week_day__lt=F('field2'))

        actual = sut.week_day < self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_less_than_or_equal_operator_generates_the_right_expression_for_the_lte_week_day_lookup(self):
        sut = self.system_under_test
        expected = Q(field__week_day__lte=sentinel.VALUE)

        actual = sut.week_day <= sentinel.VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_less_than_or_equal_operator_generates_the_right_expression_for_the_lte_week_day_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__week_day__lte=F('field2'))

        actual = sut.week_day <= self.field

        self.assertEqual(actual, expected)

    def test_not_equal_operator_generates_the_right_negated_expression_for_the_exact_week_day_lookup(self):
        sut = self.system_under_test
        expected = ~Q(field__week_day=sentinel.VALUE)

        actual = sut.week_day != sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_not_equal_operator_generates_the_right_negated_expression_for_the_exact_week_day_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = ~Q(field__week_day=F('field2'))

        actual = sut.week_day != self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_concated_gte_operator_generates_the_right_expression_for_the_greater_than_or_equal_week_day_lookup(self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__week_day__gte=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE <= sut.week_day >= sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_concated_gt_operator_generates_the_right_expression_for_the_greater_than_week_day_lookup(self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__week_day__gt=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE < sut.week_day > sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_concated_gte_and_gt_operator_generates_the_right_expression_for_the_greater_than_week_day_lookup(self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__week_day__gt=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE <= sut.week_day > sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_concated_gt_and_gte_operator_generates_the_right_expression_for_the_greater_than_or_equal_week_day_lookup(
            self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__week_day__gte=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE < sut.week_day >= sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    def test_can_and_expressions_referring_to_week_day_when_braces_are_present(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__week_day=sentinel.VALUE1, field2__week_day=sentinel.VALUE2)

        actual = (field2.week_day == sentinel.VALUE2) & (field1.week_day == sentinel.VALUE1)

        self.assertEqual(actual, expected)

    def test_can_or_expressions_referring_to_week_day_when_braces_are_present(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__week_day=sentinel.VALUE1) | Q(field2__week_day=sentinel.VALUE2)

        actual = (field1.week_day == sentinel.VALUE1) | (field2.week_day == sentinel.VALUE2)

        self.assertEqual(actual, expected)

    def test_can_add_to_field_week_day_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__week_day=F('field__week_day') + sentinel.VALUE)

        actual = sut.week_day == sut.week_day + sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_substract_from_field_week_day_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__week_day=F('field__week_day') - sentinel.VALUE)

        actual = sut.week_day == sut.week_day - sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_multiply_field_week_day_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__week_day=F('field__week_day') * sentinel.VALUE)

        actual = sut.week_day == sut.week_day * sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_divide_field_week_day_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__week_day=F('field__week_day') / sentinel.VALUE)

        actual = sut.week_day == sut.week_day / sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_raise_to_power_field_week_day_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__week_day=pow(F('field__week_day'), sentinel.VALUE))

        actual = sut.week_day == pow(F('field__week_day'), sentinel.VALUE)

        self.assertEqual(actual, expected)

    def test_can_mod_field_week_day_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__week_day=F('field__week_day') % sentinel.VALUE)

        actual = sut.week_day == sut.week_day % sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_add_week_day_value_to_field_and_compare(self):
        sut = self.system_under_test

        # For some reason this test fails with a sentinel. I used a real value instead.
        expected = Q(field__week_day=1 + F('field'))

        actual = sut.week_day == 1 + sut

        self.assertEqual(actual, expected)

    def test_can_substract_week_day_value_from_field_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__week_day=sentinel.VALUE - F('field'))

        actual = sut.week_day == sentinel.VALUE - sut

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iexact_generates_the_right_expression_for_the_iexact_week_day_lookup(self):
        sut = self.system_under_test

        expected = Q(field__week_day__iexact=sentinel.VALUE)

        actual = sut.week_day.iexact(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iexact_generates_the_right_expression_for_the_iexact_week_day_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__week_day__iexact=F('field2'))

        actual = field1.week_day.iexact(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_contains_generates_the_right_expression_for_the_contains_week_day_lookup(self):
        sut = self.system_under_test

        expected = Q(field__week_day__contains=sentinel.VALUE)

        actual = sut.week_day.contains(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_contains_generates_the_right_expression_for_the_contains_week_day_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__week_day__contains=F('field2'))

        actual = field1.week_day.contains(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_icontains_generates_the_right_expression_for_the_icontains_week_day_lookup(self):
        sut = self.system_under_test

        expected = Q(field__week_day__icontains=sentinel.VALUE)

        actual = sut.week_day.icontains(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_icontains_generates_the_right_expression_for_the_icontains_week_day_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__week_day__icontains=F('field2'))

        actual = field1.week_day.icontains(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_startswith_generates_the_right_expression_for_the_startswith_week_day_lookup(self):
        sut = self.system_under_test

        expected = Q(field__week_day__startswith=sentinel.VALUE)

        actual = sut.week_day.startswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_startswith_generates_the_right_expression_for_the_startswith_week_day_lookup_when_comparing_to_a_field(
            self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__week_day__startswith=F('field2'))

        actual = field1.week_day.startswith(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_istartswith_generates_the_right_expression_for_the_istartswith_week_day_lookup(self):
        sut = self.system_under_test

        expected = Q(field__week_day__istartswith=sentinel.VALUE)

        actual = sut.week_day.istartswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_istartswith_generates_the_right_expression_for_the_istartswith_week_day_lookup_when_comparing_to_a_field(
            self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__week_day__istartswith=F('field2'))

        actual = field1.week_day.istartswith(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_endswith_generates_the_right_expression_for_the_endswith_week_day_lookup(self):
        sut = self.system_under_test

        expected = Q(field__week_day__endswith=sentinel.VALUE)

        actual = sut.week_day.endswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_endswith_generates_the_right_expression_for_the_endswith_week_day_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__week_day__endswith=F('field2'))

        actual = field1.week_day.endswith(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iendswith_generates_the_right_expression_for_the_iendswith_week_day_lookup(self):
        sut = self.system_under_test

        expected = Q(field__week_day__iendswith=sentinel.VALUE)

        actual = sut.week_day.iendswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iendswith_generates_the_right_expression_for_the_iendswith_week_day_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__week_day__iendswith=F('field2'))

        actual = field1.week_day.iendswith(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_search_generates_the_right_expression_for_the_search_week_day_lookup(self):
        sut = self.system_under_test

        expected = Q(field__week_day__search=sentinel.VALUE)

        actual = sut.week_day.search(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_search_generates_the_right_expression_for_the_search_week_day_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__week_day__search=F('field2'))

        actual = field1.week_day.search(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_regex_generates_the_right_expression_for_the_regex_week_day_lookup(self):
        sut = self.system_under_test

        expected = Q(field__week_day__regex=sentinel.VALUE)

        actual = sut.week_day.regex(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_regex_generates_the_right_expression_for_the_regex_week_day_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__week_day__regex=F('field2'))

        actual = field1.week_day.regex(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iregex_generates_the_right_expression_for_the_iregex_week_day_lookup(self):
        sut = self.system_under_test

        expected = Q(field__week_day__iregex=sentinel.VALUE)

        actual = sut.week_day.iregex(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iregex_generates_the_right_expression_for_the_iregex_week_day_lookup_when_comparing_to_a_field(self):
        field1 = DateNaturalQueryDescriptor('field1')
        field2 = DateNaturalQueryDescriptor('field2')

        expected = Q(field1__week_day__iregex=F('field2'))

        actual = field1.week_day.iregex(field2)

        self.assertEqual(actual, expected)