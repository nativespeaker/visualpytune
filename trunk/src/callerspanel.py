# -*- coding:utf-8 -*-

import wx

from listctrl import CallListCtrl as DataList
from cakychart import CakyChart
	
import panel
	
class Panel(panel.NotebookPanel):
	def __init__(self, *a, **k):
		super(Panel, self).__init__(*a, **k)
		
		self.listctrl = DataList(self.notebook, wx.ID_ANY, \
			style = wx.LC_REPORT | wx.LC_SINGLE_SEL | wx.BORDER_NONE)
		
		self.BuildPages()
		
	def BuildPages(self):
		self.notebook.AddPage(self.listctrl, 'Callers')
		
	def update(self, caky_title, data):
		from statsmodel import make_calls_data
		self.listctrl.reset(make_calls_data(data))