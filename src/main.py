# -*- coding:utf-8 -*-

import wx

import ui

def main():
	app = wx.PySimpleApp()
	frame = ui.createUI(None, wx.ID_ANY, 'VisualPyTune', style = wx.DEFAULT_FRAME_STYLE)
	app.MainLoop()
	
if __name__ == '__main__':
	main()