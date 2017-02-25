#import matplotlib.pyplot as plt
#plt.style.use('ggplot')
import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4'] = 'PySide'
from matplotlib.backends import qt_compat
from PySide.QtCore import *
from PySide.QtGui import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import mf_tracker
import nav


def plotNav(plotCanvas, fundname, dateStart, dateEnd):
    #print mf_tracker.df_portfolio
    print fundname + "nav data loading..."
    schemeCode = mf_tracker.df_portfolio[mf_tracker.df_portfolio["fundname"] == fundname]
    schemeCode = str(int(schemeCode["code"]))

    nav_df = nav.getHistoryData(schemeCode)
    nav_df = nav_df["nav"]
    nav_df = nav_df[dateStart:dateEnd]
    plotCanvas.axes.clear()
    plotCanvas.plot(plotCanvas, nav_df)
    plotCanvas.axes.autoscale()
    print "plot finished..."
    
class NavCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        #FigureCanvas.setSizePolicy(self,
        #                           QtGui.QSizePolicy.Expanding,
        #                           QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def plot(self, plotCanvas, df_data):
        df_data.plot(ax = plotCanvas.axes)
        self.draw()
