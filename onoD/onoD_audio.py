from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.slider import Slider
from kivy.core.audio import SoundLoader
import os
import japanize_kivy

class MusicPlayer(App):
    def build(self):
        self.title = "Music Player"
        self.music_player = None  # SoundLoaderオブジェクトをここで初期化
        self.current_song = None

        # レイアウトを作成
        layout = BoxLayout(orientation="vertical", spacing=10)

        # デフォルトの音楽ディレクトリ
        default_music_directory = "C:/Users/204012/Desktop/test_git/test/onoD/onoD_audio_list"

        # ファイル選択ボックス
        file_chooser = FileChooserListView(path=default_music_directory, filters=["*.mp3"])
        file_chooser.bind(on_submit=self.load_song)
        layout.add_widget(file_chooser)

        # 再生、停止ボタン
        play_button = Button(text="再生", on_press=self.play_song)
        stop_button = Button(text="停止", on_press=self.stop_song)
        layout.add_widget(play_button)
        layout.add_widget(stop_button)

        # 音量調整スライダー
        volume_slider = Slider(min=0, max=1, value=1)
        volume_slider.bind(value=self.adjust_volume)
        layout.add_widget(Label(text="音量"))
        layout.add_widget(volume_slider)

        return layout

    def load_song(self, instance, selection, touch):
        if selection:
            self.current_song = selection[0]
            print(f"選択した曲: {self.current_song}")

            if self.music_player:
                self.music_player.unload()  # 他の曲が再生中の場合はアンロード

            self.music_player = SoundLoader.load(self.current_song)
            self.play_song()  # 読み込んだらすぐに再生

    def play_song(self, instance=None):
        try:
            if self.music_player:
                self.music_player.play()
        except Exception as e:
            print(f"エラー: 曲の再生中に問題が発生しました - {e}")

    def stop_song(self, instance=None):
        if self.music_player and self.music_player.state == 'play':
            self.music_player.stop()

    def adjust_volume(self, instance, value):
        if self.music_player:
            self.music_player.volume = value


if __name__ == "__main__":
    MusicPlayer().run()
