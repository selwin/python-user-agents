import unittest

from ua_parser import user_agent_parser
from .parsers import parse, UserAgent


iphone_ua_string = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'
ipad_ua_string = 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10'
galaxy_tab_ua_string = 'Mozilla/5.0 (Linux; U; Android 2.2; en-us; SCH-I800 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
galaxy_s3_ua_string = 'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
kindle_fire_ua_string = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-us; Silk/1.1.0-80) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16 Silk-Accelerated=true'
playbook_ua_string = 'Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.0.1; en-US) AppleWebKit/535.8+ (KHTML, like Gecko) Version/7.2.0.1 Safari/535.8+'
nexus_7_ua_string = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
windows_phone_ua_string = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; SAMSUNG; SGH-i917)'
blackberry_torch_ua_string = 'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; zh-TW) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.448 Mobile Safari/534.8+'
blackberry_bold_ua_string = 'BlackBerry9700/5.0.0.862 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/331 UNTRUSTED/1.0 3gpp-gba'
blackberry_bold_touch_ua_string = 'Mozilla/5.0 (BlackBerry; U; BlackBerry 9930; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.241 Mobile Safari/534.11+'
windows_rt_ua_string = 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; ARM; Trident/6.0)'
j2me_opera_ua_string = 'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (J2ME/22.478; U; en) Presto/2.5.25 Version/10.54'
ie_ua_string = 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'
ie_touch_ua_string = 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; Touch)'
mac_safari_ua_string = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2'
windows_ie_ua_string = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'
ubuntu_firefox_ua_string = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1'

iphone_ua = parse(iphone_ua_string)
ipad_ua = parse(ipad_ua_string)
galaxy_tab = parse(galaxy_tab_ua_string)
galaxy_s3_ua = parse(galaxy_s3_ua_string)
kindle_fire_ua = parse(kindle_fire_ua_string)
playbook_ua = parse(playbook_ua_string)
nexus_7_ua = parse(nexus_7_ua_string)
windows_phone_ua = parse(windows_phone_ua_string)
windows_rt_ua = parse(windows_rt_ua_string)
blackberry_torch_ua = parse(blackberry_torch_ua_string)
blackberry_bold_ua = parse(blackberry_bold_ua_string)
blackberry_bold_touch_ua = parse(blackberry_bold_touch_ua_string)
j2me_opera_ua = parse(j2me_opera_ua_string)
ie_ua = parse(ie_ua_string)
ie_touch_ua = parse(ie_touch_ua_string)
mac_safari_ua = parse(mac_safari_ua_string)
windows_ie_ua = parse(windows_ie_ua_string)
ubuntu_firefox_ua = parse(ubuntu_firefox_ua_string)


class UserAgentsTest(unittest.TestCase):

    def test_user_agent_object_assignments(self):
        ua_dict = user_agent_parser.Parse(iphone_ua_string)

        # Ensure browser attributes are assigned correctly
        self.assertEqual(iphone_ua.browser.family,
                         ua_dict['user_agent']['family'])
        self.assertEqual(
            iphone_ua.browser.version,
            (int(ua_dict['user_agent']['major']), int(ua_dict['user_agent']['minor']))
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

    def test_is_tablet_property(self):
        self.assertFalse(iphone_ua.is_tablet)
        self.assertFalse(galaxy_s3_ua.is_tablet)
        self.assertFalse(blackberry_torch_ua.is_tablet)
        self.assertFalse(blackberry_bold_ua.is_tablet)
        self.assertFalse(windows_phone_ua.is_tablet)
        self.assertFalse(ie_ua.is_tablet)
        self.assertFalse(ie_touch_ua.is_tablet)
        self.assertFalse(mac_safari_ua.is_tablet)
        self.assertFalse(windows_ie_ua.is_tablet)
        self.assertFalse(ubuntu_firefox_ua.is_tablet)
        self.assertFalse(j2me_opera_ua.is_tablet)
        self.assertTrue(windows_rt_ua.is_tablet)
        self.assertTrue(ipad_ua.is_tablet)
        self.assertTrue(playbook_ua.is_tablet)
        self.assertTrue(kindle_fire_ua.is_tablet)
        self.assertTrue(nexus_7_ua.is_tablet)

    def test_is_mobile_property(self):
        self.assertTrue(iphone_ua.is_mobile)
        self.assertTrue(galaxy_s3_ua.is_mobile)
        self.assertTrue(blackberry_torch_ua.is_mobile)
        self.assertTrue(blackberry_bold_ua.is_mobile)
        self.assertTrue(windows_phone_ua.is_mobile)
        self.assertTrue(j2me_opera_ua.is_mobile)
        self.assertFalse(windows_rt_ua.is_mobile)
        self.assertFalse(ipad_ua.is_mobile)
        self.assertFalse(playbook_ua.is_mobile)
        self.assertFalse(kindle_fire_ua.is_mobile)
        self.assertFalse(nexus_7_ua.is_mobile)
        self.assertFalse(ie_ua.is_mobile)
        self.assertFalse(ie_touch_ua.is_mobile)
        self.assertFalse(mac_safari_ua.is_mobile)
        self.assertFalse(windows_ie_ua.is_mobile)
        self.assertFalse(ubuntu_firefox_ua.is_mobile)

    def test_is_touch_property(self):
        self.assertTrue(iphone_ua.is_touch_capable)
        self.assertTrue(galaxy_s3_ua.is_touch_capable)
        self.assertTrue(ipad_ua.is_touch_capable)
        self.assertTrue(playbook_ua.is_touch_capable)
        self.assertTrue(kindle_fire_ua.is_touch_capable)
        self.assertTrue(nexus_7_ua.is_touch_capable)
        self.assertTrue(windows_phone_ua.is_touch_capable)
        self.assertTrue(ie_touch_ua.is_touch_capable)
        self.assertTrue(blackberry_bold_touch_ua.is_mobile)
        self.assertTrue(blackberry_torch_ua.is_mobile)
        self.assertFalse(j2me_opera_ua.is_touch_capable)
        self.assertFalse(ie_ua.is_touch_capable)
        self.assertFalse(blackberry_bold_ua.is_touch_capable)
        self.assertFalse(mac_safari_ua.is_touch_capable)
        self.assertFalse(windows_ie_ua.is_touch_capable)
        self.assertFalse(ubuntu_firefox_ua.is_touch_capable)

    def test_is_pc(self):
        self.assertFalse(iphone_ua.is_pc)
        self.assertFalse(galaxy_s3_ua.is_pc)
        self.assertFalse(ipad_ua.is_pc)
        self.assertFalse(playbook_ua.is_pc)
        self.assertFalse(kindle_fire_ua.is_pc)
        self.assertFalse(nexus_7_ua.is_pc)
        self.assertFalse(windows_phone_ua.is_pc)
        self.assertFalse(blackberry_bold_touch_ua.is_pc)
        self.assertFalse(blackberry_torch_ua.is_pc)        
        self.assertFalse(blackberry_bold_ua.is_pc)
        self.assertFalse(j2me_opera_ua.is_pc)
        self.assertTrue(mac_safari_ua.is_pc)
        self.assertTrue(windows_ie_ua.is_pc)
        self.assertTrue(ubuntu_firefox_ua.is_pc)
        self.assertTrue(ie_touch_ua.is_pc)
        self.assertTrue(ie_ua.is_pc)
