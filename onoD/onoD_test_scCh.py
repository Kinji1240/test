class Postmenu(Screen):

    def searchtitle(self):
        t = self.ids.movietitle.text
        self.title = '+'.join(t.split())

        # refer to another class ここで別スクリーンのIDに格納する
        self.manager.get_screen('post_second').ids.infomation.text = self.title

    pass