#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db.models import Model, IntegerField, DateTimeField, DateField, ForeignKey


class TestModel(Model):
    foo = IntegerField(null=True)
    bar = IntegerField(default=1)
    created_at_date = DateField(auto_now=True)
    created_at = DateTimeField(auto_now=True)
    test_model_2 = ForeignKey('TestModel2', null=True)

    def __repr__(self):
        return '<TestModel (#%d): foo=%d>' % (self.pk, self.foo)


class TestModel2(Model):
    pass
