====================
django-natural-query
====================

Natural queries using objects and operators for Django.

**Supported Django versions**: 1.7a2 and above

.. warning::
    This project is currently not production ready and uses the alpha version of Django 1.7.
    Once Django 1.7 is released this project will stabilize.

Overview
========

The Django query syntax is unnecessarily complicated and unpythonic. It uses underscores in order to specify operators.

If you are unfamiliar with the way Django works this syntax increases the steepness of the learning curve.
Even if you are familiar with Django query syntax, the syntax still is still a bit harder to understand and analyze.

This project allows you to write queries in a simpler way by using the normal python operators
like ``==``, ``>`` and ``<``.