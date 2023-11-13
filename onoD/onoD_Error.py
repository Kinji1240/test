from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color
import japanize_kivy

class ErrorApp(App):
    def build(self):
        # エラーの条件を設定
        error_condition = True

        if error_condition:
            # エラーメッセージを生成
            error_message = "エラーが発生しました。"

            # エラー画面を表示するレイアウト
            layout = BoxLayout(orientation='vertical')

            # キャンバスを更新するコールバックを設定
            layout.bind(size=self.update_canvas)

            error_label = Label(text=f'エラーメッセージ: {error_message}', font_size='32sp', color=(1, 0, 0, 1), bold=True)

            # レイアウトにウィジェットを追加
            layout.add_widget(error_label)

            # 初回描画
            self.update_canvas(layout, layout.size)

            return layout
        else:
            # エラーが発生しなかった場合の処理
            return Label(text='正常な画面です。', font_size='20sp', color=(1, 0, 0, 1), bold=True)

    def update_canvas(self, layout, size):
        # 画面全体を縦向きのトラ柄に描画
        with layout.canvas.before:
            layout.canvas.before.clear()
            stripe_width = 40
            for i in range(0, int(size[0]), stripe_width):
                Color(1, 1, 0, 1)  # 黄色の背景
                Rectangle(pos=(layout.x + i, layout.y), size=(stripe_width, size[1]))

                Color(0, 0, 0, 1)  # 黒い縞模様
                Rectangle(pos=(layout.x + i, layout.y), size=(stripe_width / 2, size[1]))

if __name__ == '__main__':
    ErrorApp().run()
