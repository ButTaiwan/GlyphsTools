#MenuTitle: 將誤用漢字命名的字符改為正確名稱
# -*- coding: utf-8 -*-
#
# (c) But Ko, 2021.
# https://zi-hi.com/
# https://github.com/ButTaiwan/GlyphsTools
# https://www.facebook.com/groups/glyphszhtw
#

from GlyphsApp import Glyphs

for g in Glyphs.font.glyphs:
	if len(g.name) == 1 and ord(g.name) > 255:
		code = ord(g.name[0])
		name = 'uni' + ('%04X' % code)
		if code >= 0x10000: name = 'u' + ('%05X' % code)
		g.name = name