# -*- coding:utf-8 -*-

import wx

import ui
from about import name, ver

def main():
	app = wx.PySimpleApp()
	frame = ui.createUI(None, wx.ID_ANY, name + ' ' + ver, style = wx.DEFAULT_FRAME_STYLE)
	app.MainLoop()
	
if __name__ == '__main__':
	main()