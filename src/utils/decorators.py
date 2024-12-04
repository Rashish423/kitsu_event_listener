#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
#
# Copyright:    (c) 2024 Ashish Rana.
#               All rights reserved.
#
#           The coded instructions, statements, computer programs, and/or
#           related material (collectively the "Data") in these files contain
#           unpublished information proprietary to Ashish Rana,
#           which is protected by applicable Copyright Laws.
#
#           Use of this software is subject to the terms of the License
#           Agreement provided at the time of installation or download,
#           or which otherwise accompanies this software in either electronic
#           or hard copy form.
#
# =============================================================================
# =============================================================================
#
# -*Meta Info*-
#
#       File        :   decorators.py
#       Author      :   Ashish Rana
#
#       Created On  :   12:47 PM, 4-Dec-2024
#       Created For :   Utility Decorators
#       IDE used    :   PyCharm
#
# =============================================================================

"""Provides utility decorators for enhancing functionality.

Examples:
    # Valid Examples If Any.

Attributes:
    # Module Level Attributes Here.

Notes:
    # Any Specific Note Over Here.

Todo:
    # Todo Stuff Over Here.

"""

# Built-in Imports
import threading
from functools import wraps


def run_in_thread(func):
    """Decorator to execute a function in a separate thread.

    This decorator allows a function to run asynchronously in its own thread,
    making it non-blocking for the main program execution.

    Args:
        func (callable): The function to be executed in a new thread.

    Returns:
        callable: The wrapped function that spawns a thread.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
        return thread

    return wrapper


if __name__ == "__main__":
    pass
