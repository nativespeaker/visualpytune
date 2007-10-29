# -*- coding:utf-8 -*-

import wx

class FindReplaceMixin(object):
	def __init__(self):
		self.Bind(wx.EVT_FIND, self.OnFind)
		self.Bind(wx.EVT_FIND_NEXT, self.OnFindNext)
		self.Bind(wx.EVT_FIND_REPLACE, self.OnReplace)
		self.Bind(wx.EVT_FIND_REPLACE_ALL, self.OnReplaceAll)
		self.Bind(wx.EVT_FIND_CLOSE, self.OnFindReplaceClose)
		
	def GetEditor(self):
		raise NotImplementedError
		
	def ShowFindDlg(self):
		data = wx.FindReplaceData()
		dlg = wx.FindReplaceDialog(self, data, "Find")
		dlg.data = data  # save a reference to it...
		dlg.Show(True)
		
	def ShowFindReplaceDlg(self):
		data = wx.FindReplaceData()
		dlg = wx.FindReplaceDialog(self, data, "Find & Replace", wx.FR_REPLACEDIALOG)
		dlg.data = data  # save a reference to it...
		dlg.Show(True)
		
	def OnFind(self, evt):
		editor = self.GetEditor()
		if wx.FR_DOWN & evt.GetFlags():
			start, end = editor.GetSelectionEnd(), editor.GetLength()
		else:
			start, end = editor.GetSelectionStart(), 0
		self.__do_find(editor, start, end, evt.GetFindString(), evt.GetFlags())
		
	def OnFindNext(self, evt):
		return self.OnFind(evt)
		
	def OnReplace(self, evt):
		pos = self.OnFind(evt)
		if pos < 0:
			return
		print evt.GetReplaceString()
		self.GetEditor.ReplaceSelection(evt.GetReplaceString())
		
	def OnReplaceAll(self, evt):
		pass
		
	def OnFindReplaceClose(self, evt):
		evt.GetDialog().Destroy()
		
	def __do_find(self, editor, start, end, findstr, flags):
		pos = editor.FindText(start, end, findstr, flags)
		print pos
		if pos >= 0:
			editor.SetSelection(pos, pos + len(findstr))
		else:
			wx.MessageDialog(self, \
				'"%s" not found.'%(findstr, ), \
				'Find', \
				wx.OK | wx.ICON_EXCLAMATION).ShowModal()
		return pos