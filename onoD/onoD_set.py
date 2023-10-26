from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout

import japanize_kivy            # [パターン１] 日本語表示させる japanize_kivy
                                #              モジュールを import する
                                #             (この１行のみで可能)
                                #             (日本語フォント：IPAexゴシックで表示される)


class Test(FloatLayout):
    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)

        btn = Button(text='setting', pos=(650,500), size_hint=(0.1,0.1), on_press=self.click)
        self.add_widget(btn)

    def click(self,btn):
        x = 70
        y = 80
        self.add_widget(Button(text="etc", pos=(x,y), size_hint=(0.1,0.1)))

class FeatureSelectionApp(App):
    def build(self):
        return Test()

if __name__ == '__main__':
    app = FeatureSelectionApp()
    app.run()