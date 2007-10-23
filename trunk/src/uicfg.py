# -*- coding:utf-8 -*-
	
import ConfigParser
from ConfigParser import SafeConfigParser as Parser

from singleton import Singleton

default_file = """
[window]
maximize=True
size=800,600
pos=200,200
[split]
left_split=0.3
up_split=0.67
right_split=-0.35
[dirctrl]
dir=
"""

WINDOW = 'window'
MAXIMIZE = 'maximize'
SIZE = 'size'
POS = 'pos'

SPLIT = 'split'
LEFT_SPLIT = 'left_split'
UP_SPLIT = 'up_split'
RIGHT_SPLIT = 'right_split'

DIRCTRL = 'dirctrl'
DIR = 'dir'

sep = ','

def modified_decorator(func):
	def setter(obj, *a, **k):
		obj.modified = True
		ret = func(obj, *a, **k)
		return ret
	return setter

def str2list(s):
	return map(lambda x: x.strip(), s.split(sep))

class UIConfig(Singleton):
	def __init__(self):
		self.__init()
		self.modified = False
		
		print 'UIConfig.__init__'
		
	def __init(self):
		self.file = self.opencfg('option/ui.cfg')
		self.cfg = Parser()
		self.cfg.readfp(self.file)
		self.file.close()
		
	def __setdefault(self):
		f = open(self.fn, 'w')
		f.write(default_file)
		f.close()
		
	def opencfg(self, fn):
		self.fn = fn
		try:
			return open(fn, 'r')
		except IOError:
			self.__setdefault()
			return open(fn, 'r')
		
	def release(self):
		if self.modified:
			f = open(self.fn, 'w')
			self.cfg.write(f)
			f.close()
			
	def setDefault(self):
		self.__setdefault()
		self.__init()
			
	def getMaximized(self):
		return self.cfg.get(WINDOW, MAXIMIZE).lower() == 'true'
		
	@modified_decorator
	def setMaximized(self, value):
		self.cfg.set(WINDOW, MAXIMIZE, str(bool(value)))
		
	def getWindowSize(self):
		return map(int, str2list(self.cfg.get(WINDOW, SIZE)))
		
	@modified_decorator
	def setWindowSize(self, value):
		self.cfg.set(WINDOW, SIZE, \
			sep.join(map(str, value)))
			
	def getWindowPos(self):
		return map(int, str2list(self.cfg.get(WINDOW, POS)))
		
	@modified_decorator
	def setWindowPos(self, value):
		self.cfg.set(WINDOW, POS, \
			sep.join(map(str, value)))
		
	def getLeftSplitPos(self, wnd):
		w, h = wnd.GetClientSizeTuple()
		return int( w * \
			self.cfg.getfloat(SPLIT, LEFT_SPLIT))
			
	@modified_decorator
	def setLeftSplitPos(self, wnd, sash_pos):
		w, h = wnd.GetClientSizeTuple()
		self.cfg.set(SPLIT, LEFT_SPLIT, \
			'%.2f'%(sash_pos / float(w), ))
			
	def getUpSplitPos(self, wnd):
		w, h = wnd.GetClientSizeTuple()
		return int( h * \
			self.cfg.getfloat(SPLIT, UP_SPLIT))
			
	@modified_decorator
	def setUpSplitPos(self, wnd, sash_pos):
		w, h = wnd.GetClientSizeTuple()
		self.cfg.set(SPLIT, UP_SPLIT, \
			'%.2f'%(sash_pos / float(h)))
			
	def getRightSplitPos(self, wnd):
		w, h = wnd.GetClientSizeTuple()
		return int( w * \
			self.cfg.getfloat(SPLIT, RIGHT_SPLIT))
			
	@modified_decorator
	def setRightSplitPos(self, wnd, sash_pos):
		w, h = wnd.GetClientSizeTuple()
		self.cfg.set(SPLIT, RIGHT_SPLIT, \
			'%.2f'%(float(sash_pos) / w))
			
	def getLastDir(self):
		return self.cfg.get(DIRCTRL, DIR)
		
	@modified_decorator
	def setLastDir(self, value):
		self.cfg.set(DIRCTRL, DIR, value)
#		
#	def getLastFile(self):
#		return self.cfg.get(DIRCTRL, FILE)
#		
#	@modified_decorator
#	def setLastFile(self, value):
#		self.cfg.set(DIRCTRL, FILE, value)
		
inst = UIConfig()
		
if __name__ == '__main__':
	op = UIConfig.inst
	
	print op.getLastDir()
	op.setLastDir('C:/')
	print op.getLastDir()
	op.release()