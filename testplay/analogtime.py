from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg

app = QtGui.QApplication([])

# ウィンドウを作成
win = pg.GraphicsLayoutWidget(show=True, title='Analog clock')
init_window_size = 800
win.resize(init_window_size, init_window_size)
pg.setConfigOptions(antialias=True)

# ウィンドウを表示
win.show()

# メインループを実行
if __name__ == '__main__':
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()