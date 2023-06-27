from kivy.config import Config

Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')

from kivy.app import App

class MyApp(App):
    def build(self):
        # アプリケーションのビルドロジックを記述します
        pass

if __name__ == '__main__':
    MyApp().run()
    