# main.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # メニューボタン
        menu_button = Button(text='Menu', size_hint=(None, None))
        menu_button.bind(on_release=self.show_menu)

        # ドロップダウンメニュー
        dropdown = DropDown()
        menu_items = ['Item 1', 'Item 2', 'Item 3']
        for item in menu_items:
            btn = Button(text=item, size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn: self.select_item(btn.text))
            dropdown.add_widget(btn)

        layout.add_widget(menu_button)
        dropdown.bind(on_select=lambda instance, x: setattr(menu_button, 'text', x))
        return layout

    def show_menu(self, button):
        dropdown = button.parent.children[0]
        dropdown.open(button)

    def select_item(self, text):
        print('Selected:', text)


if __name__ == '__main__':
    MyApp().run()