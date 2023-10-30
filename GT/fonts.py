import csv
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.text import LabelBase

def load_fonts_from_csv(file_path):
    fonts = {}
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            fonts[int(row['id'])] = {
                'name': row['name'],
                'path': row['path']
            }
    return fonts

class MyApp(App):
    def build(self):
        fonts = load_fonts_from_csv('fonts.csv')

        # Kivyにフォントを登録する
        for font_id, font_data in fonts.items():
            LabelBase.register(name=font_data['name'], fn_regular=font_data['path'])

        # 例: 数値が1の場合、ボタンのフォントを"Roboto"に設定する
        #     数値が2の場合、ボタンのフォントを"Arial"に設定する
        font_choice = 1  # ここで1または2を選択
        font_name = fonts[font_choice]['name']
        
        btn = Button(text="Hello, Kivy!", font_name=font_name, font_size=24)
        return btn

if __name__ == '__main__':
    MyApp().run()