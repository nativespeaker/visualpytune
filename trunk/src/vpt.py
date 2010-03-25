# -*- coding:utf-8 -*-

import wx
import profile
import ui
from about import name, ver

def try_psyco():
	try:
		import psyco
		psyco.full()
		print 'Psyco works!'
	except ImportError:
		import sys
		print >>sys.stderr, 'Psyco is not installed!'

def main():
	try_psyco()
	app = wx.PySimpleApp()
	frame = ui.createUI(None, wx.ID_ANY, name + ' ' + ver)
	app.MainLoop()
	
if __name__ == '__main__':
	#profile.run("main()", "vp1.prof")
	main()
	