# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        if not LoginForm.objectName():
            LoginForm.setObjectName(u"LoginForm")
        LoginForm.resize(400, 300)
        self.verticalLayoutWidget = QWidget(LoginForm)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(70, 40, 271, 179))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.textEdit_userName = QTextEdit(self.verticalLayoutWidget)
        self.textEdit_userName.setObjectName(u"textEdit_userName")
        self.textEdit_userName.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.textEdit_userName)

        self.textEdit_password = QTextEdit(self.verticalLayoutWidget)
        self.textEdit_password.setObjectName(u"textEdit_password")
        self.textEdit_password.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.textEdit_password)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(LoginForm)
        self.pushButton.clicked.connect(LoginForm.slotClickLoginButton)

        QMetaObject.connectSlotsByName(LoginForm)
    # setupUi

    def retranslateUi(self, LoginForm):
        LoginForm.setWindowTitle(QCoreApplication.translate("LoginForm", u"Form", None))
        self.textEdit_userName.setPlaceholderText(QCoreApplication.translate("LoginForm", u"\u7528\u6237\u540d", None))
        self.textEdit_password.setPlaceholderText(QCoreApplication.translate("LoginForm", u"\u5bc6\u7801", None))
        self.pushButton.setText(QCoreApplication.translate("LoginForm", u"\u767b\u5f55", None))
    # retranslateUi

