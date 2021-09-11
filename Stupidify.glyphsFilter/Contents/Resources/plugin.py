# encoding: utf-8

###########################################################################################################
#
#
#	Filter without dialog plug-in
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Filter%20without%20Dialog
#
#
###########################################################################################################

from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *

class Stupidify(FilterWithoutDialog):
	
	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': 'Stupidify',
			'jp': 'ふざける',
			'zh-Hant': '耍笨',
			'zh-Hant-TW': '耍笨',
			'zh': '耍笨',
		})

	@objc.python_method
	def getCover(self, script, masterId):
		coverGlyph = None
		if script is not None:
			coverGlyph = Glyphs.font.glyphs['_stupid.' + script]
		if coverGlyph is None:
			coverGlyph = Glyphs.font.glyphs['_stupid.any']
		if coverGlyph is None:
			return None
		
		coverLayer = coverGlyph.layers[masterId]
		if coverLayer is None: return None

		coverMask = None
		for layer in coverGlyph.layers:
			if layer.associatedMasterId == masterId and layer.name == 'Mask': coverMask = layer
		
		return (coverLayer, coverMask)


	@objc.python_method
	def filter(self, layer, inEditView, customParameters):
		script = layer.parent.script
		masterId = layer.associatedMasterId

		cover = self.getCover(script, masterId)
		if cover is None: return

		pathOptr = NSClassFromString("GSPathOperator")

		#		subtractRect = self.rectPath(minX, minY, maxX, maxY)
		#		subtractPaths = NSMutableArray.alloc().initWithObject_(subtractRect)
		layerPaths = NSMutableArray.alloc().init() # should work with simply ...layer.shapes
		for shape in layer.copyDecomposedLayer().shapes:
			layerPaths.addObject_(shape)

		if cover[1] is not None and cover[1].shapes is not None and len(cover[1].shapes) > 0:
			maskPaths = NSMutableArray.alloc().init()
			for shape in cover[1].copyDecomposedLayer().shapes:
				maskPaths.addObject_(shape)
			if pathOptr.subtractPaths_from_error_(maskPaths, layerPaths, None):
				layer.shapes = layerPaths
				# if len(layerPaths) > 0: layer.shapes = layerPaths

		for shape in cover[0].copyDecomposedLayer().shapes:
			layer.shapes.append(shape)



	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
