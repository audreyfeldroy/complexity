#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
complexity.exceptions
---------------------

All exceptions used in the Complexity code base are defined here.
"""


class ComplexityException(Exception):
    """
    Base exception class. All Complexity-specific exceptions should subclass
    this class.
    """


class MissingTemplateDirException(ComplexityException):
    """
    Raised when a project is missing a templates/ subdirectory.
    """


class NonHTMLFileException(ComplexityException):
    """
    Raised when a project's templates/ directory contains a non-HTML file.
    """
