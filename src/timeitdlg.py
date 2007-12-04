# -*- coding: utf-8 -*- 

import wx

try:
	from codectrl.codeview import DemoCodeEditor as CodeEditor
except ImportError:
	CodeEditor = wx.TextCtrl

class TimeitDlg(wx.Dialog):
	def __init__(self, *a, **k):
		super(TimeitDlg, self).__init__(size = (640, 480), *a, **k)
		
		vbox = wx.BoxSizer(wx.VERTICAL)
		
		vbox.Add(wx.StaticText(self, wx.ID_ANY, 'Statement: '), \
			border = 10, \
			flag = wx.TOP | wx.ALIGN_LEFT)
		
		#self.stmt = wx.TextCtrl(self, wx.ID_ANY, style = wx.TE_MULTILINE | wx.HSCROLL )
		self.stmt = CodeEditor(self)
		vbox.Add(self.stmt, \
			proportion = 1, \
			flag = wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND )
			
		vbox.Add(wx.StaticText(self, wx.ID_ANY, 'Statement: '), \
			border = 10, \
			flag = wx.TOP | wx.ALIGN_LEFT)
		
		#self.setup = wx.TextCtrl(self, wx.ID_ANY, style = wx.TE_MULTILINE | wx.HSCROLL )
		self.setup = CodeEditor(self)
		vbox.Add(self.setup, \
			proportion = 1, \
			flag = wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND )
			
		hbox = wx.BoxSizer(wx.HORIZONTAL)
		hbox.Add(wx.StaticText(self, wx.ID_ANY, 'Number: '), \
			flag = wx.ALIGN_LEFT)
		self.number = wx.TextCtrl(self, wx.ID_ANY)
		hbox.Add(self.number, flag = wx.ALIGN_RIGHT | wx.EXPAND)
		vbox.Add(hbox, border = 10, flag = wx.TOP | wx.EXPAND)
		
		hbox = wx.BoxSizer(wx.HORIZONTAL)
		hbox.Add(wx.StaticText(self, wx.ID_ANY, 'Repeat: '), \
			flag = wx.ALIGN_LEFT)
		self.repeat = wx.TextCtrl(self, wx.ID_ANY)
		hbox.Add(self.repeat, flag = wx.ALIGN_RIGHT | wx.EXPAND)
		vbox.Add(hbox, border = 10, flag = wx.TOP | wx.EXPAND)
		
		self.clean = wx.Button(self, wx.ID_ANY, '&Clean')
		self.ok = wx.Button(self, wx.ID_ANY, '&OK')
		hbox = wx.BoxSizer(wx.HORIZONTAL)
		hbox.Add(self.clean, border = 10, flag = wx.LEFT | wx.ALIGN_RIGHT)
		hbox.Add(self.ok, border = 10, flag = wx.LEFT | wx.ALIGN_RIGHT)
		vbox.Add(hbox, border = 10, flag = wx.TOP | wx.ALIGN_RIGHT)
		
		self.SetSizer(vbox)
		
		self.clean.Bind(wx.EVT_BUTTON, self.OnClean)
		self.ok.Bind(wx.EVT_BUTTON, self.OnOk)
		
		self.Reset()
		
	def OnClean(self, evt):
		self.Reset()
		
	def OnOk(self, evt):
		class TimeitProc(wx.Process):
			def OnTerminate(inst, pid, status):
				#print inst.GetInputStream().Read()
				#print inst.GetErrorStream().Read()
				s = ''
				stream = inst.GetErrorStream()
				while True:
					c = stream.GetC()
					if 0 == stream.LastRead():
						break
					s += c
				print s
				s = ''
				stream = inst.GetInputStream()
				while True:
					c = stream.GetC()
					if 0 == stream.LastRead():
						break
					s += c
				print s
				
					
		stmt = self.stmt.GetText()
		setup = self.setup.GetText()
		import timeit
		cmd = 'python %s -n %s -r %s '%( \
			timeit.__file__, \
			self.number.GetValue(), \
			self.repeat.GetValue())
		if setup:
			cmd += '-s ' + '"%s"'%setup + ' '
		cmd += '"%s"'%stmt
		print cmd
		proc = TimeitProc(self)
		proc.Redirect()
		wx.Execute(cmd, process = proc)
		
	def Reset(self):
		self.stmt.SetValue('')
		self.setup.SetValue('')
		self.number.SetValue('1000000')
		self.repeat.SetValue('3')
		
def ShowTimeitDlg(parent):
	dlg = TimeitDlg(parent, wx.NewId(), 'Timeit')
	dlg.ShowModal()
	
if __name__ == '__main__':
	app = wx.PySimpleApp()
	ShowTimeitDlg(None)