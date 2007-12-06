# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe

from about import name, ver

setup(windows=["vpt.py"], \
	options = {'py2exe':{'optimize':2}}, \
	name = name, \
	version = ver, \
	)