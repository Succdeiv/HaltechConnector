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
from kivy.logger import Logger, LOG_LEVELS
from kivy.clock import Clock
from functools import partial
import can
import cantools
import os
#############
#Enable Canbus
os.system('sudo ifconfig can0 down') 
os.system('sudo ip link set can0 type can bitrate 1000000')
os.system('sudo ifconfig can0 up')
#Enable Fullscreen
from kivy.core.window import Window
#Enable when PI is connected
Window.fullscreen = 'auto'
#Load DBC File
dbc = cantools.database.load_file('/home/john/HaltechConnector/pythonProgram/Haltech-Broadcast-V2.35.0.dbc')
#Set Logging Mode 
Logger.setLevel(LOG_LEVELS["info"])
filters = [
    {"can_id": 0x360, "can_mask": 0x7FF}, #Filter for RPM
    {"can_id": 0x361, "can_mask": 0x7FF}, #Filter for Oil Pressure
    {"can_id": 0x372, "can_mask": 0x7FF}, #Filter for Voltage
    {"can_id": 0x3E0, "can_mask": 0x7FF}, #Filter for Coolant
]


class DashboardApp(App):
    def build(self):
        #Enable CanBus
        self.can_bus = can.interface.Bus('can0', bustype='socketcan', can_filters=filters)
        self.can_bus.RECV_LOGGING_LEVEL=0
        Clock.schedule_interval(partial(self.getCanMessages, self), 0.01)
        Clock.schedule_interval(partial(self.updateRPM, self), 0.05)
        Clock.schedule_interval(partial(self.drawGauges, self), 0.05)
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
        self.lastOilLabel = self.oilLabel
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
    
    def drawOilPressure(self, *largs):
        #Oil Pressure will be assigned by getCanMessages function
        #Get Raw Input of the Haltech 
        rawSignal = self.oilPressure
        #Convert To PSI
        actualSignal = abs(round(rawSignal/6.895))

        #Now define the range as 0-32
        #PSI Range - Take Actual Signal and Divide by 9. 
        psiInt = round(actualSignal/2.8)
        if psiInt >= 32:
            psiInt = 32
        self.oilPressureBar = Image(source='s2kGaugeBars/s2k_' + str(psiInt) + '.png', pos = self.oilPos)
        #Removes Old Oil Graph
        if self.lastOilWidget:
            self.layout.remove_widget(self.lastOilWidget)
        self.lastOilWidget = self.oilPressureBar
        #print(self.oilPressure)

        #Define Label for Displaying Raw Output
        self.layout.add_widget(self.oilPressureBar)
        self.oilLabel = Label(text = "{} PSI".format(str(actualSignal)) , pos=(-480, -50), font_size=30, font_name='rpmFont')

        #This line Removes the Last RPM Signal From the Dashboard
        self.layout.remove_widget(self.lastOilLabel)
        #This line sets the last current readout to self.last, so it can be removed
        self.lastOilLabel = self.oilLabel
        #This line Re-adds the widget to the screen
        self.layout.add_widget(self.oilLabel)

    def drawVoltage(self, *largs):

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
            #Check Last 100 Messages, Get Latest Signals - This may need to be updated Later
            for i in range(100):
                message = self.can_bus.recv(timeout = 0)
                if message != None:
                    if message.arbitration_id == 864:
                        self.rpmSpeed = dbc.decode_message(message.arbitration_id, message.data).get('Engine_Speed')
                        #print(dbc.decode_message(message.arbitration_id, message.data).get('Engine_Speed'))
                    elif message.arbitration_id == 865:
                        self.oilPressure = dbc.decode_message(message.arbitration_id, message.data).get('Oil_Pressure')
                        #print(dbc.decode_message(message.arbitration_id, message.data).get('Oil_Pressure'))
                    elif message.arbitration_id == 992:
                        self.waterTemp = dbc.decode_message(message.arbitration_id, message.data).get('Coolant_Temperature')
                    elif message.arbitration_id == 882:
                        self.voltage = dbc.decode_message(message.arbitration_id, message.data).get('Battery_Voltage')

                else:
                    print("No Message on Can0")


    def colourByValue(self, green, yellow, value):
        if value < green or value == green:
            return "32F30F"
        elif value > green and value < yellow or value == yellow:
            return "F99A09"
        elif value > yellow:
            return "FE0000"



if __name__ == '__main__':
    DashboardApp().run()
