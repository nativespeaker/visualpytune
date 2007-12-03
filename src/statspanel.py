# -*- coding:utf-8 -*-

import wx

from listctrl import FilterStatsListCtrl as DataList
from callgraph import CallGraph
from filterpanel import FilterPanel
import panel
	
class StatsPanel(wx.Panel):
	def __init__(self, *a, **k):
		super(StatsPanel, self).__init__(*a, **k)
		
		self.listctrl = DataList(self, wx.ID_ANY, \
			style = wx.LC_REPORT | wx.LC_SINGLE_SEL | wx.NO_BORDER)
		
		self.filterpanel = FilterPanel(self, wx.ID_ANY)
		self.filterpanel.ok_callback = self.listctrl.OnFilter
		self.filterpanel.all_callback = self.listctrl.OnAll
		
		vbox = wx.BoxSizer(wx.VERTICAL)
		vbox.Add(self.filterpanel, \
			flag = wx.TOP | wx.LEFT | wx.RIGHT | wx.EXPAND | wx.ALIGN_TOP)
		vbox.Add(self.listctrl, \
			proportion = 1, \
			flag = wx.ALL | wx.EXPAND | wx.ALIGN_BOTTOM)
		
		self.SetSizer(vbox)
		
class Panel(panel.NotebookPanel):
	def __init__(self, *a, **k):
		super(Panel, self).__init__(*a, **k)
		
		self.statspanel = StatsPanel(self.notebook, wx.ID_ANY)
		self.listctrl = self.statspanel.listctrl

		self.chartctrl = CallGraph(self.notebook, wx.ID_ANY)
		
		self.BuildPages()
		
	def BuildPages(self):
		self.notebook.AddPage(self.statspanel, 'Stats')
		self.notebook.AddPage(self.chartctrl, 'Call Graph')