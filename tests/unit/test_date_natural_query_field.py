from django.test import SimpleTestCase

from natural_query.fields import DateNaturalQueryField
from natural_query.query import DatePartNaturalQueryDescriptor
from tests.common.support.models import TestModel


class NaturalQueryFieldTestCase(SimpleTestCase):
    def test_a_date_query_descriptor_is_added_to_the_model(self):
        try:
            _ = TestModel.created_at_date
        except AttributeError as e:
            self.fail('TestModel has no attribute named created_at_date.\n%s' % e.message)

    def test_a_date_query_descriptor_has_the_year_attribute(self):
        try:
            _ = TestModel.created_at_date.year
        except AttributeError as e:
            self.fail('TestModel has no attribute named created_at_date.\n%s' % e.message)

    def test_a_date_query_descriptor_year_attribute_is_a_date_part_query_descriptor(self):
        actual = TestModel.created_at_date.year

        self.assertIsInstance(actual, DatePartNaturalQueryDescriptor)

    def test_a_date_query_descriptor_year_attribute_points_at_the_year_date_part_of_the_value(self):
        actual = TestModel.created_at_date.year.date_part

        self.assertEqual(actual, 'year')

    def test_a_date_query_descriptor_month_attribute_points_at_the_month_date_part_of_the_value(self):
        actual = TestModel.created_at_date.month.date_part

        self.assertEqual(actual, 'month')

    def test_a_date_query_descriptor_day_attribute_points_at_the_day_date_part_of_the_value(self):
        actual = TestModel.created_at_date.day.date_part

        self.assertEqual(actual, 'day')

    def test_a_date_query_descriptor_week_day_attribute_points_at_the_week_day_date_part_of_the_value(self):
        actual = TestModel.created_at_date.week_day.date_part

        self.assertEqual(actual, 'week_day')
