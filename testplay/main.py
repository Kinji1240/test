from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.text import LabelBase
from kivy.uix.label import Label

import japanize_kivy            # [パターン１] 日本語表示させる japanize_kivy
                                #              モジュールを import する
                                #             (この１行のみで可能)
                                #             (日本語フォント：IPAexゴシックで表示される)


class TestKivy(App):            # この形式の場合 クラス名がTitle名になる
    def build(self): 
        return Label(text="こんにちは") 

if __name__ == "__main__": 
    TestKivy().run()