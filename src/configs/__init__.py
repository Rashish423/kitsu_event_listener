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
#       File        :   __init__.py
#       Author      :   Ashish Rana
#
#       Created On  :   12:31 PM, 4-Dec-2024
#       Created For :   Kitsu Event Listener
#       IDE used    :   PyCharm
#
# =============================================================================

"""Configuration class for managing application settings.

This module defines a `Config` class to manage the application's configuration
settings, including server and email credentials. It reads environment variables
when available, and provides default values when they are not set.

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
import os


class Config:
    """Configuration class for managing application settings.

    configurations for Kitsu server, Gmail credentials,
    and notification email settings.
    """

    # Kitsu server settings
    KITSU_HOST = os.getenv('KITSU_HOST', '127.0.0.1')
    KITSU_PORT = os.getenv('KITSU_PORT', '538')

    # Gmail app credentials for sending emails
    GMAIL_APP_KEY = os.getenv('GMAIL_APP_KEY', 'atyy qudq rqkl fypa')

    # Email address to send notifications
    SENDER_EMAIL = 'kitsutestmail@gmail.com'
    RECIPIENT_EMAIL = ['rashish423@gmail.com', 'ashishmkcl480@gmail.com']

    # User credentials for Kitsu
    KITSU_USERNAME = 'admin@example.com'
    KITSU_PASSWORD = 'mysecretpassword'
