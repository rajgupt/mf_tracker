# different routine to make plot

# assuming the pyplot

import nav
import pandas as pd
import datetime

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

