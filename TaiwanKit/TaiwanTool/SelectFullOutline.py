#MenuTitle: 擴大選取範圍到完整外框
# -*- coding: utf-8 -*-
#
# (c) But Ko, 2021.
# https://zi-hi.com/
# https://github.com/ButTaiwan/GlyphsTools
# https://www.facebook.com/groups/glyphszhtw
#

from GlyphsApp import Glyphs

if Glyphs.font.selectedLayers is not None and len(Glyphs.font.selectedLayers) == 1:
	layer = Glyphs.font.selectedLayers[0]
	nodes = [obj for obj in layer.selection if type(obj)==GSNode]
	for n in nodes:
		path = n.parent
		path.selected = True