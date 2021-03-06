# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\MyProjects\MacTransform\MAC_Transform.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MAC_Transform(object):
    def setupUi(self, MAC_Transform):
        MAC_Transform.setObjectName("MAC_Transform")
        MAC_Transform.resize(589, 300)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        MAC_Transform.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/resources/linux_216px_1210908_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MAC_Transform.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MAC_Transform)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.le_mac = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.le_mac.setFont(font)
        self.le_mac.setMaxLength(10000)
        self.le_mac.setObjectName("le_mac")
        self.gridLayout.addWidget(self.le_mac, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 3, 0, 1, 1)
        MAC_Transform.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MAC_Transform)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 589, 26))
        self.menubar.setObjectName("menubar")
        MAC_Transform.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MAC_Transform)
        self.statusbar.setObjectName("statusbar")
        MAC_Transform.setStatusBar(self.statusbar)

        self.retranslateUi(MAC_Transform)
        QtCore.QMetaObject.connectSlotsByName(MAC_Transform)

    def retranslateUi(self, MAC_Transform):
        _translate = QtCore.QCoreApplication.translate
        MAC_Transform.setWindowTitle(_translate("MAC_Transform", "MAC地址转换工具V1.0"))
        self.label.setText(_translate("MAC_Transform", "MAC地址输入框："))
        self.le_mac.setPlaceholderText(_translate("MAC_Transform", "输入12位MAC地址"))
        self.label_2.setText(_translate("MAC_Transform", "转换后的MAC数组如下:"))
import apprcc_rc
