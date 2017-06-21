from collections import namedtuple

from ua_parser import user_agent_parser
from .compat import string_types


MOBILE_DEVICE_FAMILIES = (
    'iPhone', 'iPod', 'Generic Smartphone', 'Generic Feature Phone', 'PlayStation Vita',
    'iOS-Device', '0PJA10', '4009A', '5022E', '8050D', 'A0001', 'A40C', 'A40Style Lite',
    'A50Style_Plus', 'AZUMI A45GL', 'AZUMI A50', 'AZUMI A50c+', 'Alcatel One Touch 4033A',
    'Armor', 'Astro_X4', 'Asus Z00A', 'Asus Z012DC', 'BLU ADVANCE 5.5 HD', 'BLU DASH L',
    'BLU DASH M', 'BLU DASH X', 'BLU ENERGY X PLUS', 'BLU LIFE 8 XL', 'BLU LIFE PLAY MINI',
    'BLU NEO X MINI', 'BLU STUDIO 5.0 C HD', 'BLU STUDIO 5.0 Ce', 'BLU STUDIO 6.0 HD',
    'BLU STUDIO C', 'BLU STUDIO C 5+5', 'BLU STUDIO C HD', 'BLU STUDIO G',
    'BLU STUDIO G PLUS', 'BLU STUDIO ONE', 'BLU_STUDIO_XL', 'CAM-L23', 'D6603', 'DASH 5.0+',
    'DASH X PLUS', 'DIGICEL DL 1 lite', 'DIGICEL DL1000', 'DIGICEL DL755', 'DIGICEL DL800',
    'DIGICEL DL910', 'DIGICELDL1plus', 'DL750', 'Dash L2', 'E5823', 'E6833', 'ENERGY X',
    'EVA-L09', 'Generic Smartphone', 'HTC 6525LVW', 'HTC Desire 625',
    'HTC Desire 626GPLUS dual sim', 'HTC E9pw', 'HTC M9pw', 'HTC M9u', 'HTC One',
    'HTC One A9', 'HTC One M8', 'HTC One M8s', 'HTC One M9', 'HUAWEI CUN-L23',
    'HUAWEI CUN-L33', 'HUAWEI G7-L03', 'HUAWEI KII-L23', 'HUAWEI LUA-L03', 'HUAWEI NXT-L09',
    'HUAWEI Y360-U03', 'HUAWEI Y520-U03', 'K6000 Pro', 'KIW-L24', 'Kylin 5.0', 'LG-AS330',
    'LG-D851', 'LG-D855', 'LG-F350S', 'LG-H634', 'LG-H812', 'LG-H815', 'LG-H860',
    'LG-H870DS', 'LG-H962', 'LG-K120', 'LG-K350', 'LG-K410', 'LGMS395', 'LGMS631',
    'LIFE PLAY 2', 'LIFE PURE', 'LIFE PURE MINI', 'LIFE X8', 'LOGIC X4P', 'Lenovo K10e70',
    'MHA-L09', 'Moto G (4)', 'Moto G Play', 'MotoG3', 'Neo4_5', 'Nexus 5', 'Nexus 5X',
    'Nexus 6', 'Nexus 6P', 'Nitro_4', 'ONE A2005', 'ONE E1005', 'ONEPLUS A3000',
    'ONEPLUS A3010', 'Odys PRIME 5 PLUS', 'PLATINUM 5.0+', 'R1 HD', 'SKY 4.0D', 'STH100-1',
    'STUDIO ENERGY', 'STUDIO G PLUS', 'STUDIO M HD', 'STUDIO SELFIE', 'STUDIO X PLUS',
    'STV100-1', 'Samsung GT-I8190', 'Samsung GT-I8190L', 'Samsung GT-I8200N',
    'Samsung GT-I9060C', 'Samsung GT-I9060L', 'Samsung GT-I9060M', 'Samsung GT-I9082L',
    'Samsung GT-I9100', 'Samsung GT-I9152', 'Samsung GT-I9190', 'Samsung GT-I9192',
    'Samsung GT-I9195L', 'Samsung GT-I9295', 'Samsung GT-I9300', 'Samsung GT-I9300I',
    'Samsung GT-I9301I', 'Samsung GT-I9500', 'Samsung GT-I9505', 'Samsung GT-I9515',
    'Samsung SCH-I545', 'Samsung SGH-I337', 'Samsung SGH-I337M', 'Samsung SGH-I747M',
    'Samsung SM-A300H', 'Samsung SM-A500H', 'Samsung SM-A510M', 'Samsung SM-A520F',
    'Samsung SM-A710F', 'Samsung SM-A720F', 'Samsung SM-A9000', 'Samsung SM-G313M',
    'Samsung SM-G313ML', 'Samsung SM-G355M', 'Samsung SM-G386T1', 'Samsung SM-G530H',
    'Samsung SM-G531H', 'Samsung SM-G532M', 'Samsung SM-G550T1', 'Samsung SM-G570M',
    'Samsung SM-G610F', 'Samsung SM-G610M', 'Samsung SM-G7102', 'Samsung SM-G730W8',
    'Samsung SM-G800F', 'Samsung SM-G800H', 'Samsung SM-G800Y', 'Samsung SM-G850M',
    'Samsung SM-G891A', 'Samsung SM-G900A', 'Samsung SM-G900F', 'Samsung SM-G900FD',
    'Samsung SM-G900H', 'Samsung SM-G900M', 'Samsung SM-G900P', 'Samsung SM-G900T',
    'Samsung SM-G900V', 'Samsung SM-G900W8', 'Samsung SM-G903M', 'Samsung SM-G903W',
    'Samsung SM-G906S', 'Samsung SM-G920A', 'Samsung SM-G920F', 'Samsung SM-G920G',
    'Samsung SM-G920I', 'Samsung SM-G920P', 'Samsung SM-G920T', 'Samsung SM-G920V',
    'Samsung SM-G925A', 'Samsung SM-G925F', 'Samsung SM-G925I', 'Samsung SM-G925T',
    'Samsung SM-G925V', 'Samsung SM-G925W8', 'Samsung SM-G9287', 'Samsung SM-G928C',
    'Samsung SM-G928G', 'Samsung SM-G928V', 'Samsung SM-G930F', 'Samsung SM-G930P',
    'Samsung SM-G930T', 'Samsung SM-G930U', 'Samsung SM-G930V', 'Samsung SM-G930W8',
    'Samsung SM-G9350', 'Samsung SM-G935A', 'Samsung SM-G935F', 'Samsung SM-G935T',
    'Samsung SM-G935U', 'Samsung SM-G935V', 'Samsung SM-G935W8', 'Samsung SM-G950F',
    'Samsung SM-G950U', 'Samsung SM-G955F', 'Samsung SM-G955U', 'Samsung SM-J100M',
    'Samsung SM-J105B', 'Samsung SM-J105M', 'Samsung SM-J106B', 'Samsung SM-J110M',
    'Samsung SM-J111M', 'Samsung SM-J120M', 'Samsung SM-J200M', 'Samsung SM-J320A',
    'Samsung SM-J320H', 'Samsung SM-J320M', 'Samsung SM-J500M', 'Samsung SM-J510F',
    'Samsung SM-J510FN', 'Samsung SM-J510MN', 'Samsung SM-J700F', 'Samsung SM-J700H',
    'Samsung SM-J700M', 'Samsung SM-J710MN', 'Samsung SM-N900', 'Samsung SM-N900A',
    'Samsung SM-N900T', 'Samsung SM-N900V', 'Samsung SM-N910A', 'Samsung SM-N910C',
    'Samsung SM-N910H', 'Samsung SM-N910P', 'Samsung SM-N910W8', 'Samsung SM-N915G',
    'Samsung SM-N915T', 'Samsung SM-N9200', 'Samsung SM-N9208', 'Samsung SM-N920C',
    'Samsung SM-N920G', 'Samsung SM-N920I', 'Samsung SM-N920P', 'Samsung SM-N920V',
    'Samsung SM-N930F', 'Samsung SM-N930V', 'Samsung SM-T210', 'Samsung SM-T560',
    'Samsung SM-T585', 'Samsung SM-T810', 'Samsung SM-T817T', 'Sky 5.0S', 'Studio G Plus HD',
    'Studio Max', 'UP920', 'VIVO XL', 'Vivo 5 Mini', 'WAS-LX3', 'XT1032', 'XT1064',
    'XT1068', 'XT1575', 'Z220', 'Z351', 'Z515', 'Z520', 'ZTE A2017U'
)

PC_OS_FAMILIES = (
    'Windows 95',
    'Windows 98',
    'Windows ME',
    'Solaris',
)

MOBILE_OS_FAMILIES = (
    'Windows Phone',
    'Windows Phone OS',  # Earlier versions of ua-parser returns Windows Phone OS
    'Symbian OS',
    'Bada',
    'Windows CE',
    'Windows Mobile',
    'Maemo',
)

MOBILE_BROWSER_FAMILIES = (
    'Opera Mobile',
    'Opera Mini',
)

TABLET_DEVICE_FAMILIES = (
    'iPad',
    'BlackBerry Playbook',
    'Blackberry Playbook',  # Earlier versions of ua-parser returns "Blackberry" instead of "BlackBerry"
    'Kindle',
    'Kindle Fire',
    'Kindle Fire HD',
    'Galaxy Tab',
    'Xoom',
    'Dell Streak',
)

TOUCH_CAPABLE_OS_FAMILIES = (
    'iOS',
    'Android',
    'Windows Phone',
    'Windows Phone OS',
    'Windows RT',
    'Windows CE',
    'Windows Mobile',
    'Firefox OS',
    'MeeGo',
)

TOUCH_CAPABLE_DEVICE_FAMILIES = (
    'BlackBerry Playbook',
    'Blackberry Playbook',
    'Kindle Fire',
)

EMAIL_PROGRAM_FAMILIES = {
    'Outlook',
    'Windows Live Mail',
    'AirMail',
    'Apple Mail',
    'Outlook',
    'Thunderbird',
    'Lightning',
    'ThunderBrowse',
    'Windows Live Mail',
    'The Bat!',
    'Lotus Notes',
    'IBM Notes',
    'Barca',
    'MailBar',
    'kmail2',
    'YahooMobileMail'
}

def verify_attribute(attribute):
    if isinstance(attribute, string_types) and attribute.isdigit():
        return int(attribute)

    return attribute


def parse_version(major=None, minor=None, patch=None, patch_minor=None):
    # Returns version number tuple, attributes will be integer if they're numbers
    major = verify_attribute(major)
    minor = verify_attribute(minor)
    patch = verify_attribute(patch)
    patch_minor = verify_attribute(patch_minor)

    return tuple(
        filter(lambda x: x is not None, (major, minor, patch, patch_minor))
    )


Browser = namedtuple('Browser', ['family', 'version', 'version_string'])


def parse_browser(family, major=None, minor=None, patch=None, patch_minor=None):
    # Returns a browser object
    version = parse_version(major, minor, patch)
    version_string = '.'.join([str(v) for v in version])
    return Browser(family, version, version_string)


OperatingSystem = namedtuple('OperatingSystem', ['family', 'version', 'version_string'])


def parse_operating_system(family, major=None, minor=None, patch=None, patch_minor=None):
    version = parse_version(major, minor, patch)
    version_string = '.'.join([str(v) for v in version])
    return OperatingSystem(family, version, version_string)


Device = namedtuple('Device', ['family', 'brand', 'model'])


def parse_device(family, brand, model):
    return Device(family, brand, model)


class UserAgent(object):

    def __init__(self, user_agent_string):
        ua_dict = user_agent_parser.Parse(user_agent_string)
        self.ua_string = user_agent_string
        self.os = parse_operating_system(**ua_dict['os'])
        self.browser = parse_browser(**ua_dict['user_agent'])
        self.device = parse_device(**ua_dict['device'])

    def __str__(self):
        device = self.is_pc and "PC" or self.device.family
        os = ("%s %s" % (self.os.family, self.os.version_string)).strip()
        browser = ("%s %s" % (self.browser.family, self.browser.version_string)).strip()
        return " / ".join([device, os, browser])

    def __unicode__(self):
        return unicode(str(self))

    def _is_android_tablet(self):
        # Newer Android tablets don't have "Mobile" in their user agent string,
        # older ones like Galaxy Tab still have "Mobile" though they're not
        if ('Mobile Safari' not in self.ua_string and
                self.browser.family != "Firefox Mobile"):
            return True
        return False

    def _is_blackberry_touch_capable_device(self):
        # A helper to determine whether a BB phone has touch capabilities
        # Blackberry Bold Touch series begins with 99XX
        if 'Blackberry 99' in self.device.family:
            return True
        if 'Blackberry 95' in self.device.family:  # BB Storm devices
            return True
        if 'Blackberry 95' in self.device.family:  # BB Torch devices
            return True
        return False

    @property
    def is_tablet(self):
        if self.device.family in TABLET_DEVICE_FAMILIES:
            return True
        if (self.os.family == 'Android' and self._is_android_tablet()):
            return True
        if self.os.family.startswith('Windows RT'):
            return True
        if self.os.family == 'Firefox OS' and 'Mobile' not in self.browser.family:
            return True
        return False

    @property
    def is_mobile(self):
        # First check for mobile device and mobile browser families
        if self.device.family in MOBILE_DEVICE_FAMILIES:
            return True
        if self.browser.family in MOBILE_BROWSER_FAMILIES:
            return True
        # Device is considered Mobile OS is Android and not tablet
        # This is not fool proof but would have to suffice for now
        if ((self.os.family == 'Android' or self.os.family == 'Firefox OS')
            and not self.is_tablet):
            return True
        if self.os.family == 'BlackBerry OS' and self.device.family != 'Blackberry Playbook':
            return True
        if self.os.family in MOBILE_OS_FAMILIES:
            return True
        # TODO: remove after https://github.com/tobie/ua-parser/issues/126 is closed
        if 'J2ME' in self.ua_string or 'MIDP' in self.ua_string:
            return True
        # This is here mainly to detect Google's Mobile Spider
        if 'iPhone;' in self.ua_string:
            return True
        if 'Googlebot-Mobile' in self.ua_string:
            return True
        # Mobile Spiders should be identified as mobile
        if self.device.family == 'Spider' and 'Mobile' in self.browser.family:
            return True
        # Nokia mobile
        if 'NokiaBrowser' in self.ua_string and 'Mobile' in self.ua_string:
            return True
        return False

    @property
    def is_touch_capable(self):
        # TODO: detect touch capable Nokia devices
        if self.os.family in TOUCH_CAPABLE_OS_FAMILIES:
            return True
        if self.device.family in TOUCH_CAPABLE_DEVICE_FAMILIES:
            return True
        if self.os.family.startswith('Windows 8') and 'Touch' in self.ua_string:
            return True
        if 'BlackBerry' in self.os.family and self._is_blackberry_touch_capable_device():
            return True
        return False

    @property
    def is_pc(self):
        # Returns True for "PC" devices (Windows, Mac and Linux)
        if 'Windows NT' in self.ua_string or self.os.family in PC_OS_FAMILIES:
            return True
        # TODO: remove after https://github.com/tobie/ua-parser/issues/127 is closed
        if self.os.family == 'Mac OS X' and 'Silk' not in self.ua_string:
            return True
        # Maemo has 'Linux' and 'X11' in UA, but it is not for PC
        if 'Maemo' in self.ua_string:
            return False
        if 'Chrome OS' in self.os.family:
            return True
        if 'Linux' in self.ua_string and 'X11' in self.ua_string:
            return True
        return False

    @property
    def is_bot(self):
        return True if self.device.family == 'Spider' else False

    @property
    def is_email_client(self):
        if self.browser.family in EMAIL_PROGRAM_FAMILIES:
            return True
        return False

def parse(user_agent_string):
    return UserAgent(user_agent_string)
