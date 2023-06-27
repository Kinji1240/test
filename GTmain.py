from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class RootLayout(GridLayout):

    def __init__(self, **kwargs):
        super(RootLayout, self).__init__(**kwargs)
        #カラム数
        self.cols = 2

    box_layout = BoxLayout()

    button1 = Button(text='Button 1')
    box_layout.add_widget(button1)

    button2 = Button(text='Button 2')
    box_layout.add_widget(button2)
    layout = FloatLayout()
    layout.add_widget(box_layout)

class MyApp(App):
    def build(self):
        return layout