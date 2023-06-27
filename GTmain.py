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

        layout = BoxLayout(orientation='vertical')
        button1 = Button(text='1', font_size=150)
        button2 = Button(text='Button2')

        layout.add_widget(button1)
        layout.add_widget(button2)

        layout.add_widget(button1)
        layout.add_widget(button1)

        layout.add_widget(button1)
        layout.add_widget(button1)

class MainApp(App):
    def build(self):

        return RootLayout()

if __name__ == "__main__":
    MainApp().run()