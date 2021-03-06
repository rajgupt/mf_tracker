﻿# MF Tracker is used to track and monitor the MF portfolio
# This is an extension to the Value Research Approach Tailored 
# to monitor in details

##############################################################################################
# Inputs required

# 1. Portfolio exported from value research and saved as csv after removing the top and bottom rows

# 2. Transaction History exported from Value research and saved as csv file

##############################################################################################
# Functionalities Required

# 1. Get Historical NAV Data of fund by its code - nac.py

# 2. Parse the transaction csv file

# 3. Parse the snapshot portfoilio file

# 4. Plot the transaction on time line with overlaid nav history and benchmark history

# 5. Get the return w.r.t. to a particular investment 

# 6. Get the XIRR w.r.t. to set of transactions

# 7. Get the XIRR based on various filtered criteria like time duration, fund category etc

import portfolio
import sys
import mf_tracker_gui
import pandas as pd
from PySide.QtGui import *
from PySide.QtCore import *

df_portfolio = pd.DataFrame()
df_portfolio = portfolio.extractPortfolio()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = mf_tracker_gui.NAVWindow()
    win.comboBox.addItems(sorted(list(set(df_portfolio["fundname"]))))

    win.show()
    app.exec_()
