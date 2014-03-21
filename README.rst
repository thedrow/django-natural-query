====================
django-natural-query
====================

.. image:: https://travis-ci.org/thedrow/django-natural-query.png?branch=master
    :target: https://travis-ci.org/thedrow/django-natural-query
    :alt: Build Status

.. image:: https://coveralls.io/repos/thedrow/django-natural-query/badge.png?branch=master
    :target: https://coveralls.io/r/thedrow/django-natural-query
    :alt: Coverage Status

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

Quickstart
==========

For this quickstart we'll use the User model provided by the Django auth module.

When you want to create a query that filters all users by their first name and last name you write:

.. code-block:: python

    User.objects.filter(first_name='Foo', last_name='Bar')

Or if you want to be a bit more explicit you can use Q objects:

.. code-block:: python

    User.objects.filter(Q(first_name='Foo') & Q(last_name='Bar'))

Using natural queries you can simply type:

.. code-block:: python

    User.objects.filter((User.first_name == 'Foo') & (User.last_name == 'Bar'))

These expressions evaluate to Q objects which in their turn are being used by Django.
