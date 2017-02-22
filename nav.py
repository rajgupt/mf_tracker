# getting the historical nav data from value research
import sys
import requests
import pandas as pd
import datetime

mf_df = pd.DataFrame()

# Get the historical nav and benchmark value history for 3 years in form of data frame
def getHistoryData(schemeCode):
    '''
    Historical NAV data provided by valueresearchonline.com
    Along with the benchmark index value time series
    '''
    url = "https://www.valueresearchonline.com/funds/fundVSindex.asp?Sch=" + schemeCode

    # if mf_df.size != 0:
    #     # data already present
    #     return mf_df

    response = requests.get(url)
    nav_json = response.json()

    mf_df = pd.DataFrame(nav_json[1][0]['data'])
    convert_date = lambda d: datetime.datetime.fromtimestamp(d/1000)

    mf_df.columns = ['timestamp', 'nav']
    mf_df.index = mf_df['timestamp'].map(convert_date)
    mf_df = mf_df.drop('timestamp', axis=1)

    bench_df = pd.DataFrame(nav_json[1][1]['data'])
    bench_df.columns = ['timestamp', 'nav']
    bench_df.index = bench_df['timestamp'].map(convert_date)
    bench_df = bench_df.drop('timestamp', axis=1)

    mf_df['benchmark'] = bench_df['nav']
    return mf_df

def getNavCompareData(scheme_code, start_date):
    '''
    Historical percent change time series
    '''
    # start_date should be text eg: '2014/1/1'
    nav_history_df = getHistoryData(scheme_code)
    nav_history_df = nav_history_df[start_date:]
    pct = nav_history_df.apply(getPercentChange)
    return pct

def getPercentChange(nav_series):
    '''
    func to be applied on dataframe to get percent change
    w.r.t. first index
    '''
    return (nav_series - nav_series[0])/nav_series[0]

if __name__ == "__main__":
    mf_df = getHistoryData(sys.argv[1])
    start_date = '2016/8/24'
    pct_df = getNavCompareData(sys.argv[1], start_date)
    mf = pd.concat([mf_df[start_date:], pct_df], axis=1)
    mf.to_csv(sys.argv[1]+".csv")
