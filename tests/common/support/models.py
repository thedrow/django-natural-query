#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db.models import Model, IntegerField, DateTimeField


class TestModel(Model):
    foo = IntegerField(null=True)
    bar = IntegerField(default=1)
    created_at = DateTimeField(auto_now=True)

    def __repr__(self):
        return '<TestModel (#%d): foo=%d>' % (self.pk, self.foo)