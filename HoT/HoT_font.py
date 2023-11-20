from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

class FontSettingScreen(Screen):
    def __init__(self, **kwargs):
        super(FontSettingScreen, self).__init__(**kwargs)

        self.layout = BoxLayout(orientation='vertical')

        back_button = Button(text='戻る', size_hint=(0.1, 0.1))
        back_button.bind(on_press=self.back_action)
        self.layout.add_widget(back_button)

        self.font_label = Label(text='フォント設定画面', font_size='40sp', size_hint=(1, 0.7))
        self.layout.add_widget(self.font_label)

        # フォント選択用のドロップダウンメニューを作成
        self.font_dropdown = DropDown()
        font_options = ['Default', 'Arial', 'Verdana', 'Times New Roman']  # 任意のフォントリスト
        for font_option in font_options:
            btn = Button(text=font_option, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.change_font(btn.text))
            self.font_dropdown.add_widget(btn)

        font_button = Button(text='フォント選択', size_hint=(0.2, 0.1))
        font_button.bind(on_release=self.font_dropdown.open)
        self.layout.add_widget(font_button)

        # フォント選択メニューが閉じられたときに呼ばれるコールバックを設定
        self.font_dropdown.bind(on_select=lambda instance, x: setattr(font_button, 'text', x))

        Clock.schedule_interval(self.update_time, 1)  # 1秒ごとに時間を更新

        self.add_widget(self.layout)

    def change_font(self, font_name):
        # ユーザーが選択したフォントをラベルに適用
        self.font_label.font_name = font_name

    # 他のメソッドは変更なし
