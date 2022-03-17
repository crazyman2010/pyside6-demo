from PySide6.QtWidgets import QWidget, QMessageBox

from ui.ui_login import Ui_LoginForm


class LoginWindow(QWidget):
    def __init__(self, mainWindow):
        super(LoginWindow, self).__init__()
        # 保存好父窗口，用于登录后显示父窗口
        self.parent = mainWindow
        # 创建ui
        self.ui = Ui_LoginForm()
        self.ui.setupUi(self)
        # 显示自己
        self.show()
        self.closeSplash()

    def slotClickLoginButton(self):
        userName = self.ui.textEdit_userName.toPlainText()
        password = self.ui.textEdit_password.toPlainText()
        QMessageBox.information(self, '登录', '登录成功:' + userName + '/' + password + '，点击确定跳转到主窗口')
        self.close()
        self.parent.show()

    def closeSplash(self):
        try:
            import pyi_splash
            pyi_splash.update_text('UI Loaded ...')
            pyi_splash.close()
        except:
            pass