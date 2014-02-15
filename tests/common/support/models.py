#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db.models import Model, IntegerField


class TestModel(Model):
    foo = IntegerField()