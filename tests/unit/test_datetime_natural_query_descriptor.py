from unittest import skip

from django.db.models import Q, F
from mock import sentinel

from natural_query.query import DateTimeNaturalQueryDescriptor
from tests.unit.support import assertQObjectsEqual
from tests.unit.test_date_natural_query_descriptor import DateNaturalQueryDescriptorTestCase


class DateTimeNaturalQueryDescriptorTestCase(DateNaturalQueryDescriptorTestCase):
    def assertEqual(self, first, second, msg=None):
        if isinstance(first, Q) and isinstance(second, Q):
            return assertQObjectsEqual(first, second, msg=msg)

        return super(DateTimeNaturalQueryDescriptorTestCase, self).assertEqual(first, second, msg=msg)

    def setUp(self):
        self.addTypeEqualityFunc(Q, assertQObjectsEqual)

    @property
    def system_under_test(self):
        sut = DateTimeNaturalQueryDescriptor('field')

        return sut

    @property
    def field(self):
        return DateTimeNaturalQueryDescriptor(name='field2')

    def test_equals_operator_generates_the_right_expression_for_the_exact_hour_lookup(self):
        sut = self.system_under_test
        expected = Q(field__hour=sentinel.VALUE)

        actual = sut.hour == sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_concated_equals_operator_generates_the_right_expression_for_the_exact_hour_lookup(self):
        sut = self.system_under_test
        expected = Q(field__hour=sentinel.VALUE)

        actual = sentinel.VALUE == sut.hour == sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_equals_operator_generates_the_right_expression_for_the_exact_hour_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__hour=F('field2'))

        actual = sut.hour == self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_greater_than_operator_generates_the_right_expression_for_the_gt_hour_lookup(self):
        sut = self.system_under_test
        expected = Q(field__hour__gt=sentinel.VALUE)

        actual = sut.hour > sentinel.VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_greater_than_operator_generates_the_right_expression_for_the_gt_hour_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__hour__gt=F('field2'))

        actual = sut.hour > self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_greater_than_or_equal_operator_generates_the_right_expression_for_the_gte_hour_lookup(self):
        sut = self.system_under_test
        expected = Q(field__hour__gte=sentinel.VALUE)

        actual = sut.hour >= sentinel.VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_greater_than_or_equal_operator_generates_the_right_expression_for_the_gte_hour_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__hour__gte=F('field2'))

        actual = sut.hour >= self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_less_than_operator_generates_the_right_expression_for_the_lt_hour_lookup(self):
        sut = self.system_under_test
        expected = Q(field__hour__lt=sentinel.VALUE)

        actual = sut.hour < sentinel.VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_less_than_operator_generates_the_right_expression_for_the_lt_hour_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__hour__lt=F('field2'))

        actual = sut.hour < self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_less_than_or_equal_operator_generates_the_right_expression_for_the_lte_hour_lookup(self):
        sut = self.system_under_test
        expected = Q(field__hour__lte=sentinel.VALUE)

        actual = sut.hour <= sentinel.VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_less_than_or_equal_operator_generates_the_right_expression_for_the_lte_hour_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__hour__lte=F('field2'))

        actual = sut.hour <= self.field

        self.assertEqual(actual, expected)

    def test_not_equal_operator_generates_the_right_negated_expression_for_the_exact_hour_lookup(self):
        sut = self.system_under_test
        expected = ~Q(field__hour=sentinel.VALUE)

        actual = sut.hour != sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_not_equal_operator_generates_the_right_negated_expression_for_the_exact_hour_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = ~Q(field__hour=F('field2'))

        actual = sut.hour != self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_concated_gte_operator_generates_the_right_expression_for_the_greater_than_or_equal_hour_lookup(self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__hour__gte=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE <= sut.hour >= sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_concated_gt_operator_generates_the_right_expression_for_the_greater_than_hour_lookup(self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__hour__gt=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE < sut.hour > sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_concated_gte_and_gt_operator_generates_the_right_expression_for_the_greater_than_hour_lookup(self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__hour__gt=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE <= sut.hour > sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_concated_gt_and_gte_operator_generates_the_right_expression_for_the_greater_than_or_equal_hour_lookup(
            self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__hour__gte=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE < sut.hour >= sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    def test_can_and_expressions_referring_to_hour_when_braces_are_present(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__hour=sentinel.VALUE1, field2__hour=sentinel.VALUE2)

        actual = (field1.hour == sentinel.VALUE1) & (field2.hour == sentinel.VALUE2)

        self.assertEqual(actual, expected)

    def test_can_or_expressions_referring_to_hour_when_braces_are_present(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__hour=sentinel.VALUE1) | Q(field2__hour=sentinel.VALUE2)

        actual = (field1.hour == sentinel.VALUE1) | (field2.hour == sentinel.VALUE2)

        self.assertEqual(actual, expected)

    def test_can_add_to_field_hour_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__hour=F('field__hour') + sentinel.VALUE)

        actual = sut.hour == sut.hour + sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_substract_from_field_hour_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__hour=F('field__hour') - sentinel.VALUE)

        actual = sut.hour == sut.hour - sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_multiply_field_hour_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__hour=F('field__hour') * sentinel.VALUE)

        actual = sut.hour == sut.hour * sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_divide_field_hour_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__hour=F('field__hour') / sentinel.VALUE)

        actual = sut.hour == sut.hour / sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_raise_to_power_field_hour_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__hour=pow(F('field__hour'), sentinel.VALUE))

        actual = sut.hour == pow(F('field__hour'), sentinel.VALUE)

        self.assertEqual(actual, expected)

    def test_can_mod_field_hour_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__hour=F('field__hour') % sentinel.VALUE)

        actual = sut.hour == sut.hour % sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_add_value_to_field_hour_and_compare(self):
        sut = self.system_under_test

        # For some reason this test fails with a sentinel. I used a real value instead.
        expected = Q(field__hour=1 + F('field'))

        actual = sut.hour == 1 + sut

        self.assertEqual(actual, expected)

    def test_can_substract_value_from_field_hour_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__hour=sentinel.VALUE - F('field'))

        actual = sut.hour == sentinel.VALUE - sut

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iexact_generates_the_right_expression_for_the_iexact_hour_lookup(self):
        sut = self.system_under_test

        expected = Q(field__hour__iexact=sentinel.VALUE)

        actual = sut.hour.iexact(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iexact_generates_the_right_expression_for_the_iexact_hour_lookup_when_comparing_to_a_field(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__hour__iexact=F('field2'))

        actual = field1.hour.iexact(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_contains_generates_the_right_expression_for_the_contains_hour_lookup(self):
        sut = self.system_under_test

        expected = Q(field__hour__contains=sentinel.VALUE)

        actual = sut.hour.contains(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_contains_generates_the_right_expression_for_the_contains_hour_lookup_when_comparing_to_a_field(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__hour__contains=F('field2'))

        actual = field1.hour.contains(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_icontains_generates_the_right_expression_for_the_icontains_hour_lookup(self):
        sut = self.system_under_test

        expected = Q(field__hour__icontains=sentinel.VALUE)

        actual = sut.hour.icontains(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_icontains_generates_the_right_expression_for_the_icontains_hour_lookup_when_comparing_to_a_field(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__hour__icontains=F('field2'))

        actual = field1.hour.icontains(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_startswith_generates_the_right_expression_for_the_startswith_hour_lookup(self):
        sut = self.system_under_test

        expected = Q(field__hour__startswith=sentinel.VALUE)

        actual = sut.hour.startswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_startswith_generates_the_right_expression_for_the_startswith_hour_lookup_when_comparing_to_a_field(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__hour__startswith=F('field2'))

        actual = field1.hour.startswith(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_istartswith_generates_the_right_expression_for_the_istartswith_hour_lookup(self):
        sut = self.system_under_test

        expected = Q(field__hour__istartswith=sentinel.VALUE)

        actual = sut.hour.istartswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_istartswith_generates_the_right_expression_for_the_istartswith_hour_lookup_when_comparing_to_a_field(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__hour__istartswith=F('field2'))

        actual = field1.hour.istartswith(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_endswith_generates_the_right_expression_for_the_endswith_hour_lookup(self):
        sut = self.system_under_test

        expected = Q(field__hour__endswith=sentinel.VALUE)

        actual = sut.hour.endswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_endswith_generates_the_right_expression_for_the_endswith_hour_lookup_when_comparing_to_a_field(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__hour__endswith=F('field2'))

        actual = field1.hour.endswith(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iendswith_generates_the_right_expression_for_the_iendswith_hour_lookup(self):
        sut = self.system_under_test

        expected = Q(field__hour__iendswith=sentinel.VALUE)

        actual = sut.hour.iendswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iendswith_generates_the_right_expression_for_the_iendswith_hour_lookup_when_comparing_to_a_field(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__hour__iendswith=F('field2'))

        actual = field1.hour.iendswith(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_search_generates_the_right_expression_for_the_search_hour_lookup(self):
        sut = self.system_under_test

        expected = Q(field__hour__search=sentinel.VALUE)

        actual = sut.hour.search(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_search_generates_the_right_expression_for_the_search_hour_lookup_when_comparing_to_a_field(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__hour__search=F('field2'))

        actual = field1.hour.search(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_regex_generates_the_right_expression_for_the_regex_hour_lookup(self):
        sut = self.system_under_test

        expected = Q(field__hour__regex=sentinel.VALUE)

        actual = sut.hour.regex(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_regex_generates_the_right_expression_for_the_regex_hour_lookup_when_comparing_to_a_field(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__hour__regex=F('field2'))

        actual = field1.hour.regex(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iregex_generates_the_right_expression_for_the_iregex_hour_lookup(self):
        sut = self.system_under_test

        expected = Q(field__hour__iregex=sentinel.VALUE)

        actual = sut.hour.iregex(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iregex_generates_the_right_expression_for_the_iregex_hour_lookup_when_comparing_to_a_field(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__hour__iregex=F('field2'))

        actual = field1.hour.iregex(field2)

        self.assertEqual(actual, expected)

    def test_equals_operator_generates_the_right_expression_for_the_exact_minute_lookup(self):
        sut = self.system_under_test
        expected = Q(field__minute=sentinel.VALUE)

        actual = sut.minute == sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_concated_equals_operator_generates_the_right_expression_for_the_exact_minute_lookup(self):
        sut = self.system_under_test
        expected = Q(field__minute=sentinel.VALUE)

        actual = sentinel.VALUE == sut.minute == sentinel.VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_equals_operator_generates_the_right_expression_for_the_exact_minute_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__minute=F('field2'))

        actual = sut.minute == self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_greater_than_operator_generates_the_right_expression_for_the_gt_minute_lookup(self):
        sut = self.system_under_test
        expected = Q(field__minute__gt=sentinel.VALUE)

        actual = sut.minute > sentinel.VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_greater_than_operator_generates_the_right_expression_for_the_gt_minute_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__minute__gt=F('field2'))

        actual = sut.minute > self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_greater_than_or_equal_operator_generates_the_right_expression_for_the_gte_minute_lookup(self):
        sut = self.system_under_test
        expected = Q(field__minute__gte=sentinel.VALUE)

        actual = sut.minute >= sentinel.VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_greater_than_or_equal_operator_generates_the_right_expression_for_the_gte_minute_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__minute__gte=F('field2'))

        actual = sut.minute >= self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_less_than_operator_generates_the_right_expression_for_the_lt_minute_lookup(self):
        sut = self.system_under_test
        expected = Q(field__minute__lt=sentinel.VALUE)

        actual = sut.minute < sentinel.VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_less_than_operator_generates_the_right_expression_for_the_lt_minute_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__minute__lt=F('field2'))

        actual = sut.minute < self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_less_than_or_equal_operator_generates_the_right_expression_for_the_lte_minute_lookup(self):
        sut = self.system_under_test
        expected = Q(field__minute__lte=sentinel.VALUE)

        actual = sut.minute <= sentinel.VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_less_than_or_equal_operator_generates_the_right_expression_for_the_lte_minute_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__minute__lte=F('field2'))

        actual = sut.minute <= self.field

        self.assertEqual(actual, expected)

    def test_not_equal_operator_generates_the_right_negated_expression_for_the_exact_minute_lookup(self):
        sut = self.system_under_test
        expected = ~Q(field__minute=sentinel.VALUE)

        actual = sut.minute != sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_not_equal_operator_generates_the_right_negated_expression_for_the_exact_minute_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = ~Q(field__minute=F('field2'))

        actual = sut.minute != self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_concated_gte_operator_generates_the_right_expression_for_the_greater_than_or_equal_minute_lookup(self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__minute__gte=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE <= sut.minute >= sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_concated_gt_operator_generates_the_right_expression_for_the_greater_than_minute_lookup(self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__minute__gt=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE < sut.minute > sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_concated_gte_and_gt_operator_generates_the_right_expression_for_the_greater_than_minute_lookup(self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__minute__gt=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE <= sut.minute > sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_concated_gt_and_gte_operator_generates_the_right_expression_for_the_greater_than_or_equal_minute_lookup(
            self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__minute__gte=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE < sut.minute >= sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    def test_can_and_expressions_referring_to_minute_when_braces_are_present(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__minute=sentinel.VALUE1, field2__minute=sentinel.VALUE2)

        actual = (field1.minute == sentinel.VALUE1) & (field2.minute == sentinel.VALUE2)

        self.assertEqual(actual, expected)

    def test_can_or_expressions_referring_to_minute_when_braces_are_present(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__minute=sentinel.VALUE1) | Q(field2__minute=sentinel.VALUE2)

        actual = (field1.minute == sentinel.VALUE1) | (field2.minute == sentinel.VALUE2)

        self.assertEqual(actual, expected)

    def test_can_add_to_field_minute_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__minute=F('field__minute') + sentinel.VALUE)

        actual = sut.minute == sut.minute + sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_substract_from_field_minute_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__minute=F('field__minute') - sentinel.VALUE)

        actual = sut.minute == sut.minute - sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_multiply_field_minute_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__minute=F('field__minute') * sentinel.VALUE)

        actual = sut.minute == sut.minute * sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_divide_field_minute_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__minute=F('field__minute') / sentinel.VALUE)

        actual = sut.minute == sut.minute / sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_raise_to_power_field_minute_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__minute=pow(F('field__minute'), sentinel.VALUE))

        actual = sut.minute == pow(F('field__minute'), sentinel.VALUE)

        self.assertEqual(actual, expected)

    def test_can_mod_field_minute_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__minute=F('field__minute') % sentinel.VALUE)

        actual = sut.minute == sut.minute % sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_add_value_to_field_minute_and_compare(self):
        sut = self.system_under_test

        # For some reason this test fails with a sentinel. I used a real value instead.
        expected = Q(field__minute=1 + F('field'))

        actual = sut.minute == 1 + sut

        self.assertEqual(actual, expected)

    def test_can_substract_value_from_field_minute_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__minute=sentinel.VALUE - F('field'))

        actual = sut.minute == sentinel.VALUE - sut

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iexact_generates_the_right_expression_for_the_iexact_minute_lookup(self):
        sut = self.system_under_test

        expected = Q(field__minute__iexact=sentinel.VALUE)

        actual = sut.minute.iexact(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iexact_generates_the_right_expression_for_the_iexact_minute_lookup_when_comparing_to_a_field(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__minute__iexact=F('field2'))

        actual = field1.minute.iexact(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_contains_generates_the_right_expression_for_the_contains_minute_lookup(self):
        sut = self.system_under_test

        expected = Q(field__minute__contains=sentinel.VALUE)

        actual = sut.minute.contains(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_contains_generates_the_right_expression_for_the_contains_minute_lookup_when_comparing_to_a_field(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__minute__contains=F('field2'))

        actual = field1.minute.contains(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_icontains_generates_the_right_expression_for_the_icontains_minute_lookup(self):
        sut = self.system_under_test

        expected = Q(field__minute__icontains=sentinel.VALUE)

        actual = sut.minute.icontains(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_icontains_generates_the_right_expression_for_the_icontains_minute_lookup_when_comparing_to_a_field(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__minute__icontains=F('field2'))

        actual = field1.minute.icontains(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_startswith_generates_the_right_expression_for_the_startswith_minute_lookup(self):
        sut = self.system_under_test

        expected = Q(field__minute__startswith=sentinel.VALUE)

        actual = sut.minute.startswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_startswith_generates_the_right_expression_for_the_startswith_minute_lookup_when_comparing_to_a_field(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__minute__startswith=F('field2'))

        actual = field1.minute.startswith(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_istartswith_generates_the_right_expression_for_the_istartswith_minute_lookup(self):
        sut = self.system_under_test

        expected = Q(field__minute__istartswith=sentinel.VALUE)

        actual = sut.minute.istartswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_istartswith_generates_the_right_expression_for_the_istartswith_minute_lookup_when_comparing_to_a_field(
            self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__minute__istartswith=F('field2'))

        actual = field1.minute.istartswith(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_endswith_generates_the_right_expression_for_the_endswith_minute_lookup(self):
        sut = self.system_under_test

        expected = Q(field__minute__endswith=sentinel.VALUE)

        actual = sut.minute.endswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_endswith_generates_the_right_expression_for_the_endswith_minute_lookup_when_comparing_to_a_field(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__minute__endswith=F('field2'))

        actual = field1.minute.endswith(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iendswith_generates_the_right_expression_for_the_iendswith_minute_lookup(self):
        sut = self.system_under_test

        expected = Q(field__minute__iendswith=sentinel.VALUE)

        actual = sut.minute.iendswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iendswith_generates_the_right_expression_for_the_iendswith_minute_lookup_when_comparing_to_a_field(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__minute__iendswith=F('field2'))

        actual = field1.minute.iendswith(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_search_generates_the_right_expression_for_the_search_minute_lookup(self):
        sut = self.system_under_test

        expected = Q(field__minute__search=sentinel.VALUE)

        actual = sut.minute.search(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_search_generates_the_right_expression_for_the_search_minute_lookup_when_comparing_to_a_field(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__minute__search=F('field2'))

        actual = field1.minute.search(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_regex_generates_the_right_expression_for_the_regex_minute_lookup(self):
        sut = self.system_under_test

        expected = Q(field__minute__regex=sentinel.VALUE)

        actual = sut.minute.regex(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_regex_generates_the_right_expression_for_the_regex_minute_lookup_when_comparing_to_a_field(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__minute__regex=F('field2'))

        actual = field1.minute.regex(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iregex_generates_the_right_expression_for_the_iregex_minute_lookup(self):
        sut = self.system_under_test

        expected = Q(field__minute__iregex=sentinel.VALUE)

        actual = sut.minute.iregex(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iregex_generates_the_right_expression_for_the_iregex_minute_lookup_when_comparing_to_a_field(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__minute__iregex=F('field2'))

        actual = field1.minute.iregex(field2)

        self.assertEqual(actual, expected)

    def test_equals_operator_generates_the_right_expression_for_the_exact_second_lookup(self):
        sut = self.system_under_test
        expected = Q(field__second=sentinel.VALUE)

        actual = sut.second == sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_concated_equals_operator_generates_the_right_expression_for_the_exact_second_lookup(self):
        sut = self.system_under_test
        expected = Q(field__second=sentinel.VALUE)

        actual = sentinel.VALUE == sut.second == sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_equals_operator_generates_the_right_expression_for_the_exact_second_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__second=F('field2'))

        actual = sut.second == self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_greater_than_operator_generates_the_right_expression_for_the_gt_second_lookup(self):
        sut = self.system_under_test
        expected = Q(field__second__gt=sentinel.VALUE)

        actual = sut.second > sentinel.VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_greater_than_operator_generates_the_right_expression_for_the_gt_second_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__second__gt=F('field2'))

        actual = sut.second > self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_greater_than_or_equal_operator_generates_the_right_expression_for_the_gte_second_lookup(self):
        sut = self.system_under_test
        expected = Q(field__second__gte=sentinel.VALUE)

        actual = sut.second >= sentinel.VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_greater_than_or_equal_operator_generates_the_right_expression_for_the_gte_second_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__second__gte=F('field2'))

        actual = sut.second >= self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_less_than_operator_generates_the_right_expression_for_the_lt_second_lookup(self):
        sut = self.system_under_test
        expected = Q(field__second__lt=sentinel.VALUE)

        actual = sut.second < sentinel.VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_less_than_operator_generates_the_right_expression_for_the_lt_second_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__second__lt=F('field2'))

        actual = sut.second < self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_less_than_or_equal_operator_generates_the_right_expression_for_the_lte_second_lookup(self):
        sut = self.system_under_test
        expected = Q(field__second__lte=sentinel.VALUE)

        actual = sut.second <= sentinel.VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_less_than_or_equal_operator_generates_the_right_expression_for_the_lte_second_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__second__lte=F('field2'))

        actual = sut.second <= self.field

        self.assertEqual(actual, expected)

    def test_not_equal_operator_generates_the_right_negated_expression_for_the_exact_second_lookup(self):
        sut = self.system_under_test
        expected = ~Q(field__second=sentinel.VALUE)

        actual = sut.second != sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_not_equal_operator_generates_the_right_negated_expression_for_the_exact_second_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = ~Q(field__second=F('field2'))

        actual = sut.second != self.field

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_concated_gte_operator_generates_the_right_expression_for_the_greater_than_or_equal_second_lookup(self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__second__gte=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE <= sut.second >= sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_concated_gt_operator_generates_the_right_expression_for_the_greater_than_second_lookup(self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__second__gt=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE < sut.second > sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_concated_gte_and_gt_operator_generates_the_right_expression_for_the_greater_than_second_lookup(self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__second__gt=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE <= sut.second > sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_concated_gt_and_gte_operator_generates_the_right_expression_for_the_greater_than_or_equal_second_lookup(
            self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__second__gte=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE < sut.second >= sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    def test_can_and_expressions_referring_to_second_when_braces_are_present(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__second=sentinel.VALUE1, field2__second=sentinel.VALUE2)

        actual = (field1.second == sentinel.VALUE1) & (field2.second == sentinel.VALUE2)

        self.assertEqual(actual, expected)

    def test_can_or_expressions_referring_to_second_when_braces_are_present(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__second=sentinel.VALUE1) | Q(field2__second=sentinel.VALUE2)

        actual = (field1.second == sentinel.VALUE1) | (field2.second == sentinel.VALUE2)

        self.assertEqual(actual, expected)

    def test_can_add_to_field_second_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__second=F('field__second') + sentinel.VALUE)

        actual = sut.second == sut.second + sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_substract_from_field_second_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__second=F('field__second') - sentinel.VALUE)

        actual = sut.second == sut.second - sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_multiply_field_second_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__second=F('field__second') * sentinel.VALUE)

        actual = sut.second == sut.second * sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_divide_field_second_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__second=F('field__second') / sentinel.VALUE)

        actual = sut.second == sut.second / sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_raise_to_power_field_second_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__second=pow(F('field__second'), sentinel.VALUE))

        actual = sut.second == pow(F('field__second'), sentinel.VALUE)

        self.assertEqual(actual, expected)

    def test_can_mod_field_second_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__second=F('field__second') % sentinel.VALUE)

        actual = sut.second == sut.second % sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_add_value_to_field_second_and_compare(self):
        sut = self.system_under_test

        # For some reason this test fails with a sentinel. I used a real value instead.
        expected = Q(field__second=1 + F('field'))

        actual = sut.second == 1 + sut

        self.assertEqual(actual, expected)

    def test_can_substract_value_from_field_second_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__second=sentinel.VALUE - F('field'))

        actual = sut.second == sentinel.VALUE - sut

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iexact_generates_the_right_expression_for_the_iexact_second_lookup(self):
        sut = self.system_under_test

        expected = Q(field__second__iexact=sentinel.VALUE)

        actual = sut.second.iexact(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iexact_generates_the_right_expression_for_the_iexact_second_lookup_when_comparing_to_a_field(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__second__iexact=F('field2'))

        actual = field1.second.iexact(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_contains_generates_the_right_expression_for_the_contains_second_lookup(self):
        sut = self.system_under_test

        expected = Q(field__second__contains=sentinel.VALUE)

        actual = sut.second.contains(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_contains_generates_the_right_expression_for_the_contains_second_lookup_when_comparing_to_a_field(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__second__contains=F('field2'))

        actual = field1.second.contains(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_icontains_generates_the_right_expression_for_the_icontains_second_lookup(self):
        sut = self.system_under_test

        expected = Q(field__second__icontains=sentinel.VALUE)

        actual = sut.second.icontains(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_icontains_generates_the_right_expression_for_the_icontains_second_lookup_when_comparing_to_a_field(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__second__icontains=F('field2'))

        actual = field1.second.icontains(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_startswith_generates_the_right_expression_for_the_startswith_second_lookup(self):
        sut = self.system_under_test

        expected = Q(field__second__startswith=sentinel.VALUE)

        actual = sut.second.startswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_startswith_generates_the_right_expression_for_the_startswith_second_lookup_when_comparing_to_a_field(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__second__startswith=F('field2'))

        actual = field1.second.startswith(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_istartswith_generates_the_right_expression_for_the_istartswith_second_lookup(self):
        sut = self.system_under_test

        expected = Q(field__second__istartswith=sentinel.VALUE)

        actual = sut.second.istartswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_istartswith_generates_the_right_expression_for_the_istartswith_second_lookup_when_comparing_to_a_field(
            self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__second__istartswith=F('field2'))

        actual = field1.second.istartswith(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_endswith_generates_the_right_expression_for_the_endswith_second_lookup(self):
        sut = self.system_under_test

        expected = Q(field__second__endswith=sentinel.VALUE)

        actual = sut.second.endswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_endswith_generates_the_right_expression_for_the_endswith_second_lookup_when_comparing_to_a_field(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__second__endswith=F('field2'))

        actual = field1.second.endswith(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iendswith_generates_the_right_expression_for_the_iendswith_second_lookup(self):
        sut = self.system_under_test

        expected = Q(field__second__iendswith=sentinel.VALUE)

        actual = sut.second.iendswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iendswith_generates_the_right_expression_for_the_iendswith_second_lookup_when_comparing_to_a_field(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__second__iendswith=F('field2'))

        actual = field1.second.iendswith(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_search_generates_the_right_expression_for_the_search_second_lookup(self):
        sut = self.system_under_test

        expected = Q(field__second__search=sentinel.VALUE)

        actual = sut.second.search(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_search_generates_the_right_expression_for_the_search_second_lookup_when_comparing_to_a_field(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__second__search=F('field2'))

        actual = field1.second.search(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_regex_generates_the_right_expression_for_the_regex_second_lookup(self):
        sut = self.system_under_test

        expected = Q(field__second__regex=sentinel.VALUE)

        actual = sut.second.regex(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_regex_generates_the_right_expression_for_the_regex_second_lookup_when_comparing_to_a_field(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__second__regex=F('field2'))

        actual = field1.second.regex(field2)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iregex_generates_the_right_expression_for_the_iregex_second_lookup(self):
        sut = self.system_under_test

        expected = Q(field__second__iregex=sentinel.VALUE)

        actual = sut.second.iregex(sentinel.VALUE)

        self.assertEqual(actual, expected)

    @skip('Django does not support these type of queries yet')
    def test_iregex_generates_the_right_expression_for_the_iregex_second_lookup_when_comparing_to_a_field(self):
        field1 = DateTimeNaturalQueryDescriptor('field1')
        field2 = DateTimeNaturalQueryDescriptor('field2')

        expected = Q(field1__second__iregex=F('field2'))

        actual = field1.second.iregex(field2)

        self.assertEqual(actual, expected)

