# -*- coding:utf-8 -*-

import wx

class FilterPanel(wx.Panel):
	def __init__(self, *a, **k):
		super(FilterPanel, self).__init__(*a, **k)
		
		rbox = wx.BoxSizer(wx.HORIZONTAL)
			
		rbox.Add(wx.StaticText(self, wx.ID_ANY, 'Func Filter:'), \
			border = 10, \
			flag = wx.TOP | wx.LEFT | wx.ALIGN_CENTER_VERTICAL)
		
		self.func_filter = wx.TextCtrl(self, wx.ID_ANY)
		rbox.Add(self.func_filter, \
			border = 10, \
			proportion = 1, \
			flag = wx.TOP | wx.LEFT | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL)
		
		rbox.Add(wx.StaticText(self, wx.ID_ANY, 'File Filter:'), \
			border = 10, \
			flag = wx.TOP | wx.LEFT | wx.ALIGN_CENTER_VERTICAL)
			
		self.file_filter = wx.TextCtrl(self, wx.ID_ANY)
		rbox.Add(self.file_filter, \
			border = 10, \
			proportion = 1, \
			flag = wx.TOP | wx.LEFT | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL)
		
		ID_OK = wx.NewId()
		self.OkButton = wx.Button(self, ID_OK, '&OK')
		rbox.Add(self.OkButton, \
			border = 10, \
			flag = wx.TOP | wx.LEFT | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL)
		self.Bind(wx.EVT_BUTTON, self.OnOk, id = ID_OK)
		
		ID_RESET = wx.NewId()
		self.ResetButton = wx.Button(self, ID_RESET, '&Reset')
		rbox.Add(self.ResetButton, \
			border = 10, \
			flag = wx.TOP | wx.LEFT | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL)
		self.Bind(wx.EVT_BUTTON, self.OnReset, id = ID_RESET)
			
		lbox = wx.BoxSizer(wx.HORIZONTAL)
		ID_ALL = wx.NewId()
		self.AllButton = wx.Button(self, ID_ALL, '&Show all items')
		lbox.Add(self.AllButton, \
			border = 10, \
			flag = wx.TOP | wx.LEFT | wx.ALIGN_CENTER_VERTICAL)
		self.Bind(wx.EVT_BUTTON, self.OnAll, id = ID_ALL)
			
		hbox = wx.BoxSizer(wx.HORIZONTAL)
		hbox.Add(lbox, flag = wx.EXPAND | wx.ALIGN_LEFT)
		hbox.Add(rbox, proportion = 1, flag = wx.EXPAND | wx.ALIGN_RIGHT)
			
		vbox = wx.BoxSizer(wx.VERTICAL)
		vbox.Add(hbox, \
			border = 10, \
			proportion = 1, \
			flag = wx.RIGHT | wx.EXPAND)
		vbox.Add(wx.StaticLine(self), \
			border = 10, \
			flag = wx.TOP | wx.BOTTOM | wx.EXPAND)
		
		self.SetSizer(vbox)
		
		self.ok_callback = None
		self.all_callback = None
		
	def OnOk(self, evt):
		if self.ok_callback:
			self.ok_callback( \
				self.func_filter.GetValue(), \
				self.file_filter.GetValue())
		
	def OnReset(self, evt):
		self.func_filter.Clear()
		self.file_filter.Clear()
		
		
	def OnAll(self, evt):
		if self.all_callback:
			self.all_callback()
		
if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = wx.Frame(None, wx.ID_ANY, 'Test FilterPanel')
	FilterPanel(frame)
	frame.Centre()
	frame.Show(True)
	app.MainLoop()