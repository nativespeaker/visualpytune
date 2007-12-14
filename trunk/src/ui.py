# -*- coding:utf-8 -*-

import wx
import os

import image_path as IP
	
def show(func):
	def show_func(*a, **k):
		obj = func(*a, **k)
		obj.Show(True)
		return obj
	return show_func

def centre(func):
	def centre_func(*a, **k):
		obj = func(*a, **k)
		obj.Centre()
		return obj
	return centre_func
	
def fullscreen(func):
	def fullscreen_func(*a, **k):
		obj = func(*a, **k)
		obj.ShowFullScreen(True)
		return obj
	return fullscreen_func
	
def maximize(func):
	def maximize_func(*a, **k):
		k['style'] = wx.MAXIMIZE
		obj = func(*a, **k)
		return obj
	return maximize_func

def createToolbar(frm):
	frm.toolbar = frm.CreateToolBar()
	frm.toolbar.SetToolBitmapSize(wx.Size(32, 32))
	frm.toolbar.AddSeparator()
	
def createStatusbar(frm):
	frm.CreateStatusBar()

def createMenu(frm):
	def createFileMenu(mb):
		menu = wx.Menu()
		
		# insert Open menu
		def _open(evt):
			dlg = wx.FileDialog( \
				frm, message = 'Open profile stats file', \
				defaultDir = frm.GetDirCtrlFilePath(), defaultFile = '', \
				wildcard = 'All files (*.*) | *.*', \
				style = wx.OPEN | wx.CHANGE_DIR )
			if dlg.ShowModal() != wx.ID_OK:
				return
			path = dlg.GetPath()
			if path:
				frm.OpenFile(path)
				frm.SetDirCtrlFilePath(os.path.dirname(path))
		ID_OPEN = wx.NewId()
		item_open = wx.MenuItem(menu, ID_OPEN, \
			'&Open...\tCtrl+Q', 'Open profile stats file.')
		item_open.SetBitmap(wx.Bitmap(IP.Menu.open))
		menu.AppendItem(item_open)
		frm.Bind(wx.EVT_MENU, _open, id = ID_OPEN)
		# add toolbar button
		frm.toolbar.AddLabelTool(ID_OPEN, '', \
			wx.Bitmap(IP.Toolbar.open), \
			shortHelp = 'Open profile stats file.')
		frm.toolbar.Realize()
		
		# insert Dump Stats menu
		def save(evt):
			dlg = wx.FileDialog( \
				frm, message = 'Save profile stats in a plain text file.', \
				defaultDir = frm.GetDirCtrlFilePath(), defaultFile = '', \
				wildcard = \
					'Text file (*.txt)|*.txt|All files (*.*)|*.*', \
				style = wx.SAVE)
			if dlg.ShowModal() != wx.ID_OK:
				return
			path = dlg.GetPath()
			if path:
				frm.SaveStats(path)
		ID_SAVE = wx.NewId()
		item_save = wx.MenuItem(menu, ID_SAVE, \
			'&Save...\tCtrl+S', 'save profile stats to text file.')
		item_save.SetBitmap(wx.Bitmap(IP.Menu.save))
		menu.AppendItem(item_save)
		frm.Bind(wx.EVT_MENU, save, id = ID_SAVE)
		# add toolbar button
		frm.toolbar.AddLabelTool(ID_SAVE, '', \
			wx.Bitmap(IP.Menu.save), \
			shortHelp = 'Save profile stats to text file.')
			
		frm.toolbar.Realize()
		
		# insert Separator
		menu.AppendSeparator()
		frm.toolbar.AddSeparator()
		
		# insert Quit menu
		def quit(event):
			frm.Close()
		
		ID_QUIT = wx.NewId()
		item_quit = wx.MenuItem(menu, ID_QUIT, '&Quit\tCtrl+Q', 'Quit Application!')
		item_quit.SetBitmap(wx.Bitmap(IP.Menu.quit))
		menu.AppendItem(item_quit)
		frm.Bind(wx.EVT_MENU, quit, id = ID_QUIT)
		
		mb.Append(menu, '&File')
		
	def createToolsMenu(mb):
		menu = wx.Menu()
		
		mb.Append(menu, '&Tools')
		
		def timeit(evt):
			from timeitdlg import ShowTimeitDlg
			ShowTimeitDlg(frm)
		
		ID_TIMEIT = wx.NewId()
		item_timeit = wx.MenuItem(menu, ID_TIMEIT, '&Time It\tCtrl+T')
		item_timeit.SetBitmap(wx.Bitmap(IP.Menu.timeit))
		menu.AppendItem(item_timeit)
		frm.Bind(wx.EVT_MENU, timeit, id = ID_TIMEIT)
		frm.toolbar.AddLabelTool(ID_TIMEIT, '', \
			wx.Bitmap(IP.Toolbar.timeit), \
			shortHelp = 'Time it')
		frm.toolbar.AddSeparator()
		frm.toolbar.Realize()
		
#	def createOptionMenu(mb):
#		menu = wx.Menu()
#		
#		mb.Append(menu, '&Option')
		
	def createHelpMenu(mb):
		menu = wx.Menu()
		
		#insert help menu
		def help(evt):
			print 'help'
			pass
		ID_HELP = wx.NewId()
		item_help = wx.MenuItem(menu, ID_HELP, '&Help\tCtrl+H')
		item_help.SetBitmap(wx.Bitmap(IP.Menu.help))
		menu.AppendItem(item_help)
		frm.Bind(wx.EVT_MENU, help, id = ID_HELP)
		# add toolbar button
		frm.toolbar.AddLabelTool(ID_HELP, '', \
			wx.Bitmap(IP.Toolbar.help), \
			shortHelp = 'Help')
		
		frm.toolbar.Realize()		
		
		#insert separator
		menu.AppendSeparator()
		
		# insert about menu
		def about(evt):
			def ShowAbout():
				from about import name, ver, url, author
				info = wx.AboutDialogInfo()
				
				lic = open('licence','rt')
				info.SetLicence(''.join(lic.readlines()))
				lic.close()
				
				info.SetIcon(wx.Icon(IP.PY_ICO, wx.BITMAP_TYPE_ICO))
				info.SetName(name)
				info.SetVersion(ver)
				info.SetDescription( \
					'VisualPyTune is a python program performance tuning tool, based on wxPython.\n'
					+ 'It can show you a callgraph(doing), stats report, callees, callers, and caky charts.\n'
					+ 'finaly, you can remove inessential information very easy. ')
				info.SetCopyright('(C) 2007 Yonghao Lai')
				info.SetWebSite(url)

				info.AddDeveloper(author)
#				info.AddDocWriter('Yonghao Lai')
#				info.AddArtist('Yonghao Lai')
#				info.AddTranslator('Yonghao Lai')

				wx.AboutBox(info)
			ShowAbout()
		ID_ABOUT = wx.NewId()
		item_about = wx.MenuItem(menu, ID_ABOUT, '&About...')
		menu.AppendItem(item_about)
		frm.Bind(wx.EVT_MENU, about, id = ID_ABOUT)
		
		mb.Append(menu, '&Help')
		
	mb = wx.MenuBar()
	frm.SetMenuBar(mb)
	
	createFileMenu(mb)
	createToolsMenu(mb)
#	createOptionMenu(mb)
	createHelpMenu(mb)
	
def createMainUI(frm):
	from viewpanel import Panel as vp
	from statspanel import Panel as sp
	from callerspanel import Panel as cp
	from calleespanel import Panel as cep
	from uicfg import UIConfig
	
	from proportionalsplitter import ProportionalSplitter
	splitter = ProportionalSplitter(frm, wx.ID_ANY, \
		proportion = UIConfig.inst().getLeftSplitProp(),)
	
	frm.viewpanel = vp(splitter)
	usplitter = ProportionalSplitter(splitter, wx.ID_ANY, \
		proportion = UIConfig.inst().getUpSplitProp(), \
		style = wx.BORDER_NONE)
	splitter.SplitVertically(frm.viewpanel, usplitter)
		
	frm.statspanel = sp(usplitter)
	rsplitter = ProportionalSplitter(usplitter, wx.ID_ANY, \
		proportion = UIConfig.inst().getRightSplitProp(), \
		style = wx.BORDER_NONE)
	usplitter.SplitHorizontally(frm.statspanel, rsplitter)
	
	frm.callerspanel = cp(rsplitter)
	frm.calleespanel = cep(rsplitter)
	rsplitter.SplitVertically(frm.callerspanel, frm.calleespanel)
	
	def OnStatsSelected(evt):
		idx = evt.GetIndex()
		evt_list = frm.statspanel.listctrl
		idx = int(evt_list.GetItemText(idx))
		fln = frm.model.get_fln_by_idx(idx)
		caky_title = 'Callees of ' + fln
		frm.calleespanel.update(caky_title, frm.model.get_callees(idx))
		frm.callerspanel.update(caky_title, frm.model.get_callers(idx))
		
	frm.statspanel.listctrl.selected_callback = OnStatsSelected
	
	def OnDirCtrlSelChanged(evt):
		p = frm.viewpanel.dirctrl.GetFilePath()
		if p and os.path.isfile(p):
			frm.OpenFile(p)
		evt.Skip()
#	frm.viewpanel.dirctrl.GetTreeCtrl().Bind(wx.EVT_TREE_SEL_CHANGED, \
#								OnDirCtrlSelChanged)
	wx.EVT_TREE_SEL_CHANGED(frm.viewpanel.dirctrl, \
		frm.viewpanel.dirctrl.GetTreeCtrl().GetId(), \
		OnDirCtrlSelChanged)
		
	def OnSize(evt):
		size = evt.GetSize()
		UIConfig.inst().setWindowSize((size.x, size.y))
		evt.Skip()
	frm.Bind(wx.EVT_SIZE, OnSize, frm)
		
	def OnClose(evt):
		path = frm.viewpanel.dirctrl.GetPath()
		UIConfig.inst().setLastDir( \
			path if os.path.isdir(path) else os.path.dirname(path))
		UIConfig.inst().setMaximized( \
			frm.IsMaximized())
		UIConfig.inst().setWindowPos(frm.GetPositionTuple())
		UIConfig.inst().setLeftSplitProp(splitter.proportion)
		UIConfig.inst().setUpSplitProp(usplitter.proportion)
		UIConfig.inst().setRightSplitProp(rsplitter.proportion)
		UIConfig.inst().release()
#		frm.Destroy()
		evt.Skip()
	frm.Bind(wx.EVT_CLOSE, OnClose, frm)
		
def AddMiscFunc(frm):
	def GetDirCtrlFilePath():
		path = frm.viewpanel.dirctrl.GetPath()
		if path:
			if os.path.isdir(path):
				return path
			else:
				return os.path.dirname(path)
		return os.getcwd()
	frm.GetDirCtrlFilePath = GetDirCtrlFilePath
	
	def SetDirCtrlFilePath(path):
		frm.viewpanel.dirctrl.SetPath(path)
	frm.SetDirCtrlFilePath = SetDirCtrlFilePath	
	
	def OpenFile(path):
		assert path
		print 'open', path
		from statsmodel import StatsModel
		try:
			frm.model = StatsModel(path)
		except:
			import sys
			from traceback import print_exc
			print_exc(file = sys.stdout)
			return
		frm.statspanel.listctrl.reset(frm.model.get_data())
	frm.OpenFile = OpenFile
	
	def SaveStats(path):
		assert path
		frm.model.save_stats(path)
	frm.SaveStats = SaveStats
		
#@centre
#@fullscreen
@show
def createUI(*a, **k):
	from uicfg import UIConfig

	if UIConfig.inst().getMaximized():
		if 'style' in k:
			k['style'] |= wx.MAXIMIZE
		else:
			k['style'] = wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE
	else:
		k['size'] = UIConfig.inst().getWindowSize()
		k['pos'] = UIConfig.inst().getWindowPos()
		
	obj = wx.Frame(*a, **k)
	
	obj.SetIcon(wx.Icon(IP.PY_ICO, wx.BITMAP_TYPE_ICO))
	createToolbar(obj)
	createMenu(obj)
	createStatusbar(obj)
	createMainUI(obj)
	AddMiscFunc(obj)
	
	if UIConfig.inst().getMaximized():
#		wx.CallAfter(obj.Maximize)
		obj.Maximize()
	
	return obj
	