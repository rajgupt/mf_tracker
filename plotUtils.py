# different routine to make plot

# assuming the pyplot

import nav
import pandas as pd
import datetime
from PySide.QtCore import QTime
import pyqtgraph as pg
import time

class DateAxisItem(pg.AxisItem):
    def __init__(self, *args, **kwargs):
        super(DateAxisItem, self).__init__(*args, **kwargs)
        self.classType = 'DateAxisItem'

    def tickStrings(self, values, scale, spacing):
        # PySide's QTime() initialiser fails miserably and dismisses args/kwargs
        print "Dateaxis - ", self
        print time.strftime('%Y-%m-%d', time.localtime(values[0]))
        return [time.strftime('%Y-%m-%d', time.localtime(epoch)) for epoch in values]


def plotNavHistory(schemeCode):
    nav_df = nav.getHistoryData(schemeCode)
    nav_df['nav'].plot()



def plotBenchmarkHistory(schemeCode):
    nav_df = nav.getHistoryData(schemeCode)
    nav_df['benchmark'].plot()


def plotNavBenchmarkComparison(schemeCode, initDate):
    nav_df = nav.getHistoryData(schemeCode)
    pct_df = nav.getNavCompareData(schemeCode, initDate)
    pct_df['benchmark'].plot()
    pct_df['nav'].plot()

if __name__ == "__main__":
    schemeCode = '15688'
    startDate = '2016/8/24'
    plotNavBenchmarkComparison(schemeCode, startDate)

