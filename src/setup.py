# -*- coding: utf-8 -*-

from glob import glob
from distutils.core import setup
import py2exe

from about import name, ver

setup(windows=["vpt.py"], \
	options = {'py2exe':{'optimize':2}}, \
	name = name, \
	version = ver, \
	data_files = [('option', ['option/ui.cfg']), \
		('res/codectrl', glob('res/codectrl/*.png')), \
		('res/menu', glob('res/menu/*.png')), \
		('res/menu', glob('res/toolbar/*.png'))]
	)