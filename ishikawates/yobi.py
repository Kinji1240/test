import wx
from anarogu import MyFrame, main as anarogu_main

class MainFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.HORIZONTAL)

        # anarogu.pyの内容をここで呼び出す
        anarogu_main()

        box.Add(panel, 1, flag=wx.ALL|wx.EXPAND)

        self.SetSizerAndFit(box)
        self.SetTitle('Main Frame')

def main():
    app = wx.App()
    frame = MainFrame(None)
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
