#MenuTitle: 檢查重疊或未關閉的路徑
# -*- coding: utf-8 -*-
#
# (c) But Ko, 2021.
# https://zi-hi.com/
# https://github.com/ButTaiwan/GlyphsTools
# https://www.facebook.com/groups/glyphszhtw
#

from __future__ import division, print_function, unicode_literals
from GlyphsApp import Glyphs

opened = ''
overlapped = ''

for g in Glyphs.font.glyphs:
	if not g.export: continue
	
	for lyr in g.layers:
		pcnt = len(lyr.paths)
		for i in range(pcnt):
			if not lyr.paths[i].closed:
				print(u'未關閉', g.name, lyr.name, i+1)
				opened += '/' + g.name
				continue
			baseNode = lyr.paths[i].nodes[0]
			
			for j in range(i+1, pcnt):
				if not lyr.paths[j].closed: continue
				for n in lyr.paths[j].nodes:
					if n == baseNode:
						print(u'重疊', g.name, lyr.name, i+1, j+1)
						overlapped += '/' + g.name

Glyphs.font.newTab(u'未關閉: ' + opened + u'\n重疊 :' + overlapped)