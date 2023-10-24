from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import japanize_kivy

class MorningPiApp(App):
    def build(self):
        # タイトルとサブタイトル用のラベルを作成
        title_label = Label(text="朝の目覚めにこのシステム", font_size=24)
        subtitle_label = Label(text="Morning Pi", font_size=16)
        
        # ボタンを作成
        next_button = Button(text="次へ", size_hint=(None, None))
        
        # クリック時のアクションを設定
        next_button.bind(on_release=self.on_next_button_click)
        
        # レイアウトを作成し、ウィジェットを配置
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)
        layout.add_widget(title_label)
        layout.add_widget(subtitle_label)
        layout.add_widget(next_button)
        
        return layout

    def on_next_button_click(self, instance):
        # 画面遷移を実行
        App.get_running_app().root.current = "initial2"

if __name__ == "__main__":
    sm = ScreenManager()
    sm.add_widget(Screen(name="main"))
    sm.add_widget(Screen(name="initial2"))

    MorningPiApp().run()