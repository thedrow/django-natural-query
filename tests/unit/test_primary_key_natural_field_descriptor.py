from django.test import SimpleTestCase
from mock import sentinel, patch

from natural_query.query import PrimaryKeyNaturalQueryDescriptor
from tests.common.support.models import TestModel


class NaturalQueryFieldTestCase(SimpleTestCase):
    def test_can_access_query_descriptor_from_model_type(self):
        self.assertIsInstance(TestModel.pk, PrimaryKeyNaturalQueryDescriptor)

    def test_can_access_primary_key_from_model_instance(self):
        sut = TestModel()

        with patch.object(TestModel, '_get_pk_val') as mocked_get_pk_val:
            _ = sut.pk

        mocked_get_pk_val.assert_called_once_with()

    def test_can_set_pk_from_model_instance(self):
        with patch.object(TestModel, '_set_pk_val') as mocked_set_pk_val:
            sut = TestModel()
            sut.pk = sentinel.PK

        mocked_set_pk_val.assert_called_once_with(sentinel.PK)