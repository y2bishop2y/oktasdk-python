import logging
import os
import unittest

from okta.AuthClient import AuthClient




class SessionsClientTest(unittest.TestCase):

    def setUp(self):
        self.client = AuthClient(os.environ.get('OKTA_TEST_URL'), os.environ.get('OKTA_TEST_KEY'))
        self.username = os.environ.get('OKTA_TEST_ADMIN_NAME')
        self.password = os.environ.get('OKTA_TEST_ADMIN_PASSWORD')

    def test_simple_auth(self):

        logging.info("HEREHERHE")
