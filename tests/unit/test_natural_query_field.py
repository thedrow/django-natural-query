from django.test import SimpleTestCase

from natural_query.fields import NaturalQueryField, NaturalQueryField
from natural_query.query import NaturalQueryDescriptor
from tests.common.support.models import TestModel


# class NaturalQueryFieldTestCase(SimpleTestCase):
#     def test_a_query_descriptor_is_added_to_the_model(self):
#         sut = NaturalQueryField(name='foo')
#
#         del TestModel.foo
#
#         sut.contribute_to_class(TestModel, 'foo')
#
#         try:
#             _ = TestModel.foo
#         except AttributeError:
#             self.fail('TestModel has no attribute named foo')
#
#     def test_a_query_descriptor_is_not_added_to_the_model_when_a_class_attribute_already_exists(self):
#         sut = NaturalQueryField(name='clean')
#
#         sut.contribute_to_class(TestModel, 'clean')
#
#         self.assertNotIsInstance(TestModel.clean, NaturalQueryDescriptor)