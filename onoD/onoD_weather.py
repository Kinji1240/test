from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
import csv
import japanize_kivy

class DataDisplayApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # プルダウンメニューを作成
        self.spinner = Spinner(text='都道府県選択', values=("北海道","東京","大阪") ,size_hint=(0.5, None))
        self.spinner.bind(on_text=self.on_spinner_select)

        # データ取得ボタンを作成
        data_button = Button(text='データ取得', size_hint=(None, None), width=100, height=50)

        layout.add_widget(self.spinner)
        layout.add_widget(data_button)

        return layout
    
    def on_spinner_select(self, instance, value):
        # プルダウンメニューの選択が変更された際の処理
        if value == "北海道":
            result = self.find_number_in_csv('onoD_wth_cord.csv', 0)
            print(result)


    def find_number_in_csv(self,file_path, target_number):
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                for cell in row:
                    if cell == str(target_number):
                        # ファイルの読み込みと書き込みはここで行います
                        file_path = r'C:\Users\204012\Desktop\test_git\test\onoD\onoD_Opt.csv'
        
                        # 既存のCSVファイルを読み込む
                        with open(file_path, mode='r') as file:
                            reader = csv.reader(file)
                            data = list(reader)
        
                        # 必要な部分を変更
                        data[2][1] = str(target_number)  # target_numberを文字列に変換して代入
        
                        # 新しいCSVファイルに書き出す
                        with open(file_path, mode='w', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerows(data)

                        return True

        return False  # 数字が見つからなかった場合、Falseを返す

if __name__ == '__main__':
    DataDisplayApp().run()
