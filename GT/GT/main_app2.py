from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from onoD_1day_weather import WeatherApp
from kivy.factory import Factory

# ファクトリにクラスを登録
Factory.register('WeatherApp', cls=WeatherApp)


kv = '''
FloatLayout:
    

    WeatherApp:

       
    

'''

class ExternalApp(App):
    def build(self):
        return Builder.load_string(kv)
    
if __name__ == '__main__':
    ExternalApp().run()
