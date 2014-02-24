#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.test import SimpleTestCase

from tests.common.support.models import TestModel


class DjangoModelFieldsTestCase(SimpleTestCase):
    def test_can_access_field(self):
        fields = TestModel._meta.fields
        field_names = [field.name for field in fields]
        self.assertIn('foo', field_names)