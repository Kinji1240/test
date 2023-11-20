import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.label import Label
from random import randint

kivy.require('1.11.1')  # Kivyのバージョンを指定

class TetrisApp(App):
    def build(self):
        self.grid = GridLayout(cols=10, spacing=5)
        self.grid.bind(on_touch_down=self.on_touch)
        self.blocks = [[0] * 10 for _ in range(20)]
        self.current_block = None
        self.score = 0
        self.game_over = False

        self.score_label = Label(text="Score: 0", font_size=20)
        self.grid.add_widget(self.score_label)

        for row in range(20):
            for col in range(10):
                cell = Button(background_normal='', background_color=[0.2, 0.2, 0.2, 1])
                self.grid.add_widget(cell)

        Clock.schedule_interval(self.update, 1.0)
        return self.grid

    def spawn_block(self):
        self.current_block = Block(self)
        self.grid.add_widget(self.current_block)

    def move_block(self, dx, dy):
        if self.current_block:
            new_x = self.current_block.x + dx
            new_y = self.current_block.y + dy
            if self.is_valid_move(new_x, new_y, self.current_block.shape):
                self.current_block.move(dx, dy)
            elif dy != 0:
                self.place_block()

    def place_block(self):
        shape = self.current_block.shape
        for row in range(len(shape)):
            for col in range(len(shape[0])):
                if shape[row][col] == 1:
                    x = self.current_block.x + col
                    y = self.current_block.y - row
                    self.blocks[y][x] = 1
        self.grid.remove_widget(self.current_block)
        self.clear_lines()
        self.spawn_block()

    def is_valid_move(self, x, y, shape):
        for row in range(len(shape)):
            for col in range(len(shape[0])):
                if shape[row][col] == 1:
                    if x + col < 0 or x + col >= 10 or y - row >= 20 or self.blocks[y - row][x + col] == 1:
                        return False
        return True

    def clear_lines(self):
        lines_to_clear = []
        for row in range(len(self.blocks)):
            if all(self.blocks[row]):
                lines_to_clear.append(row)

        for row in lines_to_clear:
            self.grid.remove_widget(self.blocks[row])
            del self.blocks[row]
            self.blocks.insert(0, [0] * 10)

        # スコア更新とゲームオーバー判定
        self.score += len(lines_to_clear) * 100
        self.score_label.text = "Score: " + str(self.score)
        if any(self.blocks[19]):
            self.game_over = True
            self.score_label.text = "Game Over! Score: " + str(self.score)

    def on_touch(self, instance, touch):
        if self.game_over:
            return

        if touch.y < 100:
            return
        if touch.x < Window.width / 2:
            self.move_block(-1, 0)
        else:
            self.move_block(1, 0)

    def update(self, dt):
        if not self.game_over:
            self.move_block(0, -1)

class Block(Button):
    def __init__(self, app, **kwargs):
        super(Block, self).__init__(**kwargs)
        self.app = app
        self.shape = self.get_random_shape()
        self.size_hint = (None, None)
        self.size = (40, 40)
        self.x = 4
        self.y = 19

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def get_random_shape(self):
        shapes = [
            [[1, 1], [1, 1]],
            [[1, 1, 1, 1]],
            [[1, 1, 0], [0, 1, 1]],
            [[0, 1, 1], [1, 1, 0]],
            [[1, 1, 1], [0, 1, 0]],
            [[1, 1, 1], [1, 0, 0]],
            [[1, 1, 1], [0, 0, 1]]
        ]
        return shapes[randint(0, len(shapes) - 1)]

if __name__ == '__main__':
    TetrisApp().run()
