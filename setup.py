# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='user-agents',
    version='0.1',
    author='Selwin Ong',
    author_email='selwin.ong@gmail.com',
    packages=['user_agents'],
    url='https://github.com/selwin/python-user-agents',
    license='MIT',
    description='A library to identify devices (phones, tablets) and their capabilities by parsing (browser) user agent strings',
    long_description=open('README.rst').read(),
    zip_safe=False,
    include_package_data=True,
    package_data = { '': ['README.rst'] },
    install_requires=['ua-parser'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
