# read portfolio

import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
import re
import sys

def extractPortfolio():
    # extracting the portfolio from local html file as live link is not able to extract the information
    soup = BeautifulSoup(open("../vro/Snapshot - Portfolio Manager - Value Research Online.html", "r"), "html.parser")
    mf_table = soup.html.body.find_all("tbody", attrs={"class": "trData"})[0]
    rows = mf_table.find_all("tr", attrs={"class": ""})

    try:
        del(portfolio_df)
    except NameError:
        pass

    portfolio_df = pd.DataFrame(columns=['amc', 'fundname', 'code', 'units', 'cost', 'value'])

    for i, row in enumerate(rows):
        if len(row.find_all('a')) == 0:
            continue
        portfolio_df.set_value(i, 'fundname', row.find_all('a')[0].text)
        portfolio_df.set_value(i, 'amc', row.find_all('a')[0].text.split()[0])
        url = row.find_all('a')[0]['href']
        portfolio_df.set_value(i, 'code', url.split('=',)[-1])
        
        if re.sub(",","",row.find_all("td")[8].text) == "--":
            portfolio_df.set_value(i, 'cost', 0.0)
            portfolio_df.set_value(i, 'units', 0.0)
            portfolio_df.set_value(i, 'value', 0.0)
        else:
            portfolio_df.set_value(i, 'cost', float(re.sub(",","",row.find_all("td")[8].text)))
            portfolio_df.set_value(i, 'units', float(re.sub(",","",row.find_all("td")[8].text))/float(re.sub(",","",row.find_all("td")[9].text)))
            portfolio_df.set_value(i, 'value', float(re.sub(",","",row.find_all("td")[11].text)))
    return portfolio_df

if __name__ == "__main__":
    portfolio_df = extractPortfolio()
    portfolio_df

