# Python User Agents

``user_agents`` is a Python library that provides an easy way to identify/detect devices like mobile
phones, tablets and their capabilities by parsing (browser/HTTP) user agent strings. The goal is to reliably detect whether:

* User agent is a mobile, tablet or PC based device
* User agent has touch capabilities (has touch screen)

``user_agents`` relies on the excellent `ua-parser <https://github.com/tobie/ua-parser>`_ to do the
actual parsing of the raw user agent string.


## Installation

![Build status](https://secure.travis-ci.org/selwin/python-user-agents.png)

``user-agents`` is hosted on [PyPI](http://pypi.python.org/pypi/user-agents/) and can be installed as such:

    pip install pyyaml ua-parser user-agents

Alternatively, you can also get the latest source code from
`Github`_ and install it manually.

## Usage

Various basic information that can help you identify visitors can be accessed `browser`, `device`
and `os` attributes. For example:

```python

from user_agents import parse

# iPhone's user agent string
ua_string = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'
user_agent = parse(ua_string)

# Accessing user agent's browser attributes
user_agent.browser  # returns Browser(family=u'Mobile Safari', version=(5, 1), version_string='5.1')
user_agent.browser.family  # returns 'Mobile Safari'
user_agent.browser.version  # returns (5, 1)
user_agent.browser.version_string   # returns '5.1'

# Accessing user agent's operating system properties
user_agent.os  # returns OperatingSystem(family=u'iOS', version=(5, 1), version_string='5.1')
user_agent.os.family  # returns 'iOS'
user_agent.os.version  # returns (5, 1)
user_agent.os.version_string  # returns '5.1'

# Accessing user agent's device properties
user_agent.device  # returns Device(family=u'iPhone', brand=u'Apple', model=u'iPhone')
user_agent.device.family  # returns 'iPhone'
user_agent.device.brand # returns 'Apple'
user_agent.device.model # returns 'iPhone'

# Viewing a pretty string version
str(user_agent) # returns "iPhone / iOS 5.1 / Mobile Safari 5.1"
```

``user_agents`` also expose a few other more "sophisticated" attributes that are derived from one or
more basic attributes defined above. As for now, these attributes should correctly identify
popular platforms/devices, pull requests to support smaller ones are always welcome.

Currently these attributes are supported:

* ``is_mobile``: whether user agent is identified as a mobile phone (iPhone, Android phones, Blackberry, Windows Phone devices etc)
* ``is_tablet``: whether user agent is identified as a tablet device (iPad, Kindle Fire, Nexus 7 etc)
* ``is_pc``: whether user agent is identified to be running a traditional "desktop" OS (Windows, OS X, Linux)
* ``is_touch_capable``: whether user agent has touch capabilities
* ``is_bot``: whether user agent is a search engine crawler/spider


For example:

``` python

from user_agents import parse

# Let's start from an old, non touch Blackberry device
ua_string = 'BlackBerry9700/5.0.0.862 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/331 UNTRUSTED/1.0 3gpp-gba'
user_agent = parse(ua_string)
user_agent.is_mobile # returns True
user_agent.is_tablet # returns False
user_agent.is_touch_capable # returns False
user_agent.is_pc # returns False
user_agent.is_bot # returns False
str(user_agent) # returns "BlackBerry 9700 / BlackBerry OS 5.0.0 / BlackBerry 9700"

# Now a Samsung Galaxy S3
ua_string = 'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
user_agent = parse(ua_string)
user_agent.is_mobile # returns True
user_agent.is_tablet # returns False
user_agent.is_touch_capable # returns True
user_agent.is_pc # returns False
user_agent.is_bot # returns False
str(user_agent) # returns "Samsung GT-I9300 / Android 4.0.4 / Android 4.0.4"

# iPad's user agent string
ua_string = 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10'
user_agent = parse(ua_string)
user_agent.is_mobile # returns False
user_agent.is_tablet # returns True
user_agent.is_touch_capable # returns True
user_agent.is_pc # returns False
user_agent.is_bot # returns False
str(user_agent) # returns "iPad / iOS 3.2 / Mobile Safari 4.0.4"

# Kindle Fire's user agent string
ua_string = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-us; Silk/1.1.0-80) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16 Silk-Accelerated=true'
user_agent = parse(ua_string)
user_agent.is_mobile # returns False
user_agent.is_tablet # returns True
user_agent.is_touch_capable # returns True
user_agent.is_pc # returns False
user_agent.is_bot # returns False
str(user_agent) # returns "Kindle / Android / Amazon Silk 1.1.0-80"

# Touch capable Windows 8 device
ua_string = 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; Touch)'
user_agent = parse(ua_string)
user_agent.is_mobile # returns False
user_agent.is_tablet # returns False
user_agent.is_touch_capable # returns True
user_agent.is_pc # returns True
user_agent.is_bot # returns False
str(user_agent) # returns "PC / Windows 8 / IE 10.0"
```

## Running Tests

    python -m unittest discover


## Changelog

### Version 1.0.0

* Fixes packaging issue

### Version 1.0

* Adds compatibility with ``ua-parser`` 0.4.0
* Access to more device information in ``user_agent.device.brand`` and ``user_agent.device.model``

===

### Version 0.3.2

* Better mobile detection
* Better PC detection

### Version 0.3.1

* user_agent.is_mobile returns True when mobile spider is detected

### Version 0.3.0

* Added __str__/__unicode__ methods for convenience of pretty string

### Version 0.2.0

* Fixed errors when running against newer versions if ua-parser
* Support for Python 3

### Version 0.1.1

* Added ``is_bot`` property
* Symbian OS devices are now detected as a mobile device

### Version 0.1

* Initial release


Developed by the cool guys at [Stamps](http://stamps.co.id).
