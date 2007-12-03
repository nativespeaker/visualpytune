# -*- coding: utf-8 -*- 

import wx

class TimeitDlg(wx.Dialog):
	def __init__(self, *a, **k):
		super(TimeitDlg, self).__init__(*a, **k)
		
		panel = wx.Panel(self, wx.NewId())
		vbox = wx.BoxSizer(wx.VERTICAL)
		
		self.SetSizer(vbox)
		
def ShowTimeitDlg(parent):
	dlg = TimeitDlg(parent, wx.NewId(), 'Timeit')
	dlg.Show()
	
if __name__ == '__main__':
	app = wx.PySimpleApp()
	ShowTimeitDlg(None)