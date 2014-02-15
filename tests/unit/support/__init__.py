#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db.models import Q, F
from mock import patch


def q_fake_eq(instance, other):
    if isinstance(other, tuple):
        return instance.children == other

    return instance.children == other.children and instance.connector == other.connector and instance.negated == other.negated


def f_fake_eq(instance, other):
    return instance.name == other.name


def patch_q_objects_equality():
    patch.object(Q, '__eq__', new=q_fake_eq).start()


def patch_f_objects_equality():
    patch.object(F, '__eq__', new=f_fake_eq).start()