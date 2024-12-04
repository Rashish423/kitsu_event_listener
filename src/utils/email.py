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
#       File        :   email.py
#       Author      :   Ashish Rana
#
#       Created On  :   11:58 AM, 4-Dec-2024
#       Created For :   Kitsu Event Listener
#       IDE used    :   PyCharm
#
# =============================================================================

"""Sends email notifications for events such as shot creation in the
   Kitsu platform.

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
import smtplib
import logging

# Custom Imports
from configs import Config

# Logger Configuration
logger = logging.getLogger('kitsu-event-listener')
logging.basicConfig(level=logging.INFO)


def send(data):
    """Public function to send an email notification for shot creation.

    Args:
        data (dict): A dictionary containing details about the shot.
            Expected keys include:
            - name: Name of the shot.
            - project_name: Name of the project.
            - episode_name: Name of the episode.
            - sequence_name: Name of the sequence.

    Returns:
        None
    """
    try:
        _send(data)
    except Exception as e:
        logger.warning(f'Failed to send email: {e}')


def _send(data):
    """Private function to handle the email sending logic.

    Args:
        data (dict): Shot details used to construct the email content.

    Returns:
        None
    """
    sender = Config.SENDER_EMAIL
    recipient = Config.RECIPIENT_EMAIL
    subject = f"Shot Created: {data.get('name')}"
    body = f"""
            A new shot has been created!

            Details:
            - Project: {data.get('project_name')}
            - Episode: {data.get('episode_name')}
            - Sequence: {data.get('sequence_name')}
            - Shot Name: {data.get('name')}

            Please log in to the Kitsu to review the updates.
            """
    app_password = Config.GMAIL_APP_KEY

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, app_password)
    server.sendmail(sender, recipient, f'Subject:{subject}\n\n{body}')
    logger.info(f'Email sent to {recipient}')


if __name__ == "__main__":
    pass
