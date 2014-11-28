import json
import os
import unittest

from ua_parser import user_agent_parser
from .parsers import parse
from . import compat


class UserAgentsTest(unittest.TestCase):

    def test_user_agent_object_assignments(self):
        ua_dict = user_agent_parser.Parse(devices['iphone']['ua_string'])
        iphone_ua = devices['iphone']['user_agent']

        # Ensure browser attributes are assigned correctly
        self.assertEqual(iphone_ua.browser.family,
                         ua_dict['user_agent']['family'])
        self.assertEqual(
            iphone_ua.browser.version,
            (int(ua_dict['user_agent']['major']),
             int(ua_dict['user_agent']['minor']))
        )

        # Ensure os attributes are assigned correctly
        self.assertEqual(iphone_ua.os.family, ua_dict['os']['family'])
        self.assertEqual(
            iphone_ua.os.version,
            (int(ua_dict['os']['major']), int(ua_dict['os']['minor']))
        )

        # Ensure device attributes are assigned correctly
        self.assertEqual(iphone_ua.device.family,
                         ua_dict['device']['family'])

    def test_unicode_strings(self):
        try:
            # Python 2
            unicode_ua_str = unicode(devices['iphone']['user_agent'])
            self.assertEqual(unicode_ua_str,
                             u"iPhone / iOS 5.1 / Mobile Safari 5.1")
            self.assertTrue(isinstance(unicode_ua_str, unicode))
        except NameError:
            # Python 3
            unicode_ua_str = str(devices['iphone']['user_agent'])
            self.assertEqual(unicode_ua_str,
                             "iPhone / iOS 5.1 / Mobile Safari 5.1")


with open(os.path.join(os.path.dirname(__file__), 'devices.json')) as f:
    devices = json.load(f)


def test_wrapper(items):
    def test_func(self):
        attrs = ('is_bot', 'is_mobile',
                 'is_pc', 'is_tablet', 'is_touch_capable')
        for attr in attrs:
            self.assertEqual(
                getattr(items['user_agent'], attr), items[attr], msg=attr)
        # Temporarily commenting this out since UserAgent.device
        # may return different string depending ua-parser version
        # self.assertEqual(str(items['user_agent']), items['str'])
    return test_func

for device, items in compat.iteritems(devices):
    items['user_agent'] = parse(items['ua_string'])
    setattr(UserAgentsTest, 'test_' + device, test_wrapper(items))
