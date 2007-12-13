# -*- coding: utf-8 -*- 

import sys, os

def GenCfgPath(*a):
	exe = sys.executable
	if exe.endswith('vpt.exe'):
		return os.path.join(os.path.dirname(sys.executable), *a)
	else:
		return os.path.join(*a)