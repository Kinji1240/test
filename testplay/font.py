from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MyKivyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # フォントファイルのパスを指定してフォントを使用石川のデスクトップにあるから無理
        font_name = 'C:/Users/204004/Desktop/font/NikkyouSans-mLKax.ttf'
        
        label = Label(text='Kivyサンプルアプリ', font_name=font_name, font_size=24)
        
        layout.add_widget(label)
        return layout

if __name__ == '__main__':
    MyKivyApp().run()