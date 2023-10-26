from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout

import os
import japanize_kivy            # [パターン１] 日本語表示させる japanize_kivy
                                #              モジュールを import する
                                #             (この１行のみで可能)
                                #             (日本語フォント：IPAexゴシックで表示される)


class Test(FloatLayout):
    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)

        reBtn = Button(text='⇦', pos=(50,50), size_hint=(0.1,0.1), on_press=self.click)
        lytBtn =Button(text='画面レイアウト設定', pos=(300,300), size_hint=(0.1,0.1), on_press=self.click)
        addFncBtn = Button(text='機能追加', pos=(300,200), size_hint=(0.1,0.1), on_press=self.click)
        bckBtn =Button(text='画面レイアウト設定', pos=(300,100), size_hint=(0.1,0.1), on_press=self.click)


        self.add_widget(reBtn)
        self.add_widget(bckBtn)
        self.add_widget(lytBtn)
        self.add_widget(addFncBtn)



    def click(self,reBtn):
        # main2.pyを実行
        os.system("python main2.py")
    
    def click(self,lytBtn):
        # main2.pyを実行
        os.system("python main2.py")

    def click(self,addFncBtn):
        # main2.pyを実行
        os.system("python main2.py")

class FeatureSelectionApp(App):
    def build(self):
        return Test()

if __name__ == '__main__':
    app = FeatureSelectionApp()
    app.run()