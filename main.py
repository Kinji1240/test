from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner


class MyApp(App):
    def build(self):
        layout = GridLayout(cols=2, spacing=10)

        # ラベル
        label = Label(text='item:', size_hint=(None, None))

        # スピナー
        spinner = Spinner(
            text='item select',
            values=('item1', 'item2', 'item3'),
            size_hint=(None, None)
        )
        spinner.bind(text=self.on_spinner_select)

        layout.add_widget(Label(text='item rei'))
        layout.add_widget(Label())
        layout.add_widget(label)
        layout.add_widget(spinner)

        return layout

    def on_spinner_select(self, spinner, text):
        print('item:', text)


if __name__ == '__main__':
    MyApp().run()