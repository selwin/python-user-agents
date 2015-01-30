import sys
from collections import namedtuple

from ua_parser import user_agent_parser


PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

if PY3:
    string_types = str
else:
    string_types = basestring


MOBILE_DEVICE_FAMILIES = (
    'iPhone',
    'iPod',
    'Generic Smartphone',
    'Generic Feature Phone',
    'PlayStation Vita',
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
)

TOUCH_CAPABLE_DEVICE_FAMILIES = (
    'BlackBerry Playbook',
    'Blackberry Playbook',
    'Kindle Fire',
)


def parse_version(major=None, minor=None, patch=None, patch_minor=None):
    # Returns version number tuple, attributes will be integer if they're numbers
    if major is not None and isinstance(major, string_types):
        major = int(major) if major.isdigit() else major
    if minor is not None and isinstance(minor, string_types):
        minor = int(minor) if minor.isdigit() else minor
    if patch is not None and isinstance(patch, string_types):
        patch = int(patch) if patch.isdigit() else patch
    if patch_minor is not None and isinstance(patch_minor, string_types):
        patch_minor = int(patch_minor) if patch_minor.isdigit() else patch_minor
    if patch_minor:
        return (major, minor, patch, patch_minor)
    elif patch:
        return (major, minor, patch)
    elif minor:
        return (major, minor)
    elif major:
        return (major,)
    else:
        return tuple()


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


Device = namedtuple('Device', ['family'])


def parse_device(family):
    return Device(family)


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
        if self.os.family == 'Android' and not self.is_tablet:
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
        # Mobile Spiders should be identified as mobile
        if self.device.family == 'Spider' and 'Mobile' in self.browser.family:
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
        if 'Linux' in self.ua_string and 'X11' in self.ua_string:
            return True
        return False

    @property
    def is_bot(self):
        return True if self.device.family == 'Spider' else False


def parse(user_agent_string):
    return UserAgent(user_agent_string)
