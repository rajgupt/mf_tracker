# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mf_nav.ui'
#
# Created: Sun Feb 26 23:22:19 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(608, 543)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.plotNavButton = QtGui.QPushButton(self.centralwidget)
        self.plotNavButton.setObjectName("plotNavButton")
        self.gridLayout.addWidget(self.plotNavButton, 3, 1, 1, 1)
        self.mfLabel = QtGui.QLabel(self.centralwidget)
        self.mfLabel.setObjectName("mfLabel")
        self.gridLayout.addWidget(self.mfLabel, 0, 0, 1, 1)
        self.startDateEdit = QtGui.QDateEdit(self.centralwidget)
        self.startDateEdit.setObjectName("startDateEdit")
        self.gridLayout.addWidget(self.startDateEdit, 1, 1, 1, 1)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.startDateLabel = QtGui.QLabel(self.centralwidget)
        self.startDateLabel.setObjectName("startDateLabel")
        self.gridLayout.addWidget(self.startDateLabel, 2, 0, 1, 1)
        self.endDateLabel = QtGui.QLabel(self.centralwidget)
        self.endDateLabel.setObjectName("endDateLabel")
        self.gridLayout.addWidget(self.endDateLabel, 1, 0, 1, 1)
        self.endDateEdit = QtGui.QDateEdit(self.centralwidget)
        self.endDateEdit.setObjectName("endDateEdit")
        self.gridLayout.addWidget(self.endDateEdit, 2, 1, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.gridLayout.addLayout(self.verticalLayout, 4, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 608, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Mutual Fund NAV", None, QtGui.QApplication.UnicodeUTF8))
        self.plotNavButton.setText(QtGui.QApplication.translate("MainWindow", "Plot NAV Data", None, QtGui.QApplication.UnicodeUTF8))
        self.mfLabel.setText(QtGui.QApplication.translate("MainWindow", "Mutual Fund", None, QtGui.QApplication.UnicodeUTF8))
        self.startDateLabel.setText(QtGui.QApplication.translate("MainWindow", "End Date", None, QtGui.QApplication.UnicodeUTF8))
        self.endDateLabel.setText(QtGui.QApplication.translate("MainWindow", "Start Date", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p align=\"center\">NAV Plot</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

