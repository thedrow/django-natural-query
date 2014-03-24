from django.db.models import F
from django.db.models.expressions import ExpressionNode
from mock import patch


def _compare_expression_nodes(s, other):
    return s.connector == other.connector and sorted(s.children) == sorted(
        other.children) and s.negated == other.negated


def _compare_f_objects(s, other):
    return s.name == other.name if isinstance(other, F) else True


def _compare_children(first, second):
    with patch.object(F, '__eq__', new=_compare_f_objects), patch.object(ExpressionNode, '__eq__',
                                                                         new=_compare_expression_nodes):
        return sorted(first.children) == sorted(second.children)


def assertQObjectsEqual(first, second, msg=None):
    if not msg:
        msg = '%s is not the same as %s' % (first, second)

    assert _compare_children(first,
                             second) and first.connector == second.connector and first.negated == second.negated, msg