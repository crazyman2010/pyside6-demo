from PySide6.QtWidgets import QMainWindow

from src.login import LoginWindow
from ui.ui_main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # 创建ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 创建登录类
        self.loginWindow = LoginWindow(self)
        # 隐藏自己
        self.hide()
