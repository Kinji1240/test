from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from GT.gamennsenni2 import MyApp
import japanize_kivy

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        label = Label(text="This is the main app")
        layout.add_widget(label)
        return layout

if __name__ == '__main__':
    app = MainApp()
    app.run()