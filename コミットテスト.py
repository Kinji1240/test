from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class WidgetScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(WidgetScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # ラベル
        label = Label(text='Hello, World!', font_size=24)
        self.add_widget(label)
        
        # ボタン
        button = Button(text='Click Me!', size_hint=(None, None), size=(150, 50))
        button.bind(on_press=self.on_button_press)
        self.add_widget(button)
    
    def on_button_press(self, instance):
        print('Button Clicked!')


class WidgetApp(App):
    def build(self):
        return WidgetScreen()


if __name__ == '__main__':
    WidgetApp().run()
    