# -*- coding: utf-8 -*- 

import wx
from wx.lib.intctrl import IntCtrl
from codectrl.codeview import DemoCodeEditor as CodeEditor

dlgsize = (640, 480)

class TimeitDlg(wx.Dialog):
	def __init__(self, *a, **k):
		super(TimeitDlg, self).__init__(size = dlgsize, *a, **k)
		
		vbox = wx.BoxSizer(wx.VERTICAL)
		
		# --------------- statement ------------------------------------
		hbox = wx.BoxSizer(wx.HORIZONTAL)
		self.stmtbtn = wx.Button(self, wx.ID_ANY, 'Statement >>')
		self.stmtbtn.closed = False
		hbox.Add(self.stmtbtn, \
			border = 10, \
			flag = wx.LEFT | wx.ALIGN_LEFT)
		hbox.Add(wx.StaticLine(self), \
			border = 10, \
			proportion = 1, \
			flag = wx.RIGHT  | wx.ALIGN_RIGHT | wx.ALIGN_CENTRE_VERTICAL)
		vbox.Add(hbox, border = 10, flag = wx.TOP | wx.EXPAND)
		
		#self.stmt = wx.TextCtrl(self, wx.ID_ANY, style = wx.TE_MULTILINE | wx.HSCROLL )
		self.stmt = CodeEditor(self)
		vbox.Add(self.stmt, \
			proportion = 1, \
			flag = wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND )
			
		# --------------- setup ----------------------------------------
		hbox = wx.BoxSizer(wx.HORIZONTAL)
		self.setupbtn = wx.Button(self, wx.ID_ANY, 'Setup >>')
		self.setupbtn.closed = False
		hbox.Add(self.setupbtn, \
			border = 10, \
			flag = wx.LEFT | wx.ALIGN_LEFT)
		hbox.Add(wx.StaticLine(self), \
			border = 10, \
			proportion = 1, \
			flag = wx.RIGHT | wx.ALIGN_CENTRE_VERTICAL)
		vbox.Add(hbox, border = 10, flag = wx.TOP | wx.EXPAND)
		
		#self.setup = wx.TextCtrl(self, wx.ID_ANY, style = wx.TE_MULTILINE | wx.HSCROLL )
		self.setup = CodeEditor(self)
		vbox.Add(self.setup, \
			proportion = 1, \
			flag = wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND )
		self.setup.Show(True)
			
		# --------------- arguments ------------------------------------
		hbox = wx.BoxSizer(wx.HORIZONTAL)
		self.argsbtn = wx.Button(self, wx.ID_ANY, 'Arguments >>')
		self.argsbtn.closed = False
		hbox.Add(self.argsbtn, \
			border = 10, \
			flag = wx.LEFT | wx.ALIGN_LEFT)
		hbox.Add(wx.StaticLine(self), \
			border = 10, \
			proportion = 1, \
			flag = wx.RIGHT | wx.ALIGN_CENTRE_VERTICAL)
		vbox.Add(hbox, border = 10, flag = wx.TOP | wx.EXPAND)
		
		self.argsbox = wx.BoxSizer(wx.VERTICAL)
		hbox = wx.BoxSizer(wx.HORIZONTAL)
		hbox.Add(wx.StaticText(self, wx.ID_ANY, 'Number: '), \
			flag = wx.ALIGN_LEFT)
		self.number = IntCtrl(self)
		hbox.Add(self.number, flag = wx.ALIGN_RIGHT | wx.EXPAND)
		self.argsbox.Add(hbox, border = 10, flag = wx.TOP | wx.EXPAND)
		
		hbox = wx.BoxSizer(wx.HORIZONTAL)
		hbox.Add(wx.StaticText(self, wx.ID_ANY, 'Repeat: '), \
			flag = wx.ALIGN_LEFT)
		self.repeat = IntCtrl(self)
		hbox.Add(self.repeat, flag = wx.ALIGN_RIGHT | wx.EXPAND)
		self.argsbox.Add(hbox, border = 10, flag = wx.TOP | wx.EXPAND)
		
		vbox.Add(self.argsbox, flag = wx.EXPAND)
		
		# ---------------- error and output ----------------------------
		hbox = wx.BoxSizer(wx.HORIZONTAL)
		self.resultbtn = wx.Button(self, wx.ID_ANY, 'Result >>')
		self.resultbtn.closed = False
		hbox.Add(self.resultbtn, \
			border = 10, \
			flag = wx.LEFT | wx.ALIGN_LEFT)
		hbox.Add(wx.StaticLine(self), \
			border = 10, \
			proportion = 1, \
			flag = wx.RIGHT | wx.ALIGN_CENTRE_VERTICAL)
		vbox.Add(hbox, border = 10, flag = wx.TOP | wx.EXPAND)
		
		self.result = wx.TextCtrl(self, \
			wx.ID_ANY, style = wx.TE_MULTILINE | wx.HSCROLL | wx.VSCROLL)
		vbox.Add(self.result, \
			proportion = 1, \
			flag = wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND )
		# ---------------- buttons -------------------------------------
		self.clean = wx.Button(self, wx.ID_ANY, '&Clean')
		self.ok = wx.Button(self, wx.ID_ANY, '&OK')
		hbox = wx.BoxSizer(wx.HORIZONTAL)
		hbox.Add(self.clean, border = 10, flag = wx.LEFT | wx.ALIGN_RIGHT)
		hbox.Add(self.ok, border = 10, flag = wx.LEFT | wx.ALIGN_RIGHT)
		vbox.Add(hbox, border = 10, flag = wx.TOP | wx.ALIGN_RIGHT)
		
		self.SetSizer(vbox)
		
		self.stmtbtn.Bind(wx.EVT_BUTTON, self.OnStmtbtn)
		self.setupbtn.Bind(wx.EVT_BUTTON, self.OnSetupbtn)
		self.argsbtn.Bind(wx.EVT_BUTTON, self.OnArgsbtn)
		self.resultbtn.Bind(wx.EVT_BUTTON, self.OnResultbtn)
		
		self.clean.Bind(wx.EVT_BUTTON, self.OnClean)
		self.ok.Bind(wx.EVT_BUTTON, self.OnOk)
		
		self.Reset()
		self.OnArgsbtn(None)
#		self.OnStmtbtn(None)
		self.OnSetupbtn(None)
		self.OnResultbtn(None)
		
	def OnArgsbtn(self, evt):
		if self.argsbtn.closed:
			self.GetSizer().Show(self.argsbox, True, True)
			self.argsbtn.SetLabel('Arguments <<')
		else:
			self.GetSizer().Show(self.argsbox, False, True)
			self.argsbtn.SetLabel('Arguments >>')
		self.Fit()
		self.argsbtn.closed ^= True
		
	def OnStmtbtn(self, evt):
		self.DoClose(self.stmtbtn, self.stmt, \
			('Statement >>', 'Statement <<'))
		
	def OnSetupbtn(self, evt):
		self.DoClose(self.setupbtn, self.setup, \
			('Setup >>', 'Setup <<'))
		
	def OnResultbtn(self, evt):
		self.DoClose(self.resultbtn, self.result, \
			('Result >>', 'Result <<'))
			
	def DoClose(self, btn, ctrl, lbls):
		ctrl.Show(btn.closed)
		btn.SetLabel(lbls[int(btn.closed)])
		self.Fit()
		btn.closed ^= True
		
	def OnClean(self, evt):
		self.Reset()
		
	def OnOk(self, evt):
		class TimeitProc(wx.Process):
			def OnTerminate(inst, pid, status):
				def getstr(stream):
					s = ''
					while True:
						c = stream.GetC()
						if 0 == stream.LastRead():
							break
						s += c
					return s
				self.result.SetValue( \
					'============ Error ============\n' \
					+ getstr(inst.GetErrorStream()) \
					+ '\n============ Output ============\n' \
					+ getstr(inst.GetInputStream()))
				if self.resultbtn.closed:
					self.OnResultbtn(None)
					
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
		self.number.SetValue(1000000)
		self.repeat.SetValue(3)
		
	def Fit(self):
		if not self.IsShown():
			return
		self.GetSizer().Fit(self)
		self.SetSize(dlgsize)
		
def ShowTimeitDlg(parent):
	dlg = TimeitDlg(parent, wx.NewId(), 'Timeit')
	dlg.ShowModal()
	
if __name__ == '__main__':
	app = wx.PySimpleApp()
	ShowTimeitDlg(None)