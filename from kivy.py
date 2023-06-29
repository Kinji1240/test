from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button


class RootWidget(BoxLayout):
    item_list = ObjectProperty(None)
    label_text = ObjectProperty(None)
    input_text = ObjectProperty(None)

    def widgets_list_add(self):
        self.item_list.values.append(self.input_text.text)

    def label_text_change(self):
        self.label_text.text = self.item_list.text


class SpinnerButton(Button):
    pass


class MySpinner(Spinner):
    option_cls = ObjectProperty(SpinnerButton)


class TestSpinnerApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    TestSpinnerApp().run()