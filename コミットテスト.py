from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button
 
class MyApp(App):
    title = 'My Application'
 
    def build(self):
        ''' ビルド時に1回だけ実行される '''
 
        # レイアウトやウィジェットのインスタンス化
        layout_root = PageLayout()
        layout1 = BoxLayout(orientation='horizontal')
        button1 = Button(text='Button1')
        button2 = Button(text='Button2')
        button3 = Button(text='Button3')
 
        # レイアウトにウィジェットを追加
        layout1.add_widget(button2)
        layout1.add_widget(button3)
        layout_root.add_widget(button1)
        layout_root.add_widget(layout1)
 
        return layout_root
 
 
if __name__ == '__main__':
    MyApp().run()