import csv
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image

class ImageButtonApp(App):
    def build(self):
        # 画像ボタンを作成
        image_path = r'C:\Users\204012\Desktop\image\click.jpg'
        image_button = Button(background_normal=image_path, background_down=image_path)
        image_button.bind(on_press=self.on_button_press)
        
        return image_button
    
    def on_button_press(self, instance):
        print('ボタンが押されました！')









    watch = 1

    #パスはMAYNSYS\CSVに変更予定
    file_path = r'C:\Users\204012\Desktop\test_git\test\onoD\onoD_Opt.csv'


    # 既存のCSVファイルを読み込む
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)

    # 必要な部分を変更
        data[1][1] = watch

    # 新しいCSVファイルに書き出す
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    
if __name__ == '__main__':
    ImageButtonApp().run()