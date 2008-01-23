# -*- coding: utf-8 -*- 

import wx

class AskPythonPathDlg(wx.Dialog):
	def __init__(self, *a, **k):
		super(AskPythonPathDlg, self).__init__(*a, **k)
		
#		vbox
#		hbox
#		okbtn = wx.Button(self, 
		
	def GetPath(self):
		return ''
	
#	def ShowModal(self):
#		super(AskPythonPathDlg, self).ShowModal()
#		if self.ok:
#			return wx.ID_OK
#		else:
#			return wx.ID_CANCEL