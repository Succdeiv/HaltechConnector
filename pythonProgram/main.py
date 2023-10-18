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
import can
import cantools
import random
import os

#############
import psutil
#############
process = psutil.Process()
#############
#Enable Canbus
os.system('sudo ifconfig can0 down') 
os.system('sudo ip link set can0 type can bitrate 1000000')
os.system('sudo ifconfig can0 up')
#Enable Fullscreen
from kivy.core.window import Window
#Enable when PI is connected
Window.fullscreen = 'auto'
dbc = cantools.database.load_file('/home/john/HaltechConnector/pythonProgram/Haltech-Broadcast-V2.35.0.dbc')

class DashboardApp(App):
    def build(self):
        #Enable CanBus
        self.can_bus = can.interface.Bus('can0', bustype='socketcan')
        #self.firstID = dbc.get_message_by_name('ID_0x360')
        #self.canMessage = can.Message(arbitration_id=self.firstID)
        #Set Clocks to Update Information as Required
        Clock.schedule_interval(partial(self.getCanMessages, self), 0.001)
        #Clock.schedule_interval(partial(self.updateRPM, self), 0.01)
        #Clock.schedule_interval(partial(self.drawGauges, self), .25)
        #Define Layout and Gauges
        LabelBase.register(name='rpmFont', fn_regular='RPM.ttf')
        #RPM Scale
        self.rpmSpeed = 0
        Window.size = (1280, 720)
        self.layout = FloatLayout(size=Window.size)
        self.rpmScale = Image(source='images/barScale.png', size=(1600, 200), pos_hint={'x':0, 'y':.36})
        self.layout.add_widget(self.rpmScale)
        self.numberColour = "32F30F"
        #RPM Gradient
        self.rpmStencil = StencilView(size_hint=(None,None), size=(1000, 199), pos=(0,487))
        self.rpmBar = Image(source='images/gradBar.png', size=(1600, 199), pos=(-170,487))
        self.rpmStencil.add_widget(self.rpmBar)
        self.layout.add_widget(self.rpmStencil)
        self.rpmReadout = Label(text = "RPM : "+ str(self.rpmSpeed),pos=(-290,140), font_size=50, font_name='rpmFont')
        self.layout.add_widget(self.rpmReadout)
        self.rpmUpDown = "up"

        #self.rpmStencil.width=5000 * 0.1543
        self.last = self.rpmReadout
        ##Define Oil Pressure
        #Define Gauge
        self.oilPressure = 0 
        self.oilPos = (-480, 50)
        self.oilOutline = Image(source='images/oilOutline.png', pos=self.oilPos)
        self.layout.add_widget(self.oilOutline)
        self.lastOilWidget = None
        #Define Icon
        self.oilLogoPos = tuple(map(lambda i, j: i + j, self.oilPos, (0, 280)))
        self.oilIcon = Image(source='images/oilPresIcon.png', size_hint_y= None, height= 35, pos=self.oilLogoPos)
        self.layout.add_widget(self.oilIcon)
        #Define Label 
        self.oilLabel = Label(text = "45.5 PSI" , pos=(-480, -50), font_size=30, font_name='rpmFont')
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
        self.voltagePos = (480, 50)
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
        self.rpmStencil.width = self.rpmSpeed * 0.1543
        self.rpmColour = self.colourByValue(3500, 5500, self.rpmSpeed)
        #This line creates the label with the text RPM + The current speed of the Engine
        self.rpmReadout = Label(text = 'RPM : ' + '[color={}]'.format(self.rpmColour) + str(self.rpmSpeed) + '[/color]',pos=(-375,180), font_size=50, font_name='rpmFont', markup=True)
        #This line Removes the Last RPM Signal From the Dashboard
        self.layout.remove_widget(self.last)
        #This line sets the last current readout to self.last, so it can be removed
        self.last = self.rpmReadout
        #This line Re-adds the widget to the screen
        self.layout.add_widget(self.rpmReadout)
        print(process.memory_info().rss)  # in bytes

    
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

    def getCanMessages(self, *largs):
        self.message = self.can_bus.recv(timeout=0.2)
        if self.message != None:
            if self.message.arbitration_id == 864:
                self.rpmSpeed = dbc.decode_message(self.message.arbitration_id, self.message.data).get('Engine_Speed')
                #print(dbc.decode_message(self.message.arbitration_id, self.message.data).get('Engine_Speed'))

            elif self.message.arbitration_id == 865:
                #self.oilPressure = dbc.decode_message(self.message.arbitration_id, self.message.data).get('Oil_Pressure')
                print(dbc.decode_message(self.message.arbitration_id, self.message.data).get('Oil_Pressure'))

                print(self.message.data)
        else:
            print("message = None")
        #print(dbc.decode_message(self.message.arbitration_id, self.message.data))
        #messageInfo = dbc.decode_message(self.message.arbitration_id, self.message.data)
        #if messageInfo.arbitration_id == 'ID_0x360':
        #    self.rpmSpeed = messageInfo.get("Engine_Speed")



    def colourByValue(self, green, yellow, value):
        if value < green or value == green:
            return "32F30F"
        elif value > green and value < yellow or value == yellow:
            return "F99A09"
        elif value > yellow:
            return "FE0000"



if __name__ == '__main__':
    DashboardApp().run()
