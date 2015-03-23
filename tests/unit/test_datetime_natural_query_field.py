from django.test import SimpleTestCase

from natural_query.fields import DateTimeNaturalQueryField

from natural_query.query import DatePartNaturalQueryDescriptor
from tests.common.support.models import TestModel


class NaturalQueryFieldTestCase(SimpleTestCase):
    def test_a_datetime_query_descriptor_is_added_to_the_model(self):
        try:
            _ = TestModel.created_at
        except AttributeError as e:
            self.fail('TestModel has no attribute named created_at.\n%s' % e.message)

    def test_a_datetime_query_descriptor_has_the_year_attribute(self):
        try:
            _ = TestModel.created_at.year
        except AttributeError as e:
            self.fail('TestModel has no attribute named created_at.\n%s' % e.message)

    def test_a_datetime_query_descriptor_year_attribute_points_at_the_year_date_part_of_the_value(self):
        actual = TestModel.created_at.year.date_part

        self.assertEqual(actual, 'year')

    def test_a_datetime_query_descriptor_month_attribute_points_at_the_month_date_part_of_the_value(self):
        actual = TestModel.created_at.month.date_part

        self.assertEqual(actual, 'month')

    def test_a_datetime_query_descriptor_day_attribute_points_at_the_day_date_part_of_the_value(self):
        actual = TestModel.created_at.day.date_part

        self.assertEqual(actual, 'day')

    def test_a_datetime_query_descriptor_week_day_attribute_points_at_the_week_day_date_part_of_the_value(self):
        actual = TestModel.created_at.week_day.date_part

        self.assertEqual(actual, 'week_day')

    def test_a_datetime_query_descriptor_hour_attribute_points_at_the_hour_date_part_of_the_value(self):
        actual = TestModel.created_at.hour.date_part

        self.assertEqual(actual, 'hour')

    def test_a_datetime_query_descriptor_minute_attribute_points_at_the_minute_date_part_of_the_value(self):
        actual = TestModel.created_at.minute.date_part

        self.assertEqual(actual, 'minute')

    def test_a_datetime_query_descriptor_second_attribute_points_at_the_second_date_part_of_the_value(self):
        actual = TestModel.created_at.second.date_part

        self.assertEqual(actual, 'second')
