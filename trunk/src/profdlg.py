# -*- coding: utf-8 -*- 

import wx

dlgsize = (640, 480)

class ProfDlg(wx.Dialog):
	def __init__(self, *a, **k):
		super(ProfDlg, self).__init__(size = dlgsize, *a, **k)
		
		vbox = wx.BoxSizer(wx.VERTICAL)
		
def ShowTimeitDlg(parent):
	dlg = ProfDlg(parent, wx.NewId(), 'Profile')
	dlg.ShowModal()
	dlg.Destroy()
	
if __name__ == '__main__':
	app = wx.PySimpleApp()
	ShowTimeitDlg(None)