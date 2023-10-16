import kivy
kivy.require('2.1.0') 
import time
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.text import LabelBase
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stencilview import StencilView
from kivy.uix.progressbar import ProgressBar
from kivy.properties import StringProperty
#test
from kivy.clock import Clock
from functools import partial
import random


#Set Kivy Size as Size of Screen
from kivy.core.window import Window
from kivy.config import Config
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '600')
Window.size = (1024, 600)

#Enable when PI is connected
#Window.fullscreen = 'auto'


class DashboardApp(App):

    def build(self):
        #Set Clocks to Update Information as Required
        Clock.schedule_interval(partial(self.updateRPM, self), 0.01)
        Clock.schedule_interval(partial(self.drawGauges, self), .25)
        #Define Layout and Gauges
        LabelBase.register(name='rpmFont', fn_regular='RPM.ttf')
        #RPM Scale
        self.rpmSpeed = 0
        self.layout = FloatLayout(size=(1024, 600))
        self.rpmScale = Image(source='images/barScale.png', size=(1024, 200), pos_hint={'x':0, 'y':.36})
        self.layout.add_widget(self.rpmScale)
        self.numberColour = "32F30F"

        #RPM Gradient
        self.rpmStencil = StencilView(size_hint=(None,None), size=(1000, 200), pos=(0,390))
        self.rpmBar = Image(source='images/gradBar.png', size=(1000, 200), pos=(0,390))
        self.rpmStencil.add_widget(self.rpmBar)
        self.rpmStencil.width=0
        self.layout.add_widget(self.rpmStencil)
        self.rpmReadout = Label(text = "RPM : "+ str(self.rpmSpeed),pos=(-290,140), font_size=50, font_name='rpmFont')
        self.layout.add_widget(self.rpmReadout)
        self.last = self.rpmReadout
        ##Define Oil Pressure
        #Define Gauge
        self.oilPressure = 0 
        self.oilPos = (-350, 50)
        self.oilOutline = Image(source='images/oilOutline.png', pos=self.oilPos)
        self.layout.add_widget(self.oilOutline)
        self.lastOilWidget = None
        #Define Icon
        self.oilLogoPos = tuple(map(lambda i, j: i + j, self.oilPos, (0, 220)))
        self.oilIcon = Image(source='images/oilPresIcon.png', size_hint_y= None, height= 35, pos=self.oilLogoPos)
        self.layout.add_widget(self.oilIcon)
        #Define Label 
        self.oilLabel = Label(text = "45.5 KPa" , pos=(-350, -45), font_size=30, font_name='rpmFont')
        self.layout.add_widget(self.oilLabel)
        ##Define Water Temp
        #Define Gauge 
        self.lastWaterWidget = None
        self.waterTemp = 0
        self.waterPos = (0, 50)
        self.waterOutline = Image(source='images/coolantOutline.png', pos=self.waterPos)
        self.layout.add_widget(self.waterOutline)
        #Define Label
        self.waterLabel = Label(text = "98.8° C" , pos=(0, -45), font_size=30, font_name='rpmFont')
        self.layout.add_widget(self.waterLabel)
        #Voltage
        self.voltage = 0
        self.lastVoltageWidget = None
        self.voltagePos = (350, 50)
        self.voltageOutline = Image(source='images/batteryOutline.png', pos=self.voltagePos)
        self.layout.add_widget(self.voltageOutline)
        self.voltageLabel = self.lastVoltageLabel = Label(text = "11.89 V" , pos=(350, -45), font_size=30, font_name='rpmFont')
        self.layout.add_widget(self.voltageLabel)

        return self.layout
    
    def drawGauges(self, *largs):
        self.drawOilPressure(self)
        self.drawVoltage(self)
        self.drawWater(self)

    def updateRPM(self, *largs):
        #Testing Code - This needs to be Replaced with CANBUS signal for RPM.

        #This Code Resets the RPM Speed - Test Only 
        if self.rpmSpeed > 8250:
            self.rpmSpeed = 0
        #Increase by 1 increment
        self.rpmSpeed += 1
        #This updates the length of the bar - RPM * 0.1234 translates engine speed to bar length
        self.rpmStencil.width = self.rpmSpeed * 0.1234
        
        #Add Colours to the RPM Gauge
        #Green = 32F30F
        #Orange = F99A09
        #Red = FE0000
        self.rpmColour = self.colourByValue(3500, 5500, self.rpmSpeed)
        #if self.rpmSpeed < 3500:
        #    self.numberColour = "32F30F"
        #elif self.rpmSpeed > 3500 and self.rpmSpeed < 6000:
       #     self.numberColour = "F99A09"
       # else:
        #    self.numberColour = "FE0000"

        #This line creates the label with the text RPM + The current speed of the Engine
        #ToDo - Add Better Font
        self.rpmReadout = Label(text = 'RPM : ' + '[color={}]'.format(self.rpmColour) + str(self.rpmSpeed) + '[/color]',pos=(-270,150), font_size=50, font_name='rpmFont', markup=True)

        #This line Removes the Last RPM Signal From the Dashboard
        self.layout.remove_widget(self.last)

        #This line sets the last current readout to self.last, so it can be removed
        self.last = self.rpmReadout

        #This line Re-adds the widget to the screen
        self.layout.add_widget(self.rpmReadout)
    
    def drawOilPressure(self, *largs):
        #TEST CODE
        #Needs to be replaced with Canbus input for Oil Pressure
        #This is Raw Signal - Bar goes from 0 - 32.

        #Resets Oil Pressure (Test Code)
        if self.oilPressure == 32:
            self.oilPressure = 0
        #Iterates Oil pressure
        self.oilPressure += 1
        #Builds and image - takes value between 0 and 32.
        self.oilPressureBar = Image(source='s2kGaugeBars/s2k_' + str(self.oilPressure) + '.png',
             pos = self.oilPos)
        #Removes Old Oil Graph
        if self.lastOilWidget:
            self.layout.remove_widget(self.lastOilWidget)
        self.lastOilWidget = self.oilPressureBar
        #print(self.oilPressure)
        self.layout.add_widget(self.oilPressureBar)

    def drawVoltage(self, *largs):
        #TEST CODE
        #Needs to be replaced with Canbus input for Voltage
        #This is Raw Signal - Bar goes from 0 - 32.
        self.voltage = 24
        #Builds and image - takes value between 0 and 32.
        self.voltageBar = Image(source='s2kGaugeBars/s2k_' + str(self.voltage) + '.png',
             pos = self.voltagePos)
        #Removes Old Voltage Graph
        if self.lastVoltageWidget:
            print("Removing Old Widget")
            self.layout.remove_widget(self.lastVoltageWidget)
        self.lastVoltageWidget = self.voltageBar
        self.layout.add_widget(self.voltageBar)

    def drawWater(self, *largs):
        #TEST CODE
        #Needs to be replaced with Canbus input for Voltage
        #This is Raw Signal - Bar goes from 0 - 32.
        self.waterTemp = 28
        #Builds and image - takes value between 0 and 32.
        self.waterBar = Image(source='s2kGaugeBars/s2k_' + str(self.waterTemp) + '.png',
             pos = self.waterPos)
        #Removes Old Water Graph
        if self.lastWaterWidget:
            self.layout.remove_widget(self.lastWaterWidget)
        self.lastWaterWidget = self.waterBar
        #print(self.oilPressure)
        self.layout.add_widget(self.waterBar)


    def colourByValue(self, green, yellow, value):
        if value < green or value == green:
            return "32F30F"
        elif value > green and value < yellow or value == yellow:
            return "F99A09"
        elif value > yellow:
            return "FE0000"


if __name__ == '__main__':
    DashboardApp().run()
