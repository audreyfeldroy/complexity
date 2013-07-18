#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
complexity.exceptions
---------------------

Complexity-specific exceptions.    
"""

class ComplexityException(Exception):
    """
    Base exception class; all Complexity-specific exceptions should subclass this
    """
    
class MissingTemplateDirException(ComplexityException):
    """
    Raised when a project is missing a templates/ subdirectory.
    """

class NonHTMLFileException(ComplexityException):
    """
    Raised when a project's templates/ directory contains a non-HTML file.
    """
