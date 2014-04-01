#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db.models import F
from django.db.models.expressions import ExpressionNode
from mock import patch


def assertQObjectsEqual(first, second, msg=None):
    if not msg:
        msg = '%s is not the same as %s' % (first, second)

    assert _compare_children(first,
                             second) and first.connector == second.connector and first.negated == second.negated, msg


def _compare_children(first, second):
    with patch.object(F, '__eq__', new=_compare_f_objects), patch.object(ExpressionNode, '__eq__',
                                                                         new=_compare_expression_nodes):
        return first.children == second.children


def _compare_f_objects(s, other):
    return s.name == other.name if isinstance(other, F) else True


def _compare_expression_nodes(s, other):
    return s.connector == other.connector and s.children == other.children and s.negated == other.negated