# main_display.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label


from onoD_ok_list.onoD_error import ErrorApp
# WeatherAppをimport
from onoD_ok_list.onoD_weather.onoD_1day_weather import WeatherApp

class MainDisplayApp(App):
    def build(self):
        # レイアウトのインスタンスを作成
        layout = FloatLayout(orientation='vertical')


        # TimeDisplayAppとWeatherAppのインスタンスを作成

        weather_app = WeatherApp()
        error_App = ErrorApp()


        # 各アプリの表示部分を取得

        weather_layout = weather_app.build()
        error_layout = error_App.build()

        weather_layout = Label(weather_layout,pos=(50, 200))

        # 各アプリの座標を指定（例: (100, 200)）

        # レイアウトに各アプリの表示部分を追加

        layout.add_widget(weather_layout)
        layout.add_widget(error_layout)

        return layout

if __name__ == '__main__':
    MainDisplayApp().run()
