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

