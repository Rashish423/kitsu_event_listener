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
#       File        :   listener.py
#       Author      :   Ashish Rana
#
#       Created On  :   11:50 AM, 4-Dec-2024
#       Created For :   Kitsu Event Listener
#       IDE used    :   PyCharm
#
# =============================================================================

"""Implements the Kitsu Event Listener for listening to and handling events
    in the Kitsu platform.

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
import logging

# Third-party Imports
import gazu

# Custom Imports
from configs import Config
from utils import email, decorators

# Logger Configuration
logger = logging.getLogger('kitsu-event-listener')


class Listener:
    """Class: Listener
    Handles the setup and execution of the Kitsu Event Listener.

    Attributes:
        _events (dict): Maps event types to their respective callback methods.
    """

    _events = {
        'shot:new': 'on_shot_created'
    }

    def __init__(self, **kw):
        """Initializes the Listener instance with the provided configuration."""
        self.host = kw.get('host') or Config.KITSU_HOST
        self.port = kw.get('port') or Config.KITSU_PORT
        self.username = kw.get('username') or Config.KITSU_USERNAME
        self.password = kw.get('password') or Config.KITSU_PASSWORD

    def setup_client(self):
        """Configures Gazu with the host and login credentials.

        This function sets up the Gazu API and event host URLs and logs in using
        the credentials specified in the configuration.

        Returns:
            None
        """
        gazu.set_host(f'http://{self.host}:{self.port}/api')
        gazu.set_event_host(f'http://{self.host}:{self.port}/')
        gazu.log_in(self.username, self.password)
        logger.info('Gazu client setup done successfully.')

    def initiate(self):
        """Starts the event listener and binds callbacks to events."""
        try:
            event_client = gazu.events.init()
            for event, callback in self._events.items():
                callback = getattr(self, callback, None)

                if not callable(callback):
                    logger.warning(f'Skipping setup of callback for {event}.')
                    continue

                gazu.events.add_listener(event_client, event, callback)

            logger.info(f'Listing from {self.host}:{self.port}.')
            gazu.events.run_client(event_client)
        except Exception as e:
            logger.error(f'Error during event listener initiation: {e}', exc_info=True)

    @decorators.run_in_thread
    def on_shot_created(self, data):
        """Handles the 'shot:new' event.

        Args:
            data (dict): Event data containing details about the created shot.

        This function fetches shot data and sends an email notification.
        """
        try:
            shot_data = gazu.shot.get_shot(data.get('shot_id'))
            email.send(shot_data)
            logger.info(f'Shot created: {data}')
        except Exception as e:
            logger.error(f'Error handling "shot:new" event: {e}', exc_info=True)

    def listen(self):
        """Sets up the client and initiates the event listener."""
        self.setup_client()
        self.initiate()


def main():
    """Entry point for the Listener."""
    instance = Listener()
    instance.listen()


if __name__ == '__main__':
    main()
