# encoding: utf-8

###########################################################################################################
#
#
#	Reporter Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Reporter
#
#
###########################################################################################################


from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *

class ShowCharacterBackground(ReporterPlugin):

	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': 'Character Background',
			'zh-Hant': '背景字',
			'zh-Hant-TW': '背景字',
			'zh-Hans': '背景字',
			'zh': '背景字',
			'ja': '背景文字',
		})

		self.currentIndex = None

		self.generalContextMenus = [{
			'name': Glyphs.localize({
				'en': 'Switch to next font',
				'zh-Hant': '切換下個背景字型',
				'zh-Hant-TW': '切換下個背景字型',
				'zh-Hans': '切換下个背景字体',
				'zh': '切換下個背景字型',
				'ja': '次の背景フォントで表示',
			}), 
			'action': self.switchFont
		}]

	@objc.python_method
	def background(self, layer):
		try:
			chr = None
			glyph = layer.parent
			chr = glyph.glyphInfo.unicharString()
			if not chr and "." in glyph.name:
				baseName = glyph.name[:glyph.name.find('.')]
				chr = Glyphs.glyphInfoForName(baseName).unicharString()
			
			if not chr and "." in glyph.name:
				nameWithoutSuffix = glyph.name[:glyph.name.find(".")]
				glyphInfo = Glyphs.glyphInfoForName(nameWithoutSuffix)
				character = glyphInfo.unicharString()
		except:
			pass

		if not chr: return
			
		master = layer.associatedFontMaster()
		fonts = self.getFonts()
		if fonts is None: return
		if self.currentIndex is None or self.currentIndex > len(fonts)-1: self.currentIndex = 0

		try:	
			font = fonts[self.currentIndex]
			fontAttr = {
				NSFontAttributeName: font[0],
				NSForegroundColorAttributeName: self.getColor()
			}
			displayText = NSAttributedString.alloc().initWithString_attributes_('%s' % chr, fontAttr)
			displayText.drawAtPoint_alignment_(NSPoint(0, master.descender + font[1]), 0)
		except Exception as e:
			print(e)
			import traceback
			print(traceback.format_exc())

	def switchFont(self):
		if self.currentIndex is None: return
		self.currentIndex += 1
		Glyphs.redraw()

	@objc.python_method
	def getFonts(self):
		cfgStr = Glyphs.font.customParameters["CharBG Fonts"]
		if not cfgStr: return None

		fonts = []
		cfgs = cfgStr.split(';')
		for fstr in cfgs:
			tmp = fstr.split(',')
			fn = tmp[0].strip()
			offy = int(tmp[1].strip()) if len(tmp) > 1 else 0
			font = NSFont.fontWithName_size_(fn, Glyphs.font.upm)
			if font: fonts.append((font, offy))

		if len(fonts) > 0: return fonts
		return None

		
	@objc.python_method
	def getColor(self):
		colorHex = Glyphs.font.customParameters["CharBG Color"]

		try:
			r = int(colorHex[0:2], 16) / 255.0
			g = int(colorHex[2:4], 16) / 255.0
			b = int(colorHex[4:6], 16) / 255.0
			alpha = int(colorHex[6:8], 16) / 255.0 if len(colorHex) == 8 else 0.15
			return NSColor.colorWithRed_green_blue_alpha_(r, g, b, alpha)
		except:
			return NSColor.colorWithRed_green_blue_alpha_(0.1, 0.8, 0.6, 0.15)

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
