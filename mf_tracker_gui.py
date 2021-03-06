import exceptions
from PySide.QtCore import *
from PySide.QtGui import *

import mf_tracker
import nav
import mf_nav_ui
import mf_nav_gui
import pyqtgraph as pg
from plotUtils import DateAxisItem
pg.setConfigOptions(antialias=True)

TimeIntervalInYears = 1

class NAVWindow(QMainWindow, mf_nav_ui.Ui_MainWindow):
    def __init__(self, *args):
        super(NAVWindow, self).__init__(*args)
        self.setupUi(self)
        self.startDateEdit.setDate(QDate.currentDate().addYears(-1*TimeIntervalInYears))
        self.endDateEdit.setDate(QDate.currentDate())
        self.connect(self.comboBox, SIGNAL("currentIndexChanged(int)"), self.mf_selected)
        self.connect(self.plotNavButton, SIGNAL("clicked()"), self.plotNavCallback)

    def mf_selected(self, int):
        pass

    def plotNavCallback(self):
        qdateStart = self.startDateEdit.date()
        qdateEnd = self.endDateEdit.date()
        dateStart = str(qdateStart.year())+"/"+str(qdateStart.month())+"/"+str(qdateStart.day())
        dateEnd = str(qdateEnd.year())+"/"+str(qdateEnd.month())+"/"+str(qdateEnd.day())
        mf_nav_gui.plotNav(self.comboBox.currentText(), dateStart, dateEnd)
