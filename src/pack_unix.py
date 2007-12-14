# -*- coding: utf-8 -*-

from distutils.core import setup
from glob import glob
from about import *

setup(name= name,
	  version=ver,
	  author = author, 
	  author_email = author_email, 
	  url = url, 
	  package_dir={'VisualPyTune': '.'},
	  data_files = [ \
		('option', ['dist/option/ui.cfg']), \
		('', glob('*.py')), \
		('', ['dist/licence']), \
		('res', ['dist/res/Py.ico']), \
		('res/codectrl', glob('dist/res/codectrl/*.png')), \
		('res/menu', glob('dist/res/menu/*.png')), \
		('res/toolbar', glob('dist/res/toolbar/*.png'))
	  	]
	  )
