# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'U:/extensions/studioTools/python/arxShotgunVersionCheck/ui.ui'
#
# Created: Wed Mar 18 00:48:29 2015
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ShotgunVersionWindow(object):
    def setupUi(self, ShotgunVersionWindow):
        ShotgunVersionWindow.setObjectName("ShotgunVersionWindow")
        ShotgunVersionWindow.resize(500, 660)
        ShotgunVersionWindow.setMinimumSize(QtCore.QSize(500, 660))
        self.centralwidget = QtGui.QWidget(ShotgunVersionWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.logo_label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.logo_label.setFont(font)
        self.logo_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.logo_label.setObjectName("logo_label")
        self.verticalLayout_4.addWidget(self.logo_label)
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtGui.QFrame.Box)
        self.frame_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.project_comboBox = QtGui.QComboBox(self.frame_2)
        self.project_comboBox.setObjectName("project_comboBox")
        self.horizontalLayout.addWidget(self.project_comboBox)
        self.getData_pushButton = QtGui.QPushButton(self.frame_2)
        self.getData_pushButton.setMinimumSize(QtCore.QSize(140, 0))
        self.getData_pushButton.setObjectName("getData_pushButton")
        self.horizontalLayout.addWidget(self.getData_pushButton)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.frame = QtGui.QFrame(self.frame_2)
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.status_label = QtGui.QLabel(self.frame)
        self.status_label.setText("")
        self.status_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.status_label.setObjectName("status_label")
        self.horizontalLayout_2.addWidget(self.status_label)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.shotgun_tableWidget = QtGui.QTableWidget(self.frame)
        self.shotgun_tableWidget.setObjectName("shotgun_tableWidget")
        self.shotgun_tableWidget.setColumnCount(9)
        self.shotgun_tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.shotgun_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.shotgun_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.shotgun_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.shotgun_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.shotgun_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.shotgun_tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.shotgun_tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.shotgun_tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.shotgun_tableWidget.setHorizontalHeaderItem(8, item)
        self.verticalLayout_2.addWidget(self.shotgun_tableWidget)
        self.all_checkBox = QtGui.QCheckBox(self.frame)
        self.all_checkBox.setObjectName("all_checkBox")
        self.verticalLayout_2.addWidget(self.all_checkBox)
        self.update_pushButton = QtGui.QPushButton(self.frame)
        self.update_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.update_pushButton.setObjectName("update_pushButton")
        self.verticalLayout_2.addWidget(self.update_pushButton)
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_4.addWidget(self.frame_2)
        ShotgunVersionWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ShotgunVersionWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        ShotgunVersionWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ShotgunVersionWindow)
        self.statusbar.setObjectName("statusbar")
        ShotgunVersionWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ShotgunVersionWindow)
        QtCore.QMetaObject.connectSlotsByName(ShotgunVersionWindow)

    def retranslateUi(self, ShotgunVersionWindow):
        ShotgunVersionWindow.setWindowTitle(QtGui.QApplication.translate("ShotgunVersionWindow", "Shotgun Version Checking", None, QtGui.QApplication.UnicodeUTF8))
        self.logo_label.setText(QtGui.QApplication.translate("ShotgunVersionWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ShotgunVersionWindow", "Project", None, QtGui.QApplication.UnicodeUTF8))
        self.getData_pushButton.setText(QtGui.QApplication.translate("ShotgunVersionWindow", "Scan Shot", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ShotgunVersionWindow", "Shotgun Shot list", None, QtGui.QApplication.UnicodeUTF8))
        self.shotgun_tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("ShotgunVersionWindow", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.shotgun_tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("ShotgunVersionWindow", "Action", None, QtGui.QApplication.UnicodeUTF8))
        self.shotgun_tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("ShotgunVersionWindow", "Shot", None, QtGui.QApplication.UnicodeUTF8))
        self.shotgun_tableWidget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("ShotgunVersionWindow", "Shotgun", None, QtGui.QApplication.UnicodeUTF8))
        self.shotgun_tableWidget.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("ShotgunVersionWindow", "Server", None, QtGui.QApplication.UnicodeUTF8))
        self.shotgun_tableWidget.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("ShotgunVersionWindow", "Publish", None, QtGui.QApplication.UnicodeUTF8))
        self.shotgun_tableWidget.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("ShotgunVersionWindow", "Step", None, QtGui.QApplication.UnicodeUTF8))
        self.shotgun_tableWidget.horizontalHeaderItem(7).setText(QtGui.QApplication.translate("ShotgunVersionWindow", "task", None, QtGui.QApplication.UnicodeUTF8))
        self.shotgun_tableWidget.horizontalHeaderItem(8).setText(QtGui.QApplication.translate("ShotgunVersionWindow", "Convert", None, QtGui.QApplication.UnicodeUTF8))
        self.all_checkBox.setText(QtGui.QApplication.translate("ShotgunVersionWindow", "All", None, QtGui.QApplication.UnicodeUTF8))
        self.update_pushButton.setText(QtGui.QApplication.translate("ShotgunVersionWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))

