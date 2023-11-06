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
        self.spinner= Spinner(text='都道府県選択', values=("北海道","東京","大阪") ,size_hint=(0.5, None))
        spinner =self.spinner
        # データ取得ボタンを作成
        data_button = Button(text='データ取得', size_hint=(None, None), width=100, height=50)
        data_button.bind(on_press=self.data_button_click)
        
        layout.add_widget(self.spinner)
        layout.add_widget(data_button)

        return layout
    
    def data_button_click(self, instance): 
        selected_prefecture = self.spinner.text
        print(f"選択された都道府県: {selected_prefecture}")

        opt_tihou = 0

        if(selected_prefecture == "北海道"):
            opt_tihou = 0
            print(opt_tihou)
        elif(selected_prefecture == "東京"):
            opt_tihou = 12
            print(opt_tihou)
        elif(selected_prefecture == "大阪"):
            opt_tihou = 26
            print(opt_tihou)
           
        
        # ファイルの読み込みと書き込みはここで行います
        file_path = r'C:\Users\204012\Desktop\test_git\test\onoD\onoD_wth_cord.csv'

        # 既存のCSVファイルを読み込む
        with open(file_path, mode='r',encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
        
        for i in range(opt_tihou + 1):
            if(i == opt_tihou ):
                opt_weather_cord = data[opt_tihou][1]
                print(opt_weather_cord)


        # ファイルの読み込みと書き込みはここで行います
        file_path = r'C:\Users\204012\Desktop\test_git\test\onoD\onoD_Opt.csv'

            # 既存のCSVファイルを読み込む
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            data = list(reader)
        
        # 必要な部分を変更
        data[2][1] = opt_weather_cord  # watchを文字列に変換して代入
        
        # 新しいCSVファイルに書き出す
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

if __name__ == '__main__':
    DataDisplayApp().run()
