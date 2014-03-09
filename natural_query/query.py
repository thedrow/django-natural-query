from django.db.models import Field, F, Q


def _get_value_or_field(other):
    if isinstance(other, Field):
        other = F(other.name)
    return other


def create_query_object(constructed_lookup, other):
    return Q(**{constructed_lookup: other})


class NaturalQueryDescriptor(object):
    def __init__(self, name):
        self.name = name

    def transform_operator_to_query_object(self, lookup_type, other):
        other = _get_value_or_field(other)
        constructed_lookup = self.construct_lookup(lookup_type)
        return create_query_object(constructed_lookup, other)

    def construct_lookup(self, lookup_type):
        return '%s__%s' % (self.name, lookup_type)

    def __eq__(self, other):
        return self.transform_operator_to_query_object('exact', other)

    def __gt__(self, other):
        return self.transform_operator_to_query_object('gt', other)

    def __ge__(self, other):
        return self.transform_operator_to_query_object('gte', other)

    def __lt__(self, other):
        return self.transform_operator_to_query_object('lt', other)

    def __le__(self, other):
        return self.transform_operator_to_query_object('lte', other)

    def __ne__(self, other):
        return ~self.transform_operator_to_query_object('exact', other)

    def __invert__(self):
        return ~Q(self.name)

    def __add__(self, other):
        return F(self.name) + other

    def __sub__(self, other):
        return F(self.name) - other

    def __mul__(self, other):
        return F(self.name) * other

    def __div__(self, other):
        return F(self.name) / other

    def __radd__(self, other):
        return F(self.name) + other

    def __rsub__(self, other):
        return other - F(self.name)

    def __rmul__(self, other):
        return F(self.name) * other

    def __rdiv__(self, other):
        return other / F(self.name)

    def __pow__(self, power, modulo=None):
        return pow(F(self.name), power, modulo)

    def __mod__(self, other):
        return F(self.name) % other

    def __rmod__(self, other):
        return other % F(self.name)