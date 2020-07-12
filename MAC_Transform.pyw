# -*- coding: utf-8 -*-
"""
开发者：周梦雄
最后更新日期：2020/7/12
"""
import sys
import pyperclip
import re
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QTableWidget,
    QMessageBox,
)
from Ui_mac_transform import *
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp


class MyMainWindow(QMainWindow, Ui_MAC_Transform):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # MAC地址取值范围 ：0-9，A-F
        reg = QRegExp("[0-9A-Fa-f]+")
        MacValidator = QRegExpValidator(reg)
        self.le_mac.setValidator(MacValidator)

        self.statusbar.setStyleSheet(
            "* { color: #00CD00;font-size:30px;font-weight:bold;}")
        self.le_mac.editingFinished.connect(self.GenerateMessage)
        self.show()

    def GenerateMessage(self):
        if len(self.le_mac.text()) != 12:
            QMessageBox.warning(
                self, '错误：', '您输入的MAC地址不是12位，请重新输入！', QMessageBox.Ok)
            self.le_mac.setFocus()
        else:
            try:
                mac_list = re.findall(r'.{2}', self.le_mac.text())
                # 每个字节加0x
                mac_list1 = [('0x'+e) for e in mac_list]
                # 去掉十六进制前面的0
                mac_list2 = [hex(eval(e)) for e in mac_list1]
                # 格式化为数组字符串
                mac_list_str = "[%s,%s,%s,%s,%s,%s]" % tuple(mac_list2)
                self.textBrowser.setText(
                    "MAC地址："+self.le_mac.text()+'\n'+"MAC地址数组:" + mac_list_str)
                pyperclip.copy(mac_list_str)
                self.statusbar.showMessage("报文已复制到剪贴板", 5000)
                self.le_mac.clear()
                with open("mac数据.txt", 'a') as f:
                    f.writelines(mac_list_str + '\n')

            except Exception:
                return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyMainWindow()
    sys.exit(app.exec_())
