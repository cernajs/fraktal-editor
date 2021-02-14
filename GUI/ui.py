"""
from tkinter import *
from tkinter import ttk

import PySimpleGUI as sg

root = Tk()
root.geometry("700x600")
root.title("Fraktály")

menu = Menu(root)

fractals = Menu(menu, tearoff = 0)
menu.add_cascade(label="fraktály", menu = fractals)
fractals.add_command(label="vločka", command=None)

root.config(menu = menu)
mainloop()
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        MainWindow.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TopFrame = QtWidgets.QFrame(self.centralwidget)
        self.TopFrame.setMaximumSize(QtCore.QSize(1666666, 40))
        self.TopFrame.setStyleSheet("background-color: rgb(57, 57, 57);")
        self.TopFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TopFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TopFrame.setObjectName("TopFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.TopFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toggle = QtWidgets.QFrame(self.TopFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggle.sizePolicy().hasHeightForWidth())
        self.toggle.setSizePolicy(sizePolicy)
        self.toggle.setMaximumSize(QtCore.QSize(70, 40))
        self.toggle.setStyleSheet("background-color: rgb(56, 82, 255);")
        self.toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toggle.setObjectName("toggle")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.toggle)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tgButton = QtWidgets.QPushButton(self.toggle)
        self.tgButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.tgButton.setObjectName("tgButton")
        self.verticalLayout_2.addWidget(self.tgButton)
        self.horizontalLayout.addWidget(self.toggle)
        self.top = QtWidgets.QFrame(self.TopFrame)
        self.top.setStyleSheet("background-color: rgb(33, 39, 37);")
        self.top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top.setObjectName("top")
        self.horizontalLayout.addWidget(self.top)
        self.verticalLayout.addWidget(self.TopFrame)
        self.ContentFrame = QtWidgets.QFrame(self.centralwidget)
        self.ContentFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ContentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ContentFrame.setObjectName("ContentFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.ContentFrame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.leftMenu = QtWidgets.QFrame(self.ContentFrame)
        self.leftMenu.setMinimumSize(QtCore.QSize(70, 0))
        self.leftMenu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.leftMenu.setStyleSheet("background-color: rgb(33, 39, 37);")
        self.leftMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftMenu.setObjectName("leftMenu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.leftMenu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.top_menus = QtWidgets.QFrame(self.leftMenu)
        self.top_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_menus.setObjectName("top_menus")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.top_menus)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.top_menus)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(56, 82, 255);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_4.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.top_menus)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(56, 82, 255);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.pushButton_1 = QtWidgets.QPushButton(self.top_menus)
        self.pushButton_1.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_1.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(56, 82, 255);\n"
"}")
        self.pushButton_1.setObjectName("pushButton_1")
        self.verticalLayout_4.addWidget(self.pushButton_1)
        self.verticalLayout_3.addWidget(self.top_menus, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.leftMenu)
        self.fraktalView = QtWidgets.QFrame(self.ContentFrame)
        self.fraktalView.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraktalView.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraktalView.setObjectName("fraktalView")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.fraktalView)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.p_widget = QtWidgets.QStackedWidget(self.fraktalView)
        self.p_widget.setObjectName("p_widget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.p_widget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.p_widget.addWidget(self.page_2)
        self.verticalLayout_5.addWidget(self.p_widget)
        self.horizontalLayout_2.addWidget(self.fraktalView)
        self.verticalLayout.addWidget(self.ContentFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tgButton.setText(_translate("MainWindow", "Open"))
        self.pushButton_3.setText(_translate("MainWindow", "L_System"))
        self.pushButton_2.setText(_translate("MainWindow", "L_System"))
        self.pushButton_1.setText(_translate("MainWindow", "L_System"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
