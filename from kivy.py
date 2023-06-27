from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

class PrefectureDropDownApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10)

        # プルダウンメニューのボタン
        dropdown_button = Button(text='都道府県を選択', size_hint=(None, None), size=(200, 50))
        dropdown_button.bind(on_release=self.show_dropdown)
        layout.add_widget(dropdown_button)

        # プルダウンメニューのコンテンツ
        dropdown = DropDown()
        prefectures = ['北海道', '青森県', '岩手県', '宮城県', '秋田県', '山形県', '福島県', '茨城県', '栃木県', '群馬県',
                       '埼玉県', '千葉県', '東京都', '神奈川県', '新潟県', '富山県', '石川県', '福井県', '山梨県', '長野県',
                       '岐阜県', '静岡県', '愛知県', '三重県', '滋賀県', '京都府', '大阪府', '兵庫県', '奈良県', '和歌山県',
                       '鳥取県', '島根県', '岡山県', '広島県', '山口県', '徳島県', '香川県', '愛媛県', '高知県', '福岡県',
                       '佐賀県', '長崎県', '熊本県', '大分県', '宮崎県', '鹿児島県', '沖縄県']

        button.bind(on_release=dropdown.open)

        layout.add_widget(button)
        return layout
    
    PrefectureDropDownApp().run()