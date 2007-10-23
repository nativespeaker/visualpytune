# -*- coding:utf-8 -*-

import wx
import os
		
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
		item_open.SetBitmap(wx.Bitmap('res/menu/document-open.png'))
		menu.AppendItem(item_open)
		frm.Bind(wx.EVT_MENU, _open, id = ID_OPEN)
		# add toolbar button
		frm.toolbar.AddLabelTool(ID_OPEN, '', \
			wx.Bitmap('res/toolbar/document-open.png'), \
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
		item_save.SetBitmap(wx.Bitmap('res/menu/document-save.png'))
		menu.AppendItem(item_save)
		frm.Bind(wx.EVT_MENU, save, id = ID_SAVE)
		# add toolbar button
		frm.toolbar.AddLabelTool(ID_SAVE, '', \
			wx.Bitmap('res/toolbar/document-save.png'), \
			shortHelp = 'Save profile stats to text file.')
			
		frm.toolbar.Realize()
		
		# insert Separator
		menu.AppendSeparator()
		frm.toolbar.AddSeparator()
		
		# insert Quit menu
		def quit(event):
			frm.Destroy()
		
		ID_QUIT = wx.NewId()
		item_quit = wx.MenuItem(menu, ID_QUIT, '&Quit\tCtrl+Q', 'Quit Application!')
		item_quit.SetBitmap(wx.Bitmap('res/menu/process-stop.png'))
		menu.AppendItem(item_quit)
		frm.Bind(wx.EVT_MENU, quit, id = ID_QUIT)
		
		mb.Append(menu, '&File')
		
	def createToolsMenu(mb):
		menu = wx.Menu()
		
		mb.Append(menu, '&Tools')
		
	def createOptionMenu(mb):
		menu = wx.Menu()
		
		mb.Append(menu, '&Option')
		
	def createHelpMenu(mb):
		menu = wx.Menu()
		
		#insert help menu
		def help(evt):
			pass
		ID_HELP = wx.NewId()
		item_help = wx.MenuItem(menu, ID_HELP, '&Help\tCtrl+H')
		item_help.SetBitmap(wx.Bitmap('res/menu/help-browser.png'))
		menu.AppendItem(item_help)
		# add toolbar button
		frm.toolbar.AddLabelTool(ID_HELP, '', \
			wx.Bitmap('res/toolbar/help-browser.png'), \
			shortHelp = 'Help')
		
		frm.toolbar.Realize()		
		
		#insert separator
		menu.AppendSeparator()
		
		# insert about menu
		def about(evt):
			pass
		ID_ABOUT = wx.NewId()
		item_about = wx.MenuItem(menu, ID_ABOUT, '&About...')
		menu.AppendItem(item_about)
		
		mb.Append(menu, '&Help')
		
	mb = wx.MenuBar()
	frm.SetMenuBar(mb)
	
	createFileMenu(mb)
	createToolsMenu(mb)
	createOptionMenu(mb)
	createHelpMenu(mb)
	
def createMainUI(frm):
	from viewpanel import Panel as vp
	from datapanel import Panel as dp
	from callerspanel import Panel as cp
	from calleespanel import Panel as cep
	from uicfg import UIConfig
	
	splitter = wx.SplitterWindow(frm, wx.ID_ANY)
	
	frm.viewpanel = vp(splitter)
	usplitter = wx.SplitterWindow(splitter, wx.ID_ANY, style = wx.BORDER_NONE)
	splitter.SplitVertically(frm.viewpanel, usplitter, UIConfig.inst().getLeftSplitPos(frm))
	
	frm.datapanel = dp(usplitter)
	rsplitter = wx.SplitterWindow(usplitter, wx.ID_ANY, style = wx.BORDER_NONE)
	usplitter.SplitHorizontally(frm.datapanel, rsplitter, UIConfig.inst().getUpSplitPos(frm))
	
	frm.callerspanel = cp(rsplitter)
	frm.calleespanel = cep(rsplitter)
	rsplitter.SplitVertically(frm.callerspanel, frm.calleespanel)
	
	def OnDataSelected(evt):
		idx = evt.GetIndex()
		evt_list = frm.datapanel.listctrl
		idx = int(evt_list.GetItemText(idx))
		fln = frm.model.get_fln_by_idx(idx)
		caky_title = 'Callees of ' + fln
		frm.calleespanel.update(caky_title, frm.model.get_callees(idx))
		frm.callerspanel.update(caky_title, frm.model.get_callers(idx))
		
	frm.datapanel.listctrl.selected_callback = OnDataSelected
	
	def OnDirCtrlSelChanged(evt):
		path = frm.viewpanel.dirctrl.GetFilePath()
		if path:
			frm.OpenFile(path)
	frm.viewpanel.dirctrl.GetTreeCtrl().Bind(wx.EVT_TREE_SEL_CHANGED, \
								OnDirCtrlSelChanged)
	
	def OnSize(evt):
		size = evt.GetSize()
		UIConfig.inst().setWindowSize((size.x, size.y))
		
		splitter.SetSashPosition(UIConfig.inst().getLeftSplitPos(frm))
		usplitter.SetSashPosition(UIConfig.inst().getUpSplitPos(frm))
		rsplitter.SetSashPosition(UIConfig.inst().getRightSplitPos(frm))
		evt.Skip()
	frm.Bind(wx.EVT_SIZE, OnSize, frm)
		
	def onSashPosChanged(evt):
		evtobj = evt.GetEventObject()
		pos = evt.GetSashPosition()
		if evtobj == splitter:
			UIConfig.inst().setLeftSplitPos(frm, pos)
		elif evtobj == usplitter:
			UIConfig.inst().setUpSplitPos(frm, pos)
		elif evtobj == rsplitter:
			UIConfig.inst().setRightSplitPos(frm, pos)
	frm.Bind(wx.EVT_SPLITTER_SASH_POS_CHANGED, onSashPosChanged)
		
	def OnClose(evt):
		UIConfig.inst().setLastDir( \
			os.path.dirname(frm.viewpanel.dirctrl.GetPath()))
		UIConfig.inst().setMaximized( \
			frm.IsMaximized())
		UIConfig.inst().setWindowPos(frm.GetPositionTuple())
		UIConfig.inst().release()
		frm.Destroy()
	frm.Bind(wx.EVT_CLOSE, OnClose, frm)
		
def AddMiscFunc(frm):
	def GetDirCtrlFilePath():
		path = frm.viewpanel.dirctrl.GetFilePath()
		if path:
			return path
		import os
		return os.getcwd()
	frm.GetDirCtrlFilePath = GetDirCtrlFilePath
	
	def SetDirCtrlFilePath(path):
		frm.viewpanel.dirctrl.SetPath(path)
	frm.SetDirCtrlFilePath = SetDirCtrlFilePath	
	
	def OpenFile(path):
		assert path
		print 'Opening %s'%path
		from datamodel import DataModel
		try:
			frm.model = DataModel(path)
		except:
			import sys
			from traceback import print_exc
			print_exc(file = sys.stdout)
			return
		frm.datapanel.listctrl.reset(frm.model.get_data())
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
	
	createToolbar(obj)
	createMenu(obj)
	createStatusbar(obj)
	createMainUI(obj)
	AddMiscFunc(obj)
	
	return obj
	