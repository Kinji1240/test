# main.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown


class MyApp(App):
    
   
def build(self):
        layout = BoxLayout(orientation=
       
'vertical')

        

       


# メニューボタン
        menu_button = Button(text=
        menu_button = Button(text

        menu_button = Button

        menu

       
'Menu', size_hint=(None, None))
        menu_button.bind(on_release=self.show_menu)

        
        menu_button.bind(on_release=self.show_menu)

       

        menu_button.bind(on_release=self.show_menu)


        menu_button.bind(on_release=self

       
# ドロップダウンメニュー
        dropdown = DropDown()
        menu_items = [
        dropdown = DropDown()
        menu_items =

        dropdown = DropDown()
        menu_items

        dropdown = DropDown()
        menu

        dropdown = DropDown()
       

        dropdown = DropDown()

       
'Item 1', 'Item 2', 'Item 3']
        
       
for item in menu_items:
            btn = Button(text=item, size_hint_y=
            btn = Button(text=item

            btn = Button(text

            btn =

           
None, height=40)
            btn.bind(on_release=
            btn.bind(on_release

            btn

           
lambda btn: self.select_item(btn.text))
            dropdown.add_widget(btn)

        layout.add_widget(menu_button)
        dropdown.bind(on_select=
            dropdown.add_widget(btn)

        layout.add_widget(menu_button)
        dropdown.bind(on_select

            dropdown.add_widget(btn)

        layout.add_widget(menu_button)
        dropdown

            dropdown.add_widget(btn)

        layout.add_widget(menu_button)
       

            dropdown.add_widget(btn)

        layout.add_widget(menu_button)

            dropdown.add_widget(btn)

       

            dropdown.add_widget(btn)


           
lambda instance, x: setattr(menu_button, 'text', x))
        return layout

    

def show_menu(self, button):
        dropdown = button.parent.children[
        dropdown = button
0]
        dropdown.open(button)

    def select_item(self, text):
        
       
print('Selected:', text)


if __name__ == '__main__':
    MyApp().run()

    MyApp().run()
``