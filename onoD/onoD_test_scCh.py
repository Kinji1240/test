import random

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class Test(FloatLayout):
    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)

        btn = Button(text='setting', pos=(650,500), size_hint=(0.1,0.1), on_press=self.click)
        self.add_widget(btn)

    def click(self,btn):
        x = 120
        y = 80
        self.add_widget(Button(text="etc", pos=(x,y), size_hint=(0.1,0.1)))


class Sample(App):
    def build(self):
        return Test()

if __name__ == '__main__':
    Sample().run()