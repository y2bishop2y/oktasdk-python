
import logging
import unittest


from okta.framework.Utils import Utils
from okta.models.user.User import User

FROM_DATA = """
{
  "id": "00u8yrgh4v0BId5y30h7",
  "status": "ACTIVE",
  "created": "2016-12-07T21:40:53.000Z",
  "activated": "2016-12-07T23:43:44.000Z",
  "statusChanged": "2016-12-07T23:43:44.000Z",
  "lastLogin": "2016-12-08T00:33:48.000Z",
  "lastUpdated": "2016-12-08T19:02:55.000Z",
  "passwordChanged": "2016-12-07T21:40:54.000Z",
  "profile": {
    "firstName": "BILLY",
    "lastName": "BOBBERS",
    "mobilePhone": null,
    "email": "emiliano+5@medlista.com",
    "secondEmail": null,
    "login": "emiliano+5@medlista.com",
    "associations": [
      "THISIS A TEST",
      "DOES THIS WORK"
    ],
    "karma_points": 10
  },
  "credentials": {
    "password": {},
    "provider": {
      "type": "OKTA",
      "name": "OKTA"
    }
  },
  "_links": {
    "suspend": {
      "href": "https://portaltest1.oktapreview.com/api/v1/users/00u8yrgh4v0BId5y30h7/lifecycle/suspend",
      "method": "POST"
    },
    "resetPassword": {
      "href": "https://portaltest1.oktapreview.com/api/v1/users/00u8yrgh4v0BId5y30h7/lifecycle/reset_password",
      "method": "POST"
    },
    "expirePassword": {
      "href": "https://portaltest1.oktapreview.com/api/v1/users/00u8yrgh4v0BId5y30h7/lifecycle/expire_password",
      "method": "POST"
    },
    "self": {
      "href": "https://portaltest1.oktapreview.com/api/v1/users/00u8yrgh4v0BId5y30h7"
    },
    "changeRecoveryQuestion": {
      "href": "https://portaltest1.oktapreview.com/api/v1/users/00u8yrgh4v0BId5y30h7/credentials/change_recovery_question",
      "method": "POST"
    },
    "deactivate": {
      "href": "https://portaltest1.oktapreview.com/api/v1/users/00u8yrgh4v0BId5y30h7/lifecycle/deactivate",
      "method": "POST"
    },
    "changePassword": {
      "href": "https://portaltest1.oktapreview.com/api/v1/users/00u8yrgh4v0BId5y30h7/credentials/change_password",
      "method": "POST"
    }
  }
}
"""


class TestUser(unittest.TestCase):


    def test_deserialzie(self):

        print("=========================")
        user = Utils.deserialize(from_data=FROM_DATA, to_class=User)

        self.assertIsNotNone(user)
        self.assertIsNotNone(user.profile.associations)

