from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # 画像を中央に配置
        image = Image(source='image.png', size_hint=(1, 1), allow_stretch=True)
        layout.add_widget(image)

        # ボタンを横方向に2つ配置
        button_layout = BoxLayout(orientation='horizontal')

        button1 = Button(text='Button 1', size_hint=(None, None), size=(300, 300))
        button2 = Button(text='Button 2', size_hint=(None, None), size=(300, 300))

        button_layout.add_widget(button1)
        button_layout.add_widget(button2)

        layout.add_widget(button_layout)

        return layout


if __name__ == '__main__':
    MyApp().run()