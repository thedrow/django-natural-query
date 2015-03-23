#!/usr/bin/env python
# -*- coding: utf-8 -*-


def assertQObjectsEqual(first, second, msg=None):
    if not msg:
        msg = '%s is not the same as %s' % (first, second)

    are_expressions_exactly_equal = str(first) == str(second)

    are_expressions_equivalent = False
    if not are_expressions_exactly_equal:
        first.children = sorted(first.children, key=lambda c: c[0][0])
        second.children = sorted(second.children, key=lambda c: c[0][0])

        first_node = first.children[0][1]
        second_node = second.children[0][1]

        try:
            if first_node.connector == second_node.connector == '+':
                are_expressions_equivalent = str(first_node.rhs) == str(second_node.lhs) and str(first_node.lhs) == str(second_node.rhs)
        except AttributeError:
            pass

    assert (are_expressions_exactly_equal or are_expressions_equivalent) and first.connector == second.connector and first.negated == second.negated, msg