import kivy
kivy.require('2.1.0') 
import time
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.text import LabelBase
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stencilview import StencilView
from kivy.uix.progressbar import ProgressBar
from kivy.properties import StringProperty
from kivy.clock import Clock
from functools import partial
import random


#Set Kivy Size as Size of Screen
from kivy.core.window import Window
from kivy.config import Config
#Config.set('graphics', 'width', '1024')
#Config.set('graphics', 'height', '600')
Window.size = (1280, 720)

#Enable when PI is connected
#Window.fullscreen = 'auto'


class DashboardApp(App):

    def build(self):
        self.bigLayout = GridLayout(cols=2)
        self.layout = GridLayout(rows=2)
        self.layout.add_widget(Button(text='Hello 1'))
        self.layout.add_widget(Button(text='World 1'))
        self.layout.add_widget(Button(text='Hello 2'))
        self.layout.add_widget(Button(text='World 2'))
        Window.size = (1280, 720)
        print(Window.size)
        return self.layout




if __name__ == '__main__':
    DashboardApp().run()
