from unittest import expectedFailure

from django.db.models import Q, Field, F
from django.test import SimpleTestCase
from mock import sentinel

from natural_query.query import NaturalQueryDescriptor
from tests.unit.support import assertQObjectsEqual


class NaturalQueryDescriptorTestCase(SimpleTestCase):
    def setUp(self):
        self.addTypeEqualityFunc(Q, assertQObjectsEqual)

    @property
    def system_under_test(self):
        sut = NaturalQueryDescriptor('field')

        return sut

    @property
    def field(self):
        return NaturalQueryDescriptor(name=sentinel.FIELD_NAME)

    def test_equals_operator_generates_the_right_expression_for_the_exact_lookup(self):
        sut = self.system_under_test
        expected = Q(field__exact=sentinel.VALUE)

        actual = sut == sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_concated_equals_operator_generates_the_right_expression_for_the_exact_lookup(self):
        sut = self.system_under_test
        expected = Q(field__exact=sentinel.VALUE)

        actual = sentinel.VALUE == sut == sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_equals_operator_generates_the_right_expression_for_the_exact_lookup_when_comparing_to_another_field(self):
        sut = self.system_under_test
        expected = Q(field__exact=F(sentinel.FIELD_NAME))

        actual = sut == self.field

        self.assertEqual(actual, expected)

    def test_greater_than_operator_generates_the_right_expression_for_the_gt_lookup(self):
        sut = self.system_under_test
        expected = Q(field__gt=sentinel.VALUE)

        actual = sut > sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_greater_than_operator_generates_the_right_expression_for_the_gt_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__gt=F(sentinel.FIELD_NAME))

        actual = sut > self.field

        self.assertEqual(actual, expected)

    def test_greater_than_or_equal_operator_generates_the_right_expression_for_the_gte_lookup(self):
        sut = self.system_under_test
        expected = Q(field__gte=sentinel.VALUE)

        actual = sut >= sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_greater_than_or_equal_operator_generates_the_right_expression_for_the_gte_lookup_when_comparing_to_another_field(

            self):
        sut = self.system_under_test
        expected = Q(field__gte=F(sentinel.FIELD_NAME))

        actual = sut >= self.field

        self.assertEqual(actual, expected)

    def test_less_than_operator_generates_the_right_expression_for_the_lt_lookup(self):
        sut = self.system_under_test
        expected = Q(field__lt=sentinel.VALUE)

        actual = sut < sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_less_than_operator_generates_the_right_expression_for_the_lt_lookup_when_comparing_to_another_field(self):
        sut = self.system_under_test
        expected = Q(field__lt=F(sentinel.FIELD_NAME))

        actual = sut < self.field

        self.assertEqual(actual, expected)

    def test_less_than_or_equal_operator_generates_the_right_expression_for_the_lte_lookup(self):
        sut = self.system_under_test
        expected = Q(field__lte=sentinel.VALUE)

        actual = sut <= sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_less_than_or_equal_operator_generates_the_right_expression_for_the_lte_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = Q(field__lte=F(sentinel.FIELD_NAME))

        actual = sut <= self.field

        self.assertEqual(actual, expected)

    def test_not_equal_operator_generates_the_right_negated_expression_for_the_exact_lookup(self):
        sut = self.system_under_test
        expected = ~Q(field__exact=sentinel.VALUE)

        actual = sut != sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_not_equal_operator_generates_the_right_negated_expression_for_the_exact_lookup_when_comparing_to_another_field(
            self):
        sut = self.system_under_test
        expected = ~Q(field__exact=F(sentinel.FIELD_NAME))

        actual = sut != self.field

        self.assertEqual(actual, expected)

    def test_concated_gte_operator_generates_the_right_expression_for_the_greater_than_or_equal_lookup(self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__gte=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE <= sut >= sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    def test_concated_gt_operator_generates_the_right_expression_for_the_greater_than_lookup(self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__gt=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE < sut > sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    def test_concated_gte_and_gt_operator_generates_the_right_expression_for_the_greater_than_lookup(self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__gt=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE <= sut > sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    def test_concated_gt_and_gte_operator_generates_the_right_expression_for_the_greater_than_or_equal_lookup(self):
        """
        This should generate an expression that picks the lower value for comparison.
        """
        sut = self.system_under_test
        expected = Q(field__gte=sentinel.LOWER_VALUE)

        actual = sentinel.HIGHER_VALUE < sut >= sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    def test_negating_generates_the_right_expression_for_the_not_lookup(self):
        sut = self.system_under_test
        expected = ~Q('field')

        actual = ~sut

        self.assertEqual(actual, expected)

    def test_can_and_expressions_when_braces_are_present(self):
        field1 = NaturalQueryDescriptor('field1')
        field2 = NaturalQueryDescriptor('field2')

        expected = Q(field1__exact=sentinel.VALUE1, field2__exact=sentinel.VALUE2)

        actual = (field1 == sentinel.VALUE1) & (field2 == sentinel.VALUE2)

        self.assertEqual(actual, expected)

    def test_can_or_expressions_when_braces_are_present(self):
        field1 = NaturalQueryDescriptor('field1')
        field2 = NaturalQueryDescriptor('field2')

        expected = Q(field1__exact=sentinel.VALUE1) | Q(field2__exact=sentinel.VALUE2)

        actual = (field1 == sentinel.VALUE1) | (field2 == sentinel.VALUE2)

        self.assertEqual(actual, expected)

    def test_can_add_to_field_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__exact=F('field') + sentinel.VALUE)

        actual = sut == sut + sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_substract_from_field_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__exact=F('field') - sentinel.VALUE)

        actual = sut == sut - sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_multiply_field_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__exact=F('field') * sentinel.VALUE)

        actual = sut == sut * sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_divide_field_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__exact=F('field') / sentinel.VALUE)

        actual = sut == sut / sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_raise_to_power_field_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__exact=pow(F('field'), sentinel.VALUE))

        actual = sut == pow(F('field'), sentinel.VALUE)

        self.assertEqual(actual, expected)

    def test_can_mod_field_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__exact=F('field') % sentinel.VALUE)

        actual = sut == sut % sentinel.VALUE

        self.assertEqual(actual, expected)

    def test_can_add_value_to_field_and_compare(self):
        sut = self.system_under_test

        # For some reason this test fails with a sentinel. I used a real value instead.
        expected = Q(field__exact=1 + F('field'))

        actual = sut == 1 + sut

        self.assertEqual(actual, expected)

    def test_can_substract_value_from_field_and_compare(self):
        sut = self.system_under_test
        expected = Q(field__exact=sentinel.VALUE - F('field'))

        actual = sut == sentinel.VALUE - sut

        self.assertEqual(actual, expected)

    def test_iexact_generates_the_right_expression_for_the_iexact_lookup(self):
        sut = self.system_under_test

        expected = Q(field__iexact=sentinel.VALUE)

        actual = sut.iexact(sentinel.VALUE)

        self.assertEqual(actual, expected)

    def test_iexact_generates_the_right_expression_for_the_iexact_lookup_when_comparing_to_a_field(self):
        field1 = NaturalQueryDescriptor('field1')
        field2 = NaturalQueryDescriptor('field2')

        expected = Q(field1__iexact=F('field2'))

        actual = field1.iexact(field2)

        self.assertEqual(actual, expected)

    def test_contains_generates_the_right_expression_for_the_contains_lookup(self):
        sut = self.system_under_test

        expected = Q(field__contains=sentinel.VALUE)

        actual = sut.contains(sentinel.VALUE)

        self.assertEqual(actual, expected)

    def test_contains_generates_the_right_expression_for_the_contains_lookup_when_comparing_to_a_field(self):
        field1 = NaturalQueryDescriptor('field1')
        field2 = NaturalQueryDescriptor('field2')

        expected = Q(field1__contains=F('field2'))

        actual = field1.contains(field2)

        self.assertEqual(actual, expected)

    def test_icontains_generates_the_right_expression_for_the_icontains_lookup(self):
        sut = self.system_under_test

        expected = Q(field__icontains=sentinel.VALUE)

        actual = sut.icontains(sentinel.VALUE)

        self.assertEqual(actual, expected)

    def test_icontains_generates_the_right_expression_for_the_icontains_lookup_when_comparing_to_a_field(self):
        field1 = NaturalQueryDescriptor('field1')
        field2 = NaturalQueryDescriptor('field2')

        expected = Q(field1__icontains=F('field2'))

        actual = field1.icontains(field2)

        self.assertEqual(actual, expected)

    def test_startswith_generates_the_right_expression_for_the_startswith_lookup(self):
        sut = self.system_under_test

        expected = Q(field__startswith=sentinel.VALUE)

        actual = sut.startswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    def test_startswith_generates_the_right_expression_for_the_startswith_lookup_when_comparing_to_a_field(self):
        field1 = NaturalQueryDescriptor('field1')
        field2 = NaturalQueryDescriptor('field2')

        expected = Q(field1__startswith=F('field2'))

        actual = field1.startswith(field2)

        self.assertEqual(actual, expected)

    def test_istartswith_generates_the_right_expression_for_the_istartswith_lookup(self):
        sut = self.system_under_test

        expected = Q(field__istartswith=sentinel.VALUE)

        actual = sut.istartswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    def test_istartswith_generates_the_right_expression_for_the_istartswith_lookup_when_comparing_to_a_field(self):
        field1 = NaturalQueryDescriptor('field1')
        field2 = NaturalQueryDescriptor('field2')

        expected = Q(field1__istartswith=F('field2'))

        actual = field1.istartswith(field2)

        self.assertEqual(actual, expected)

    def test_endswith_generates_the_right_expression_for_the_endswith_lookup(self):
        sut = self.system_under_test

        expected = Q(field__endswith=sentinel.VALUE)

        actual = sut.endswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    def test_endswith_generates_the_right_expression_for_the_endswith_lookup_when_comparing_to_a_field(self):
        field1 = NaturalQueryDescriptor('field1')
        field2 = NaturalQueryDescriptor('field2')

        expected = Q(field1__endswith=F('field2'))

        actual = field1.endswith(field2)

        self.assertEqual(actual, expected)

    def test_iendswith_generates_the_right_expression_for_the_iendswith_lookup(self):
        sut = self.system_under_test

        expected = Q(field__iendswith=sentinel.VALUE)

        actual = sut.iendswith(sentinel.VALUE)

        self.assertEqual(actual, expected)

    def test_iendswith_generates_the_right_expression_for_the_iendswith_lookup_when_comparing_to_a_field(self):
        field1 = NaturalQueryDescriptor('field1')
        field2 = NaturalQueryDescriptor('field2')

        expected = Q(field1__iendswith=F('field2'))

        actual = field1.iendswith(field2)

        self.assertEqual(actual, expected)

    def test_search_generates_the_right_expression_for_the_search_lookup(self):
        sut = self.system_under_test

        expected = Q(field__search=sentinel.VALUE)

        actual = sut.search(sentinel.VALUE)

        self.assertEqual(actual, expected)

    def test_search_generates_the_right_expression_for_the_search_lookup_when_comparing_to_a_field(self):
        field1 = NaturalQueryDescriptor('field1')
        field2 = NaturalQueryDescriptor('field2')

        expected = Q(field1__search=F('field2'))

        actual = field1.search(field2)

        self.assertEqual(actual, expected)

    def test_regex_generates_the_right_expression_for_the_regex_lookup(self):
        sut = self.system_under_test

        expected = Q(field__regex=sentinel.VALUE)

        actual = sut.regex(sentinel.VALUE)

        self.assertEqual(actual, expected)

    def test_regex_generates_the_right_expression_for_the_regex_lookup_when_comparing_to_a_field(self):
        field1 = NaturalQueryDescriptor('field1')
        field2 = NaturalQueryDescriptor('field2')

        expected = Q(field1__regex=F('field2'))

        actual = field1.regex(field2)

        self.assertEqual(actual, expected)

    def test_iregex_generates_the_right_expression_for_the_iregex_lookup(self):
        sut = self.system_under_test

        expected = Q(field__iregex=sentinel.VALUE)

        actual = sut.iregex(sentinel.VALUE)

        self.assertEqual(actual, expected)

    def test_iregex_generates_the_right_expression_for_the_iregex_lookup_when_comparing_to_a_field(self):
        field1 = NaturalQueryDescriptor('field1')
        field2 = NaturalQueryDescriptor('field2')

        expected = Q(field1__iregex=F('field2'))

        actual = field1.iregex(field2)

        self.assertEqual(actual, expected)

    def test_in_generates_the_right_expression_for_the_in_lookup(self):
        sut = self.system_under_test

        expected = Q(field__in=(sentinel.VALUE1, sentinel.VALUE2))

        actual = sut.in_values(sentinel.VALUE1, sentinel.VALUE2)

        self.assertEqual(actual, expected)

    def test_in_generates_the_right_expression_for_the_in_lookup_when_comparing_to_a_field(self):
        sut = self.system_under_test
        field2 = NaturalQueryDescriptor('field2')

        expected = Q(field__in=(sentinel.VALUE, F('field2')))

        actual = sut.in_values(sentinel.VALUE, field2)

        self.assertEqual(actual, expected)

    def test_between_generates_the_right_expression_for_the_range_lookup(self):
        sut = self.system_under_test

        expected = Q(field__range=(sentinel.VALUE1, sentinel.VALUE2))

        actual = sut.between(sentinel.VALUE1, sentinel.VALUE2)

        self.assertEqual(actual, expected)

    def test_between_generates_the_right_expression_for_the_range_lookup_when_comparing_to_a_field(self):
        sut = self.system_under_test
        field2 = NaturalQueryDescriptor('field2')

        expected = Q(field__range=(sentinel.VALUE, F('field2')))

        actual = sut.between(sentinel.VALUE, field2)

        self.assertEqual(actual, expected)


class NaturalQueryDescriptorUnsupportedOperationsTestCase(SimpleTestCase):
    @property
    def system_under_test(self):
        sut = NaturalQueryDescriptor('field')

        return sut

    @property
    def field(self):
        return Field(name=sentinel.FIELD_NAME)

    @expectedFailure
    def test_concated_equals_operator_generates_the_wrong_expression_for_the_exact_lookup(self):
        sut = self.system_under_test
        expected = Q(field__exact=sentinel.VALUE)

        actual = sut == sentinel.VALUE == sentinel.VALUE

        self.assertEqual(actual, expected)

    @expectedFailure
    def test_concated_greater_than_or_equals_operator_generates_the_wrong_expression_for_the_range_lookup(self):
        sut = self.system_under_test
        expected = Q(field__range=[sentinel.LOWER_VALUE, sentinel.HIGHER_VALUE])

        actual = sentinel.HIGHER_VALUE >= sut >= sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    @expectedFailure
    def test_concated_greater_than_operator_generates_the_wrong_expression_for_the_lt_and_gt_lookup(self):
        sut = self.system_under_test
        expected = Q(field_gt=sentinel.LOWER_VALUE, field_lt=sentinel.HIGHER_VALUE)

        actual = sentinel.HIGHER_VALUE > sut > sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    @expectedFailure
    def test_concated_greater_than_or_equal_and_greater_than_operator_generates_the_wrong_expression_for_the_lt_and_gte_lookup(
            self):
        sut = self.system_under_test
        expected = Q(field_gt=sentinel.LOWER_VALUE, field_lte=sentinel.HIGHER_VALUE)

        actual = sentinel.HIGHER_VALUE >= sut > sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    @expectedFailure
    def test_concated_greater_than_and_greater_than_or_equal_operator_generates_the_wrong_expression_for_the_lt_and_gte_lookup(
            self):
        sut = self.system_under_test
        expected = Q(field_gte=sentinel.LOWER_VALUE, field_lt=sentinel.HIGHER_VALUE)

        actual = sentinel.HIGHER_VALUE > sut >= sentinel.LOWER_VALUE

        self.assertEqual(actual, expected)

    @expectedFailure
    def test_concated_lower_than_or_equals_operator_generates_the_wrong_expression_for_the_range_lookup(self):
        sut = self.system_under_test
        expected = Q(field__range=[sentinel.LOWER_VALUE, sentinel.HIGHER_VALUE])

        actual = sentinel.LOWER_VALUE <= sut <= sentinel.HIGHER_VALUE

        self.assertEqual(actual, expected)

    @expectedFailure
    def test_concated_lower_than_operator_generates_the_wrong_expression_for_the_lt_and_gt_lookup(self):
        sut = self.system_under_test
        expected = Q(field_gt=sentinel.LOWER_VALUE, field_lt=sentinel.HIGHER_VALUE)

        actual = sentinel.LOWER_VALUE < sut < sentinel.HIGHER_VALUE

        self.assertEqual(actual, expected)

    @expectedFailure
    def test_concated_lower_than_or_equal_and_lower_than_operator_generates_the_wrong_expression_for_the_lt_and_gt_lookup(
            self):
        sut = self.system_under_test
        expected = Q(field_gte=sentinel.LOWER_VALUE, field_lt=sentinel.HIGHER_VALUE)

        actual = sentinel.LOWER_VALUE <= sut < sentinel.HIGHER_VALUE

        self.assertEqual(actual, expected)

    @expectedFailure
    def test_concated_lower_than_and_lower_than_or_equal_operator_generates_the_wrong_expression_for_the_lt_and_gt_lookup(
            self):
        sut = self.system_under_test
        expected = Q(field_gt=sentinel.LOWER_VALUE, field_lte=sentinel.HIGHER_VALUE)

        actual = sentinel.LOWER_VALUE < sut <= sentinel.HIGHER_VALUE

        self.assertEqual(actual, expected)

    @expectedFailure
    def test_cant_and_expressions_when_braces_are_not_present(self):
        field1 = NaturalQueryDescriptor('field1')
        field2 = NaturalQueryDescriptor('field2')

        expected = Q(field1__exact=sentinel.VALUE1, field2__exact=sentinel.VALUE2)

        actual = field1 == sentinel.VALUE1 & field2 == sentinel.VALUE2

        self.assertEqual(actual, expected)

    @expectedFailure
    def test_cant_or_expressions_when_braces_are_not_present(self):
        field1 = NaturalQueryDescriptor('field1')
        field2 = NaturalQueryDescriptor('field2')

        expected = Q(field1__exact=sentinel.VALUE1) | Q(field2__exact=sentinel.VALUE2)

        actual = field1 == sentinel.VALUE1 | field2 == sentinel.VALUE2

        self.assertEqual(actual, expected)