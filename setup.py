# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='user-agents',
    version='1.0.1',
    author='Selwin Ong',
    author_email='selwin.ong@gmail.com',
    packages=['user_agents'],
    url='https://github.com/selwin/python-user-agents',
    license='MIT',
    description='A library to identify devices (phones, tablets) and their capabilities by parsing (browser/HTTP) user agent strings',
    long_description=open('README.rst').read(),
    zip_safe=False,
    include_package_data=True,
    package_data={'': ['README.rst']},
    install_requires=['ua-parser'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
