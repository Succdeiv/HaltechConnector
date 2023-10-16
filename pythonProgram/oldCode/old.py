    ##This stupid piece of shit code only runs once, to render the bars into their correct locations.
    #  When they're meant to be built, you can use self.layout.add_widget(self.<barname><x>) to add them to the screen.
    #  When they need to be removed, you can use self.layout.remove_widget(self.<barname><x>) to remove them from the screen.
    def buildBars(self, *largs):
        print("Rendering Bars")

        self.oPBar1 = Image(source='gaugebars/1.png',
                        pos = tuple(map(lambda i, j: i + j, self.oilPos, (-100, 241))),
                        size_hint_y= None,
                        height= 19)
        
        self.oPBar2 = Image(source='gaugebars/2.png',
                        pos = tuple(map(lambda i, j: i + j, self.oilPos, (-97, 252))),
                        size_hint_y= None,
                        height= 22)
        self.oPBar3 = Image(source='gaugebars/3.png',
                        pos = tuple(map(lambda i, j: i + j, self.oilPos, (-92, 262))),
                        size_hint_y= None,
                        height= 24.5)
        self.oPBar4 = Image(source='gaugebars/4.png',
                        pos = tuple(map(lambda i, j: i + j, self.oilPos, (-85, 272))),
                        size_hint_y= None,
                        height= 28)
        self.oPBar5 = Image(source='gaugebars/5.png',
                        pos = tuple(map(lambda i, j: i + j, self.oilPos, (-76, 280))),
                        size_hint_y= None,
                        height= 31)
        self.oPBar6 = Image(source='gaugebars/6.png',
                        pos = tuple(map(lambda i, j: i + j, self.oilPos, (-66, 289))),
                        size_hint_y= None,
                        height= 33)
        self.oPBar7 = Image(source='gaugebars/7.png',
                        pos = tuple(map(lambda i, j: i + j, self.oilPos, (-55, 296))),
                        size_hint_y= None,
                        height= 35)
        self.oPBar8 = Image(source='gaugebars/8.png',
                        pos = tuple(map(lambda i, j: i + j, self.oilPos, (-44, 303))),
                        size_hint_y= None,
                        height= 35)
        self.oPBar9 = Image(source='gaugebars/9.png',
                        pos = tuple(map(lambda i, j: i + j, self.oilPos, (-30, 307))),
                        size_hint_y= None,
                        height= 35)
        self.oPBar10 = Image(source='gaugebars/10.png',
                        pos = tuple(map(lambda i, j: i + j, self.oilPos, (-15, 310))),
                        size_hint_y= None,
                        height= 35)

        #-------------#MIDDLE BAR#-------------#
        self.oPBar11 = Image(source='gaugebars/11.png',
                        pos = tuple(map(lambda i, j: i + j, self.oilPos, (0, 310))),
                        size_hint_y= None,
                        height= 35)
        #-------------#MIDDLE BAR#-------------#
        ##Going down otherside

        self.oPBar12 = Image(source='gaugebars/12.png',
                        pos = tuple(map(lambda i, j: i + j, self.oilPos, (15, 310))),
                        size_hint_y= None,
                        height= 35)

        self.oPBar13 = Image(source='gaugebars/13.png',
                        pos = tuple(map(lambda i, j: i + j, self.oilPos, (30, 307))),
                        size_hint_y= None,
                        height= 35)
        self.oPBar14 = Image(source='gaugebars/14.png',
                        pos = tuple(map(lambda i, j: i + j, self.oilPos, (44, 303))),
                        size_hint_y= None,
                        height= 35)
        self.oPBar15 = Image(source='gaugebars/15.png',
                        pos = tuple(map(lambda i, j: i + j, self.oilPos, (55, 296))),
                        size_hint_y= None,
                        height= 35)
        self.oPBar16 = Image(source='gaugebars/16.png',
                        pos = tuple(map(lambda i, j: i + j, self.oilPos, (66, 288))),
                        size_hint_y= None,
                        height= 33)
        self.oPBar17 = Image(source='gaugebars/17.png',
                        pos = tuple(map(lambda i, j: i + j, self.oilPos, (76, 280))),
                        size_hint_y= None,
                        height= 31)
        self.oPBar18 = Image(source='gaugebars/18.png',
                        pos = tuple(map(lambda i, j: i + j, self.oilPos, (85, 272))),
                        size_hint_y= None,
                        height= 28)
        self.oPBar19 = Image(source='gaugebars/19.png',
                        pos = tuple(map(lambda i, j: i + j, self.oilPos, (92, 262))),
                        size_hint_y= None,
                        height= 24.5)
        self.oPBar20 = Image(source='gaugebars/20.png',
                        pos = tuple(map(lambda i, j: i + j, self.oilPos, (97, 252))),
                        size_hint_y= None,
                        height= 22)
        self.oPBar21 = Image(source='gaugebars/21.png',
                        pos = tuple(map(lambda i, j: i + j, self.oilPos, (100, 241))),
                        size_hint_y= None,
                        height= 19)
        self.oPRing = Image(source='gaugebars/outsideRing.png',
                            pos = tuple(map(lambda i, j: i + j, self.oilPos, (0, 248))),
                            size_hint_y = None,
                            height = 98)
        self.layout.add_widget(self.oPRing)
        


        ##SECOND GAUGE

        
        self.wTBar1 = Image(source='gaugebars/1.png',
                        pos = tuple(map(lambda i, j: i + j, self.waterPos, (-100, 241))),
                        size_hint_y= None,
                        height= 19)
        
        self.wTBar2 = Image(source='gaugebars/2.png',
                        pos = tuple(map(lambda i, j: i + j, self.waterPos, (-97, 252))),
                        size_hint_y= None,
                        height= 22)
        self.wTBar3 = Image(source='gaugebars/3.png',
                        pos = tuple(map(lambda i, j: i + j, self.waterPos, (-92, 262))),
                        size_hint_y= None,
                        height= 24.5)
        self.wTBar4 = Image(source='gaugebars/4.png',
                        pos = tuple(map(lambda i, j: i + j, self.waterPos, (-85, 272))),
                        size_hint_y= None,
                        height= 28)
        self.wTBar5 = Image(source='gaugebars/5.png',
                        pos = tuple(map(lambda i, j: i + j, self.waterPos, (-76, 280))),
                        size_hint_y= None,
                        height= 31)
        self.wTBar6 = Image(source='gaugebars/6.png',
                        pos = tuple(map(lambda i, j: i + j, self.waterPos, (-66, 289))),
                        size_hint_y= None,
                        height= 33)
        self.wTBar7 = Image(source='gaugebars/7.png',
                        pos = tuple(map(lambda i, j: i + j, self.waterPos, (-55, 296))),
                        size_hint_y= None,
                        height= 35)
        self.wTBar8 = Image(source='gaugebars/8.png',
                        pos = tuple(map(lambda i, j: i + j, self.waterPos, (-44, 303))),
                        size_hint_y= None,
                        height= 35)
        self.wTBar9 = Image(source='gaugebars/9.png',
                        pos = tuple(map(lambda i, j: i + j, self.waterPos, (-30, 307))),
                        size_hint_y= None,
                        height= 35)
        self.wTBar10 = Image(source='gaugebars/10.png',
                        pos = tuple(map(lambda i, j: i + j, self.waterPos, (-15, 310))),
                        size_hint_y= None,
                        height= 35)

        #-------------#MIDDLE BAR#-------------#
        self.wTBar11 = Image(source='gaugebars/11.png',
                        pos = tuple(map(lambda i, j: i + j, self.waterPos, (0, 310))),
                        size_hint_y= None,
                        height= 35)
        #-------------#MIDDLE BAR#-------------#
        ##Going down otherside

        self.wTBar12 = Image(source='gaugebars/12.png',
                        pos = tuple(map(lambda i, j: i + j, self.waterPos, (15, 310))),
                        size_hint_y= None,
                        height= 35)

        self.wTBar13 = Image(source='gaugebars/13.png',
                        pos = tuple(map(lambda i, j: i + j, self.waterPos, (30, 307))),
                        size_hint_y= None,
                        height= 35)
        self.wTBar14 = Image(source='gaugebars/14.png',
                        pos = tuple(map(lambda i, j: i + j, self.waterPos, (44, 303))),
                        size_hint_y= None,
                        height= 35)
        self.wTBar15 = Image(source='gaugebars/15.png',
                        pos = tuple(map(lambda i, j: i + j, self.waterPos, (55, 296))),
                        size_hint_y= None,
                        height= 35)
        self.wTBar16 = Image(source='gaugebars/16.png',
                        pos = tuple(map(lambda i, j: i + j, self.waterPos, (66, 288))),
                        size_hint_y= None,
                        height= 33)
        self.wTBar17 = Image(source='gaugebars/17.png',
                        pos = tuple(map(lambda i, j: i + j, self.waterPos, (76, 280))),
                        size_hint_y= None,
                        height= 31)
        self.wTBar18 = Image(source='gaugebars/18.png',
                        pos = tuple(map(lambda i, j: i + j, self.waterPos, (85, 272))),
                        size_hint_y= None,
                        height= 28)
        self.wTBar19 = Image(source='gaugebars/19.png',
                        pos = tuple(map(lambda i, j: i + j, self.waterPos, (92, 262))),
                        size_hint_y= None,
                        height= 24.5)
        self.wTBar20 = Image(source='gaugebars/20.png',
                        pos = tuple(map(lambda i, j: i + j, self.waterPos, (97, 252))),
                        size_hint_y= None,
                        height= 22)
        self.wTBar21 = Image(source='gaugebars/21.png',
                        pos = tuple(map(lambda i, j: i + j, self.waterPos, (100, 241))),
                        size_hint_y= None,
                        height= 19)
        self.wTRing = Image(source='gaugebars/outsideRing.png',
                            pos = tuple(map(lambda i, j: i + j, self.waterPos, (0, 248))),
                            size_hint_y = None,
                            height = 98)
        self.layout.add_widget(self.wTRing)

        #-------------------THIRD GAUGE--------------------------

        self.vBar1 = Image(source='gaugebars/1.png',
                        pos = tuple(map(lambda i, j: i + j, self.voltagePos, (-100, 241))),
                        size_hint_y= None,
                        height= 19)
        
        self.vBar2 = Image(source='gaugebars/2.png',
                        pos = tuple(map(lambda i, j: i + j, self.voltagePos, (-97, 252))),
                        size_hint_y= None,
                        height= 22)
        self.vBar3 = Image(source='gaugebars/3.png',
                        pos = tuple(map(lambda i, j: i + j, self.voltagePos, (-92, 262))),
                        size_hint_y= None,
                        height= 24.5)
        self.vBar4 = Image(source='gaugebars/4.png',
                        pos = tuple(map(lambda i, j: i + j, self.voltagePos, (-85, 272))),
                        size_hint_y= None,
                        height= 28)
        self.vBar5 = Image(source='gaugebars/5.png',
                        pos = tuple(map(lambda i, j: i + j, self.voltagePos, (-76, 280))),
                        size_hint_y= None,
                        height= 31)
        self.vBar6 = Image(source='gaugebars/6.png',
                        pos = tuple(map(lambda i, j: i + j, self.voltagePos, (-66, 289))),
                        size_hint_y= None,
                        height= 33)
        self.vBar7 = Image(source='gaugebars/7.png',
                        pos = tuple(map(lambda i, j: i + j, self.voltagePos, (-55, 296))),
                        size_hint_y= None,
                        height= 35)
        self.vBar8 = Image(source='gaugebars/8.png',
                        pos = tuple(map(lambda i, j: i + j, self.voltagePos, (-44, 303))),
                        size_hint_y= None,
                        height= 35)
        self.vBar9 = Image(source='gaugebars/9.png',
                        pos = tuple(map(lambda i, j: i + j, self.voltagePos, (-30, 307))),
                        size_hint_y= None,
                        height= 35)
        self.vBar10 = Image(source='gaugebars/10.png',
                        pos = tuple(map(lambda i, j: i + j, self.voltagePos, (-15, 310))),
                        size_hint_y= None,
                        height= 35)

        #-------------#MIDDLE BAR#-------------#
        self.vBar11 = Image(source='gaugebars/11.png',
                        pos = tuple(map(lambda i, j: i + j, self.voltagePos, (0, 310))),
                        size_hint_y= None,
                        height= 35)
        #-------------#MIDDLE BAR#-------------#
        ##Going down otherside

        self.vBar12 = Image(source='gaugebars/12.png',
                        pos = tuple(map(lambda i, j: i + j, self.voltagePos, (15, 310))),
                        size_hint_y= None,
                        height= 35)

        self.vBar13 = Image(source='gaugebars/13.png',
                        pos = tuple(map(lambda i, j: i + j, self.voltagePos, (30, 307))),
                        size_hint_y= None,
                        height= 35)
        self.vBar14 = Image(source='gaugebars/14.png',
                        pos = tuple(map(lambda i, j: i + j, self.voltagePos, (44, 303))),
                        size_hint_y= None,
                        height= 35)
        self.vBar15 = Image(source='gaugebars/15.png',
                        pos = tuple(map(lambda i, j: i + j, self.voltagePos, (55, 296))),
                        size_hint_y= None,
                        height= 35)
        self.vBar16 = Image(source='gaugebars/16.png',
                        pos = tuple(map(lambda i, j: i + j, self.voltagePos, (66, 288))),
                        size_hint_y= None,
                        height= 33)
        self.vBar17 = Image(source='gaugebars/17.png',
                        pos = tuple(map(lambda i, j: i + j, self.voltagePos, (76, 280))),
                        size_hint_y= None,
                        height= 31)
        self.vBar18 = Image(source='gaugebars/18.png',
                        pos = tuple(map(lambda i, j: i + j, self.voltagePos, (85, 272))),
                        size_hint_y= None,
                        height= 28)
        self.vBar19 = Image(source='gaugebars/19.png',
                        pos = tuple(map(lambda i, j: i + j, self.voltagePos, (92, 262))),
                        size_hint_y= None,
                        height= 24.5)
        self.vBar20 = Image(source='gaugebars/20.png',
                        pos = tuple(map(lambda i, j: i + j, self.voltagePos, (97, 252))),
                        size_hint_y= None,
                        height= 22)
        self.vBar21 = Image(source='gaugebars/21.png',
                        pos = tuple(map(lambda i, j: i + j, self.voltagePos, (100, 241))),
                        size_hint_y= None,
                        height= 19)
        self.vRing = Image(source='gaugebars/outsideRing.png',
                            pos = tuple(map(lambda i, j: i + j, self.voltagePos, (0, 248))),
                            size_hint_y = None,
                            height = 98)
        self.layout.add_widget(self.vRing)

        self.s2kBar = Image(source='s2kGaugeBars/s2k_' + str(32) + '.png',
                            pos = tuple(map(lambda i, j: i + j, self.voltagePos, (0, 0))))
        self.layout.add_widget(self.s2kBar)