from django.test import SimpleTestCase

from natural_query.fields import DateNaturalQueryField
from natural_query.query import DatePartNaturalQueryDescriptor
from tests.common.support.models import TestModel


class NaturalQueryFieldTestCase(SimpleTestCase):
    def setUp(self):
        del TestModel.created_at_date

    def test_a_date_query_descriptor_is_added_to_the_model(self):
        sut = DateNaturalQueryField(name='created_at_date')

        sut.contribute_to_class(TestModel, 'created_at_date')

        try:
            _ = TestModel.created_at_date
        except AttributeError:
            self.fail('TestModel has no attribute named foo')

    def test_a_date_query_descriptor_has_the_year_attribute(self):
        sut = DateNaturalQueryField(name='created_at_date')

        sut.contribute_to_class(TestModel, 'created_at_date')

        try:
            _ = TestModel.created_at_date.year
        except AttributeError:
            self.fail('TestModel has no attribute named foo')

    def test_a_date_query_descriptor_year_attribute_is_a_date_part_query_descriptor(self):
        sut = DateNaturalQueryField(name='created_at_date')

        sut.contribute_to_class(TestModel, 'created_at_date')

        actual = TestModel.created_at_date.year

        self.assertIsInstance(actual, DatePartNaturalQueryDescriptor)

    def test_a_date_query_descriptor_year_attribute_points_at_the_year_date_part_of_the_value(self):
        sut = DateNaturalQueryField(name='created_at_date')

        sut.contribute_to_class(TestModel, 'created_at_date')

        actual = TestModel.created_at_date.year.date_part

        self.assertEqual(actual, 'year')

    def test_a_date_query_descriptor_month_attribute_points_at_the_month_date_part_of_the_value(self):
        sut = DateNaturalQueryField(name='created_at_date')

        sut.contribute_to_class(TestModel, 'created_at_date')

        actual = TestModel.created_at_date.month.date_part

        self.assertEqual(actual, 'month')

    def test_a_date_query_descriptor_day_attribute_points_at_the_day_date_part_of_the_value(self):
        sut = DateNaturalQueryField(name='created_at_date')

        sut.contribute_to_class(TestModel, 'created_at_date')

        actual = TestModel.created_at_date.day.date_part

        self.assertEqual(actual, 'day')

    def test_a_date_query_descriptor_week_day_attribute_points_at_the_week_day_date_part_of_the_value(self):
        sut = DateNaturalQueryField(name='created_at_date')

        sut.contribute_to_class(TestModel, 'created_at_date')

        actual = TestModel.created_at_date.week_day.date_part

        self.assertEqual(actual, 'week_day')
