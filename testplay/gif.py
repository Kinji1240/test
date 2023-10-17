from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
from PIL import Image as PILImage
from kivy.core.image import Image as CoreImage

class MyKivyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 背景GIFの読み込み
        gif_file = 'C:/Users/204004/Desktop/font/cat.gif'
        self.gif_images = PILImage.open(gif_file)
        self.gif_images.seek(0)  # 最初のフレームを表示

        # 背景画像のサイズをウィンドウサイズに合わせる
        self.background = Rectangle(texture=self._get_texture(), pos=(0, 0), size=Window.size)

        layout.add_widget(self.background)

        # アニメーションの開始
        Clock.schedule_interval(self.animate_background, 1/30.0)  # 30 FPSで更新

        return layout

    def _get_texture(self):
        # GifImageFileをKivyのテクスチャに変換
        pil_image = self.gif_images
        pil_image = pil_image.convert('RGBA')  # RGBA形式に変換
        data = pil_image.tobytes()
        texture = CoreImage(data, ext='png', mipmap=True).texture
        return texture

    def animate_background(self, dt):
        try:
            self.gif_images.seek(self.gif_images.tell() + 1)
            self.background.texture = self._get_texture()
        except EOFError:
            self.gif_images.seek(0)
            self.background.texture = self._get_texture()

if __name__ == '__main__':
    MyKivyApp().run()