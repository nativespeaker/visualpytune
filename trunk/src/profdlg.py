# -*- coding: utf-8 -*- 

import wx

dlgsize = (640, 480)

class ProfDlg(wx.Dialog):
	def __init__(self, *a, **k):
		super(ProfDlg, self).__init__(size = dlgsize, *a, **k)
		
		vbox = wx.BoxSizer(wx.VERTICAL)
		
		self.Bind(wx.EVT_CLOSE, self.OnClose)
		
	def OnClose(self, evt):
		self.Destroy()
		
def ShowProfDlg(parent):
	dlg = ProfDlg(parent, wx.NewId(), 'Profile')
	dlg.Show()
	
if __name__ == '__main__':
	app = wx.PySimpleApp()
	ShowProfDlg(None)
	app.MainLoop()