#MenuTitle: 繁中字型符號幫手
# -*- coding: utf-8 -*-
#
# (c) But Ko, 2021.
# https://zi-hi.com/
# https://www.facebook.com/groups/glyphszhtw
#
from vanilla import Window, Button, TextBox, Tabs, PopUpButton, Slider, Group, HorizontalLine
from Foundation import NSPoint
import math
P = NSPoint

class TWSymbolMate:

    def __init__(self):
        self.w = Window((380, 260), u'繁中字型符號幫手 by But Ko')
        #self.w.tabs = Tabs((10, 40, -10, -10), [u'訊息', u'全形英數', u'標號', u'直排', u'其它'])
        self.w.tabs = Tabs((10, 40, -10, -10), [ u'全形英數', u'標號', u'對稱與直排', u'注音調號', u'其它'])

        self.w.text = TextBox((10, 10, 150, 20), u'請選擇要處理的主板：')
        self.w.sel = PopUpButton((160, 10, 120, 20), self.getMasters(), callback=self.onSelectMaster)
        self.w.buttReload = Button((300,  10, -10, 20), u'重整', callback=self.onSelectMaster)

        self.tabEng = self.w.tabs[0]
        self.tabEng.titleText1 = TextBox((10, 10, -10, 20), u'自動生成')
        self.tabEng.buttEng1 = Button((100,  10, -10, 20), u'自動生成全形英數字', callback=self.onButtEng1)
        self.tabEng.buttEng2 = Button((100,  35, -10, 20), u'自動生成羅馬數字', callback=self.onButtEng2)
        self.tabEng.buttEng3 = Button((100,  60, -10, 20), u'自動生成縮寫合字', callback=self.onButtEng3)
        self.tabEng.hr = HorizontalLine((10, 90, -10, 1))
        self.tabEng.titleText2 = TextBox((10, 100, -10, 20), u'自動調整')
        self.tabEng.myButtonVorg = Button((100, 100, -10, 20), u'自動調整VORG位置', callback=self.onButtVorg)
        self.tabEng.noteText = TextBox((100, 125, -10, 60), u'調整直排時的Y軸起始位置，讓字符不要超過上下伸線之間的範圍。\n需要Glyphs版本v2.6.2以上')

        self.tabNum = self.w.tabs[1]
        self.tabNum.hr = HorizontalLine((10, 90, -10, 1))

        self.tabNum.g1 = Group((1, 1, -1, 80))
        self.tabNum.g1.titleText = TextBox((10, 10, -10, 20), u'加圈數字')
        self.tabNum.g1.butt = Button((220, 60, -10, 20), u'生成加圈數字', callback=self.onButtonNum1)
        #self.tabNum.g1.minTag = TextBox((10, 53, 40, 20), '10%', alignment='right')
        #self.tabNum.g1.maxTag = TextBox((150, 53, 40, 20), '100%', alignment='left')
        self.tabNum.g1.tag1 = TextBox((20, 35, 40, 20), u'縮放', alignment='right')
        self.tabNum.g1.val1 = TextBox((65, 35, 40, 20), u'70%', alignment='right')
        self.tabNum.g1.slider1 = Slider((110, 33, 100, 23), minValue=10, maxValue=100, value=70, callback=self.onSlider)
        self.tabNum.g1.tag2 = TextBox((20, 60, 40, 20), u'ΔY', alignment='right')
        self.tabNum.g1.val2 = TextBox((65, 60, 40, 20), u'100', alignment='right')
        self.tabNum.g1.slider2 = Slider((110, 58, 100, 23), minValue=0, maxValue=400, value=100, callback=self.onSlider)

        self.tabNum.g2 = Group((1, 90, -1, 80))
        self.tabNum.g2.titleText = TextBox((10, 10, -10, 20), u'括號數字')
        self.tabNum.g2.butt = Button((220, 60, -10, 20), u'生成括號數字', callback=self.onButtonNum2)
        self.tabNum.g2.tag1 = TextBox((20, 35, 40, 20), u'縮放', alignment='right')
        self.tabNum.g2.val1 = TextBox((65, 35, 40, 20), u'70%', alignment='right')
        self.tabNum.g2.slider1 = Slider((110, 33, 100, 23), minValue=10, maxValue=100, value=70, callback=self.onSlider)
        self.tabNum.g2.tag2 = TextBox((20, 60, 40, 20), u'ΔY', alignment='right')
        self.tabNum.g2.val2 = TextBox((65, 60, 40, 20), u'100', alignment='right')
        self.tabNum.g2.slider2 = Slider((110, 58, 100, 23), minValue=0, maxValue=400, value=100, callback=self.onSlider)

        self.tabVert = self.w.tabs[2]
        self.tabVert.myButtonMark = Button((10, 10, -100, 20), u'標註來源初始字符', callback=self.onButtMark)
        self.tabVert.markMsg = TextBox((20, 35, -10, 20), u'黃色：需要製作的字符／灰色：能自動生成的字符')
        self.tabVert.hr = HorizontalLine((10, 60, -10, 1))
        self.tabVert.myButtonPair = Button((10, 70, -100, 20), u'自動生成對應對稱字符', callback=self.onButtPair)
        self.tabVert.myButtonVert = Button((10, 95, -100, 20), u'自動生成直排符號', callback=self.onButtVert)
        self.tabVert.vertMsg = TextBox((20, 120, -10, -10))

        self.tabTones = self.w.tabs[3]
        self.tabTones.tag1 = TextBox((10, 10, -10, 20), u'注音調號 *尚未完成')
        self.tabTones.buttVertTone = Button((40, 35, 180, 20), u'自動生成直排用調號', callback=self.onButtVertTone)
        self.tabTones.buttVertLight = Button((40, 65, 180, 20), u'調整輕聲直排度量', callback=self.onButtVertLight)
        self.tabTones.noteText = TextBox((230, 65, -10, 20), u'*版本v2.6.2以上', alignment='left')
        self.tabTones.hr = HorizontalLine((10, 100, -10, 1))
        self.tabTones.tag2 = TextBox((10, 110, -10, 20), u'方音（台語注音） *尚未完成')
        self.tabTones.buttVertExts = Button((40, 135, -10, 20), u'自動生成方音符號合成韻尾', callback=self.onButtVertExts)
        self.tabTones.buttVertTone.enable(False)
        self.tabTones.buttVertLight.enable(False)
        self.tabTones.buttVertExts.enable(False)

        self.tabBlock = self.w.tabs[4]
        self.tabBlock.hr = HorizontalLine((10, 115, -10, 1))
        self.tabBlock.titleText1 = TextBox((10, 10, 100, 20), u'表格符號與方塊')
        self.tabBlock.tag1 = TextBox((100, 10, 80, 20), u'表格線寬', alignment='right')
        self.tabBlock.val1 = TextBox((180, 10, 40, 20), u'30', alignment='right')
        self.tabBlock.slider1 = Slider((225, 8, 100, 23), minValue=5, maxValue=200, value=30, callback=self.onSlider)
        self.tabBlock.tag2 = TextBox((100, 35, 80, 20), u'雙線距離', alignment='right')
        self.tabBlock.val2 = TextBox((180, 35, 40, 20), u'100', alignment='right')
        self.tabBlock.slider2 = Slider((225, 33, 100, 23), minValue=5, maxValue=800, value=100, callback=self.onSlider)
        self.tabBlock.tag3 = TextBox((100, 60, 80, 20), u'圓角半徑', alignment='right')
        self.tabBlock.val3 = TextBox((180, 60, 40, 20), u'200', alignment='right')
        self.tabBlock.slider3 = Slider((225, 58, 100, 23), minValue=30, maxValue=400, value=200, callback=self.onSlider)
        self.tabBlock.buttBlock = Button((120, 85, -10, 20), u'自動生成表格符號與方塊', callback=self.onButtBlock)
        self.tabBlock.titleText2 = TextBox((10, 125, 100, 20), u'全形小型標點')

        self.tabBlock.tag9 = TextBox((100, 125, 80, 20), u'縮放率', alignment='right')
        self.tabBlock.val9 = TextBox((180, 125, 40, 20), u'70％', alignment='right')
        self.tabBlock.slider9 = Slider((225, 123, 100, 23), minValue=10, maxValue=100, value=70, callback=self.onSlider)
        self.tabBlock.buttSmall = Button((120, 150, -10, 20), u'自動生成全形小型標點', callback=self.onButtSmall)
        #self.w.myTextBox = TextBox((10, 40, -10, 17), "My Text Box")
        self.w.open()
        self.onSelectMaster(self.w.sel)

        self.glistEng1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
                        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.glistEng2 = {'One': 'I', 'Two': 'I,I', 'Three': 'I,I,I', 'Four': 'I,V', 'Five': 'V', 'Six': 'V,I', 'Seven': 'V,I,I', 'Eight': 'V,I,I,I', 'Nine': 'I,X', 'Ten': 'X',
                        'one': 'i', 'two': 'i,i', 'three': 'i,i,i', 'four': 'i,v', 'five': 'v', 'six': 'v,i', 'seven': 'v,i,i', 'eight': 'v,i,i,i', 'nine': 'i,x', 'ten': 'x'}
        self.glistEng3 = {'logSquare': 'l,o,g', 'lnSquare': 'l,n', 'milSquare': 'm,i,l', 'mmSquare': 'm,m', 'cmSquare': 'c,m',
                        'kmSquare': 'k,m', 'KMSquare': 'K,M', 'msquaredSquare': 'm,twosuperior', 'mgSquare': 'm,g',
                        'kgSquare': 'k,g', 'ccSquare': 'c,c', 'numero': 'N,o,period', 'telephone': 'T,e,l', 'centigrade': 'degree,C', 'fahrenheit': 'degree,F'}
        self.glistNum = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'one_zero',
                        'one_one', 'one_two', 'one_three', 'one_four', 'one_five', 'one_six', 'one_seven', 'one_eight', 'one_nine', 'two_zero',
                        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.glistCopy = {'wavedash': 'asciitilde.full', 'ellipsis': 'midlinehorizontalellipsis', 'colon.full': 'colon.full.vert', 'semicolon.full': 'semicolon.full.vert'} 
        self.glistPair1= {'parenleft.full': 'parenright.full', 'braceleft.full': 'braceright.full', 'bracketleft.full': 'bracketright.full',
                          'tortoiseshellbracketleft': 'tortoiseshellbracketright', 'blacklenticularbracketleft': 'blacklenticularbracketright',
                          'dblanglebracketleft': 'dblanglebracketright', 'anglebracketleft': 'anglebracketright', 
                          'minute': 'primeReversed', 'quotedoubleprime': 'quotedoubleprimeReversed', 
                          'slash.full': 'backslash.full', 'greateroverequal': 'lessoverequal', 'greater.full': 'less.full'}
        self.glistPair2= {'cornerbracketleft': 'cornerbracketright', 'whitecornerbracketleft': 'whitecornerbracketright',
                          'because': 'therefore', 'intersection': 'union',
                          'lowlinecenterline': 'overlinecenterline', 'lowlinedashed': 'overlinedashed', 'overlinedashed': 'overlinewavy',
                          'upBlackTriangle': 'downBlackTriangle', 'upWhiteTriangle': 'downWhiteTriangle'}
        self.glistVert = ['ellipsis', 'emdash', 'underscore.full', 'wavyunderscore', 'parenleft.full', 'parenright.full', 'braceleft.full', 'braceright.full',
						  'tortoiseshellbracketleft', 'tortoiseshellbracketright', 'blacklenticularbracketleft', 'blacklenticularbracketright',
						  'dblanglebracketleft', 'dblanglebracketright', 'anglebracketleft', 'anglebracketright', 'cornerbracketleft',
						  'cornerbracketright', 'whitecornerbracketleft', 'whitecornerbracketright', 'bracketleft.full', 'bracketright.full']
        self.glistVert2 = {'underscorewavy': 'wavyunderscore.vert', 'twodotenleader': 'twodotleader.vert', 'ellipsis': 'ellipsisvertical'}
        self.glistArrow = ['northEastArrow', 'rightArrow', 'southEastArrow', 'downArrow', 'southWestArrow', 'leftArrow', 'northWestArrow']
        self.glistSmall = {'ampersand.full': 'ampersandsmall', 'asterisk.full': 'asterisksmall', 'at.full': 'atsmall', 'colon.full': 'colonsmall',
                           'comma.full': 'commasmall', 'exclam.full': 'exclamsmall', 'numbersign.full': 'numbersignsmall', 'percent.full': 'percentsmall',
                           'period.full': 'periodsmall', 'question.full': 'questionsmall', 'backslash.full': 'reverseslashsmall', 'comma-han': 'commasmall-han', 
                           'semicolon.full': 'semicolonsmall', 'braceleft.full': 'braceleftsmall', 'braceright.full': 'bracerightsmall',
                           'parenleft.full': 'parenleftsmall', 'parenright.full': 'parenrightsmall', 'hyphen.full': 'hyphensmall', 'dollar.full': 'dollarsmall',
                           'tortoiseshellbracketleft': 'tortoiseshellbracketleftsmall', 'tortoiseshellbracketright': 'tortoiseshellbracketrightsmall',
                           'equal.full': 'equalsmall', 'greater.full': 'greatersmall', 'less.full': 'lesssmall', 'plus.full': 'plussmall'}
        self.glistTones = ['secondtonechinese', 'caron', 'fourthtonechinese', 'thirdtoneminnan', 'senventhtoneminnan']
        self.glistVerbs = ['finalp-bopomofo', 'finalk-bopomofo', 'finalt-bopomofo', 'finalh-bopomofo', 'finalg-bopomofo']

        #self.glistVert2 = {'leftArrow': 'upArrow', 'rightArrow': 'downArrow'}

    def getMasters(self):        
        vals = []
        if Glyphs.font != None:
            for m in Glyphs.font.masters: vals.append(m.name)
        return vals

    def getMasterInfo(self):
        if Glyphs.font == None: return None
        for master in Glyphs.font.masters:
            if master.name != self.w.sel.getItem(): continue
            res = {'mId': master.id, 'upm': Glyphs.font.upm, 'asc': master.ascender, 'des': master.descender }
            res['isSquare'] = round(res['asc']-res['des']) == res['upm']
            return res
        return None

    def onSelectMaster(self, sender):
        minfo = self.getMasterInfo()
        if minfo == None: return

        mId = minfo['mId']
        cirG = Glyphs.font.glyphs['empty.circled']
        parG = Glyphs.font.glyphs['empty.paren']
        cirOK = cirG != None and cirG.layers[mId] != None
        parOK = parG != None and parG.layers[mId] != None

        msg = u'UPM: ' + str(minfo['upm']) + u'\n'
        msg += u'上下伸線距離: ' + str(int(minfo['asc'])) + u' - ' + str(int(minfo['des'])) + u' = ' + str(int(minfo['asc']-minfo['des']))
        if minfo['isSquare']:
            self.tabVert.myButtonVert.enable(True)
        else:
            msg += u' - 必須相同！\n'
            self.tabVert.myButtonVert.enable(False)

        self.tabVert.vertMsg.set(msg)

        self.tabNum.g1.titleText.set(u'加圈數字' if cirOK else u'加圈數字：請先定義空圈字符 empty.circled')
        self.tabNum.g1.butt.enable(cirOK)

        self.tabNum.g2.titleText.set(u'括號數字' if parOK else u'括號數字：請先定義空括號字符 empty.paren')
        self.tabNum.g2.butt.enable(parOK)

    def clearGlyphsKeys(self, g):
        g.leftKerningGroup = None
        g.rightKerningGroup = None
        #g.leftKerningKey = None
        #g.rightKerningKey = None
        g.leftMetricsKey = None
        g.rightMetricsKey = None
        g.widthMetricsKey = None

    def createLayer(self, minfo, glyphName, srcList):
        glyph = Glyphs.font.glyphs[glyphName]
        if glyph == None: return

        self.clearGlyphsKeys(glyph)
        masterId = minfo['mId']

        advWidth = 0
        widthList = []
        for srcGlyphName in srcList:
            srcGlyph = Glyphs.font.glyphs[srcGlyphName]
            if srcGlyph == None: return
            srcLayer = srcGlyph.layers[masterId]
            if srcLayer == None: return
            advWidth = advWidth + srcLayer.width
            widthList.append(srcLayer.width)

        if glyph.layers[masterId] != None: del(glyph.layers[masterId])

        layer = GSLayer()
        layer.layerId = masterId
        layer.width = minfo['upm']
        pos = (minfo['upm'] - advWidth)/2
        for i in range(0, len(srcList)):
            comp = GSComponent(srcList[i], NSPoint(pos, 0))
            comp.automaticAlignment = False
            layer.components.append(comp)
            pos = pos + widthList[i]

        glyph.layers[masterId] = layer

        layer.color = None
        bnd = layer.bounds
        #vorg = layer.vertOrigin if layer.vertOrigin else 0
        if bnd.origin.y < minfo['des'] or bnd.origin.y+bnd.size.height > minfo['asc']: layer.color = 1
        if bnd.origin.x < 0 or bnd.origin.x+bnd.size.width > minfo['upm']: layer.color = 0
    
    def createNumGlyph(self, minfo, baseGlyph, scale, deltaY, glyphName, srcList):
        glyph = Glyphs.font.glyphs[glyphName]
        if glyph == None: return
        masterId = minfo['mId']
        self.clearGlyphsKeys(glyph)

        advWidth = 0
        widthList = []
        for srcGlyphName in srcList:
            srcGlyph = Glyphs.font.glyphs[srcGlyphName]
            if srcGlyph == None: return
            srcLayer = srcGlyph.layers[masterId]
            if srcLayer == None: return
            advWidth = advWidth + round(srcLayer.width * scale)
            widthList.append(round(srcLayer.width * scale))

        if glyph.layers[masterId] != None: del(glyph.layers[masterId])
        #scaledWidth = round(advWidth * scale)
        layer = GSLayer()
        layer.layerId = masterId
        layer.width = minfo['upm']
        if baseGlyph:
            comp = GSComponent(baseGlyph, NSPoint(0, 0))
            comp.automaticAlignment = False
            layer.components.append(comp)

        pos = (minfo['upm'] - advWidth)/2
        for i in range(0, len(srcList)):
            comp = GSComponent(srcList[i], NSPoint(pos, deltaY))
            comp.scale = scale
            comp.automaticAlignment = False
            layer.components.append(comp)
            pos = pos + widthList[i]

        glyph.layers[masterId] = layer

        layer.color = None
        bnd = layer.bounds
        #vorg = layer.vertOrigin if layer.vertOrigin else 0
        if bnd.origin.y < minfo['des'] or bnd.origin.y+bnd.size.height > minfo['asc']: layer.color = 1
        if bnd.origin.x < 0 or bnd.origin.x+bnd.size.width > minfo['upm']: layer.color = 0

    def createRotateGlyph(self, minfo, baseGlyph, glyphName, angle, mirror = False):
        glyph = Glyphs.font.glyphs[glyphName]
        if glyph == None: return
        masterId = minfo['mId']
        self.clearGlyphsKeys(glyph)
        if glyph.layers[masterId] != None: del(glyph.layers[masterId])

        offset = NSPoint(0, 0)
        if angle != 0 or mirror:
            oriX = minfo['upm']/2
            oriY = (minfo['asc']-minfo['des'])/2+minfo['des']
            dis = math.sqrt(oriX*oriX+oriY*oriY)
            deg = math.atan2(oriY, -oriX if mirror else oriX)
            rangle = deg+(angle*math.pi / 180.0)
            if rangle:
                rotX = round(math.cos(rangle)*dis)
                rotY = round(math.sin(rangle)*dis)
                offset = NSPoint(oriX-rotX, oriY-rotY)

        layer = GSLayer()
        layer.layerId = masterId
        layer.width = minfo['upm']
        comp = GSComponent(baseGlyph, offset)
        comp.automaticAlignment = False
        comp.rotation = angle # / 180.0 * math.pi
        if mirror: comp.scale = (-1.0, 1)
        layer.components.append(comp)
        glyph.layers[masterId] = layer

        layer.color = None

    def createGlyphByPoints(self, minfo, glyphName, *paths):
        glyph = Glyphs.font.glyphs[glyphName]
        if glyph == None: return
        masterId = minfo['mId']
        self.clearGlyphsKeys(glyph)
        if glyph.layers[masterId] != None: del(glyph.layers[masterId])

        layer = GSLayer()
        layer.layerId = masterId
        layer.width = minfo['upm']
        for pth in paths:
            path = GSPath()
            for pnt in pth:
                path.nodes.append(GSNode(pnt, 'LINE'))
            path.closed = True
            layer.paths.append(path)
        #layer.components.append(comp)
        glyph.layers[masterId] = layer
        layer.color = None
        return layer

    def onButtEng1(self, sender):
        minfo = self.getMasterInfo()
        if minfo == None: return

        for gname in self.glistEng1:
            self.createLayer(minfo, gname+'.full', [gname])

    def onButtEng2(self, sender):
        minfo = self.getMasterInfo()
        if minfo == None: return

        for k, v in self.glistEng2.items():
            self.createLayer(minfo, k+'-roman', v.split(','))

    def onButtEng3(self, sender):
        minfo = self.getMasterInfo()
        if minfo == None: return

        for k, v in self.glistEng3.items():
            self.createLayer(minfo, k, v.split(','))

    def setVorg(self, minfo, glyphName):
        glyph = Glyphs.font.glyphs[glyphName]
        if glyph == None: return
        masterId = minfo['mId']
        layer = glyph.layers[masterId]
        if layer == None: return
        
        mHeight = round(minfo['asc']-minfo['des'])-10
        bnd = layer.bounds
        #vorg = layer.vertOrigin if layer.vertOrigin else 0
        if bnd.size.height <= mHeight and (bnd.origin.y < minfo['des'] or bnd.origin.y+bnd.size.height > minfo['asc']):
            layer.vertOrigin = minfo['des'] - bnd.origin.y + 5

        layer.color = None
        vorg = layer.vertOrigin if layer.vertOrigin else 0
        if bnd.origin.y+vorg < minfo['des'] or bnd.origin.y+bnd.size.height+vorg > minfo['asc']: layer.color = 1
        if bnd.origin.x < 0 or bnd.origin.x+bnd.size.width > minfo['upm']: layer.color = 0

    def onButtVorg(self, sender):
        minfo = self.getMasterInfo()
        if minfo == None: return

        for gname in self.glistEng1:        self.setVorg(minfo, gname+'.full')
        for k, v in self.glistEng2.items(): self.setVorg(minfo, k+'-roman')
        for k, v in self.glistEng3.items(): self.setVorg(minfo, k)

    def onSlider(self, sender):
        val = sender.get()
        if sender == self.tabNum.g1.slider1: self.tabNum.g1.val1.set(str(int(val)) + '%')
        if sender == self.tabNum.g1.slider2: self.tabNum.g1.val2.set(str(int(val)))
        if sender == self.tabNum.g2.slider1: self.tabNum.g2.val1.set(str(int(val)) + '%')
        if sender == self.tabNum.g2.slider2: self.tabNum.g2.val2.set(str(int(val)))
        if sender == self.tabBlock.slider1:    self.tabBlock.val1.set(str(int(val)))
        if sender == self.tabBlock.slider2:    self.tabBlock.val2.set(str(int(val)))
        if sender == self.tabBlock.slider3:    self.tabBlock.val3.set(str(int(val)))
        if sender == self.tabBlock.slider9:    self.tabBlock.val9.set(str(int(val)) + '%')

    def onButtonNum1(self, sender):
        minfo = self.getMasterInfo()
        if minfo == None: return
        base = Glyphs.font.glyphs['empty.circled']
        if base == None: return

        scale = round(self.tabNum.g1.slider1.get())*0.01
        deltaY = round(self.tabNum.g1.slider2.get())
        self.createNumGlyph(minfo, base, scale, deltaY, 'zero.circled', ['zero'])
        for gname in self.glistNum:
            self.createNumGlyph(minfo, base, scale, deltaY, gname+'.circled', gname.split('_'))

    def onButtonNum2(self, sender):
        minfo = self.getMasterInfo()
        if minfo == None: return
        base = Glyphs.font.glyphs['empty.paren']
        if base == None: return

        scale = round(self.tabNum.g2.slider1.get())*0.01
        deltaY = round(self.tabNum.g2.slider2.get())
        for gname in self.glistNum:
            self.createNumGlyph(minfo, base, scale, deltaY, gname+'.paren', gname.split('_'))

    def setGlyphMark(self, minfo, glyphName, color):
        glyph = Glyphs.font.glyphs[glyphName]
        if glyph == None: return
        masterId = minfo['mId']
        self.clearGlyphsKeys(glyph)

        if glyph.layers[masterId] == None:
            layer = GSLayer()
            layer.layerId = masterId
            glyph.layers[masterId] = layer
        glyph.layers[masterId].width = minfo['upm']
        glyph.color = color

    def onButtMark(self, sender):
        minfo = self.getMasterInfo()
        if minfo == None: return

        for gname in self.glistVert:
            self.setGlyphMark(minfo, gname, 3)
            self.setGlyphMark(minfo, gname+'.vert', 10)
        for k, v in self.glistVert2.items():
            self.setGlyphMark(minfo, k, 3)
            self.setGlyphMark(minfo, v, 10)
        self.setGlyphMark(minfo, 'asciitilde.full.vert', 10)
        self.setGlyphMark(minfo, 'wavedash.vert', 10)
        for gname in self.glistArrow:
            self.setGlyphMark(minfo, gname, 10)
        self.setGlyphMark(minfo, 'upArrow', 3)
        for k, v in self.glistPair1.items():
            self.setGlyphMark(minfo, k, 3)
            self.setGlyphMark(minfo, v, 10)
        for k, v in self.glistPair2.items():
            self.setGlyphMark(minfo, k, 3)
            self.setGlyphMark(minfo, v, 10)
        for k, v in self.glistCopy.items():
            self.setGlyphMark(minfo, k, 3)
            self.setGlyphMark(minfo, v, 10)

    def onButtPair(self, sender):
        minfo = self.getMasterInfo()
        if minfo == None: return

        for k, v in self.glistCopy.items():
            self.createRotateGlyph(minfo, k, v, 0)
        for k, v in self.glistPair1.items():
            self.createRotateGlyph(minfo, k, v, 0, True)
        for k, v in self.glistPair2.items():
            self.createRotateGlyph(minfo, k, v, 180)

        deg = 0
        for gname in self.glistArrow:
            deg -= 45
            self.createRotateGlyph(minfo, 'upArrow', gname, deg)

    def onButtVert(self, sender):
        minfo = self.getMasterInfo()
        if minfo == None: return
        #'asciitilde.full', 'wavedash', 

        for gname in self.glistVert:
            self.createRotateGlyph(minfo, gname, gname+'.vert', -90)
        for k, v in self.glistVert2.items():
            self.createRotateGlyph(minfo, k, v, -90)
        self.createRotateGlyph(minfo, 'wavedash', 'wavedash.vert', -90, True)
        self.createRotateGlyph(minfo, 'asciitilde.full', 'asciitilde.full.vert', -90, True)

    def onButtVertTone(selft, sender):
        minfo = self.getMasterInfo()
        if minfo == None: return
        #'asciitilde.full', 'wavedash', 

        for gname in self.glistTones:
            pass

    def onButtVertLight(selft, sender):
        return

    def onButtVertExts(selft, sender):
        return

    def createRoundedCorner(self, minfo, gname, radius, stroke, path):
        layer = self.createGlyphByPoints(minfo, gname, path)

        filter = NSClassFromString("GlyphsFilterRoundCorner")
        layer.clearSelection()
        layer.paths[0].nodes[4].selected = True
        #roundLayer_radius_checkSelection_visualCorrect_grid_(layer, maxRadius, checkSelection, visualCorrect, doRound)
        filter.roundLayer_radius_checkSelection_visualCorrect_grid_(layer, round(radius+stroke/2), True, False, True)
        layer.clearSelection()
        layer.paths[0].nodes[1].selected = True
        filter.roundLayer_radius_checkSelection_visualCorrect_grid_(layer, round(radius-stroke/2), True, False, True)

    def onButtBlock(self, sender):
        minfo = self.getMasterInfo()
        if minfo == None: return

        upm = minfo['upm']
        asc = minfo['asc']
        des = minfo['des']
        hght = asc-des
        
        stroke = int(self.tabBlock.slider1.get())
        dis = int(self.tabBlock.slider2.get())
        radius = int(self.tabBlock.slider3.get())

        # blocks
        self.createGlyphByPoints(minfo, 'fullBlock', [P(0, des), P(upm, des), P(upm, asc), P(0, asc)])
        sn = ['OneEighth', 'OneQuarter', 'ThreeEighths', 'Half', 'FiveEighths', 'ThreeQuarters', 'SevenEighths']
        for n in range(len(sn)):
            y = round(des+hght/8*(n+1))
            x = round(upm/8*(n+1))
            self.createGlyphByPoints(minfo, 'lower'+sn[n]+'Block', [P(0, des), P(upm, des), P(upm, y), P(0, y)])
            self.createGlyphByPoints(minfo, 'left'+('' if n == 3 else sn[n])+'Block', [P(0, des), P(x, des), P(x, asc), P(0, asc)])
        self.createGlyphByPoints(minfo, 'rightOneEighthBlock', [P(round(upm*7/8), des), P(upm, des), P(upm, asc), P(round(upm*7/8), asc)])
        self.createGlyphByPoints(minfo, 'upperOneEighthBlock', [P(0, asc-round(hght/8)), P(upm, asc-round(hght/8)), P(upm, asc), P(0, asc)])

        #triangles
        self.createGlyphByPoints(minfo, 'upperRightBlackTriangle', [P(0, asc), P(upm, des), P(upm, asc)])
        self.createGlyphByPoints(minfo, 'lowerRightBlackTriangle', [P(0, des), P(upm, des), P(upm, asc)])
        self.createGlyphByPoints(minfo, 'lowerLeftBlackTriangle',  [P(0, asc), P(  0, des), P(upm, des)])
        self.createGlyphByPoints(minfo, 'upperLeftBlackTriangle',  [P(0, asc), P(  0, des), P(upm, asc)])

        # table single
        x_1, x11, x21 = round(    ( upm-stroke)/2)       , round(    ( upm-dis)/2)-stroke, round(    ( upm+dis)/2)
        x_2, x12, x22 = round(    ( upm-stroke)/2)+stroke, round(    ( upm-dis)/2)       , round(    ( upm+dis)/2)+stroke
        y_1, y11, y21 = round(des+(hght-stroke)/2)       , round(des+(hght-dis)/2)-stroke, round(des+(hght+dis)/2)
        y_2, y12, y22 = round(des+(hght-stroke)/2)+stroke, round(des+(hght-dis)/2)       , round(des+(hght+dis)/2)+stroke
        self.createGlyphByPoints(minfo, 'boxLightHorizontal', [P(  0, y_1), P(upm, y_1), P(upm, y_2), P(  0, y_2)])
        self.createGlyphByPoints(minfo, 'boxLightVertical',   [P(x_1, des), P(x_2, des), P(x_2, asc), P(x_1, asc)])
        self.createGlyphByPoints(minfo, 'boxLightLeft', [P(  0, y_1), P(x_2, y_1), P(x_2, y_2), P(  0, y_2)])
        for xn, xs in {'Right': [x_1, upm], 'Horizontal': [0, upm], 'Left': [0, x_2]}.items():
            for yn, ys in {'Down': [des, y_2], 'Vertical': [des, asc], 'Up': [y_1, asc]}.items():
                gname = 'boxLight'+yn+'And'+xn
                self.createGlyphByPoints(minfo, gname,
                    [P(xs[0],   y_1), P(xs[1],   y_1), P(xs[1],   y_2), P(xs[0],   y_2)],
                    [P(  x_1, ys[0]), P(  x_2, ys[0]), P(  x_2, ys[1]), P(  x_1, ys[1])])
                if yn != 'Vertical': continue
                gname = 'boxVerticalSingleAnd'+xn+'Double'
                self.createGlyphByPoints(minfo, gname,
                    [P(xs[0],   y11), P(xs[1],   y11), P(xs[1],   y12), P(xs[0],   y12)],
                    [P(xs[0],   y21), P(xs[1],   y21), P(xs[1],   y22), P(xs[0],   y22)],
                    [P(  x_1, ys[0]), P(  x_2, ys[0]), P(  x_2, ys[1]), P(  x_1, ys[1])],)

        # table double
        dbls = {
            'idr': [P(x22, des), P(x22, y11), P(upm, y11), P(upm, y12), P(x21, y12), P(x21, des)],
            'idl': [P(  0, y11), P(x11, y11), P(x11, des), P(x12, des), P(x12, y12), P(  0, y12)],
            'iur': [P(upm, y22), P(x22, y22), P(x22, asc), P(x21, asc), P(x21, y21), P(upm, y21)],
            'iul': [P(x11, asc), P(x11, y22), P(  0, y22), P(  0, y21), P(x12, y21), P(x12, asc)],
            'odr': [P(x12, des), P(x12, y21), P(upm, y21), P(upm, y22), P(x11, y22), P(x11, des)],
            'odl': [P(  0, y21), P(x21, y21), P(x21, des), P(x22, des), P(x22, y22), P(  0, y22)],
            'our': [P(upm, y12), P(x12, y12), P(x12, asc), P(x11, asc), P(x11, y11), P(upm, y11)],
            'oul': [P(x21, asc), P(x21, y12), P(  0, y12), P(  0, y11), P(x22, y11), P(x22, asc)],
            'uh' : [P(  0, y21), P(upm, y21), P(upm, y22), P(  0, y22)],
            'dh' : [P(  0, y11), P(upm, y11), P(upm, y12), P(  0, y12)],
            'lv' : [P(x11, des), P(x12, des), P(x12, asc), P(x11, asc)],
            'rv' : [P(x21, des), P(x22, des), P(x22, asc), P(x21, asc)]
        }

        self.createGlyphByPoints(minfo, 'boxDoubleHorizontal',            dbls['uh'] , dbls['dh'])
        self.createGlyphByPoints(minfo, 'boxDoubleVertical',              dbls['lv'] , dbls['rv'])
        self.createGlyphByPoints(minfo, 'boxDoubleDownAndRight',          dbls['idr'], dbls['odr'])
        self.createGlyphByPoints(minfo, 'boxDoubleDownAndLeft',           dbls['idl'], dbls['odl'])
        self.createGlyphByPoints(minfo, 'boxDoubleUpAndRight',            dbls['iur'], dbls['our'])
        self.createGlyphByPoints(minfo, 'boxDoubleUpAndLeft',             dbls['iul'], dbls['oul'])
        self.createGlyphByPoints(minfo, 'boxDoubleDownAndHorizontal',     dbls['idr'], dbls['idl'], dbls['uh'])
        self.createGlyphByPoints(minfo, 'boxDoubleUpAndHorizontal',       dbls['iur'], dbls['iul'], dbls['dh'])
        self.createGlyphByPoints(minfo, 'boxDoubleVerticalAndRight',      dbls['idr'], dbls['iur'], dbls['lv'])
        self.createGlyphByPoints(minfo, 'boxDoubleVerticalAndLeft',       dbls['idl'], dbls['iul'], dbls['rv'])
        self.createGlyphByPoints(minfo, 'boxDoubleVerticalAndHorizontal', dbls['idr'], dbls['idl'], dbls['iur'], dbls['iul'])
        self.createGlyphByPoints(minfo, 'boxDoubleHorizontal',            dbls['uh'] , dbls['dh'])

        # table cross
        xstrk = round(stroke/math.sqrt(2))
        p1 = [P(0, asc), P(0, asc-xstrk), P(upm-xstrk, des), P(upm, des), P(upm, des+xstrk), P(xstrk, asc)]
        p2 = [P(0, des), P(xstrk, des), P(upm, asc-xstrk), P(upm, asc), P(upm-xstrk, asc), P(0, des+xstrk)]
        self.createGlyphByPoints(minfo, 'boxLightDiagonalUpperLeftToLowerRight', p1)
        self.createGlyphByPoints(minfo, 'boxLightDiagonalUpperRightToLowerLeft', p2)
        self.createGlyphByPoints(minfo, 'boxLightDiagonalCross', p1, p2)

        # table rounded corner
        self.createRoundedCorner(minfo, 'boxLightArcDownAndRight', radius, stroke, [P(x_2, des), P(x_2, y_1), P(upm, y_1), P(upm, y_2), P(x_1, y_2), P(x_1, des)])
        self.createRoundedCorner(minfo, 'boxLightArcDownAndLeft',  radius, stroke, [P(  0, y_1), P(x_1, y_1), P(x_1, des), P(x_2, des), P(x_2, y_2), P(  0, y_2)])
        self.createRoundedCorner(minfo, 'boxLightArcUpAndRight',   radius, stroke, [P(upm, y_2), P(x_2, y_2), P(x_2, asc), P(x_1, asc), P(x_1, y_1), P(upm, y_1)])
        self.createRoundedCorner(minfo, 'boxLightArcUpAndLeft',    radius, stroke, [P(x_1, asc), P(x_1, y_2), P(  0, y_2), P(  0, y_1), P(x_2, y_1), P(x_2, asc)])

    def onButtSmall(self, sender):
        minfo = self.getMasterInfo()
        if minfo == None: return
        scale = round(self.tabBlock.slider9.get())*0.01
        deltaY = int((minfo['asc']-minfo['des'])*(1-scale)/2)

        for k, v in self.glistSmall.items():
            self.createNumGlyph(minfo, None, scale, deltaY, v, [k])
            #if Glyphs.font.glyphs[k] == None: print(k)

TWSymbolMate()