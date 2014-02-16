#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db.models import Model, IntegerField


class TestModel(Model):
    foo = IntegerField()

    def __repr__(self):
        return '<TestModel (#%d): foo=%d>' % (self.pk, self.foo)