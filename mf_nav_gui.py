#import matplotlib.pyplot as plt
#plt.style.use('ggplot')
import pyqtgraph as pg
from pyqtgraph import GraphicsLayout
from PySide.QtCore import *
from PySide.QtGui import *
import mf_tracker
import nav
from datetime import datetime
import time
from plotUtils import DateAxisItem


def plotNav(fundname, dateStart, dateEnd):
    #print mf_tracker.df_portfolio
    print fundname + " nav data loading..."
    schemeCode = mf_tracker.df_portfolio[mf_tracker.df_portfolio["fundname"] == fundname]
    schemeCode = str(int(schemeCode[:1]["code"]))

    nav_df = nav.getHistoryData(schemeCode)
    nav_df = nav_df["nav"]
    nav_df = nav_df[dateStart:dateEnd]
    win = pg.GraphicsWindow(title="NAV Plot")
    plot = win.addPlot(title='NAV data', axisItems={'bottom': DateAxisItem(orientation='bottom')})

    plot.showGrid(x=True, y=True)
    epoch_times = [time.mktime(ts.timetuple()) for ts in nav_df.index]
    tickTuples = [[(int(epoch), time.strftime('%Y-%m-%d', time.localtime(epoch))) for epoch in epoch_times]]

    plot.plot(epoch_times, nav_df.values, clear=True)
    # plotItem.getAxis('bottom').setTicks(tickTuples)
    print "plot finished..."
