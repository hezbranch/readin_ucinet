# READIN_UCINET.PY
# Author: Hezekiah Branch
# Date: September 24, 2020
# Purpose: Read in UCINET DL dataset as pandas DF

#!/usr/bin/env python3

import pandas as pd

def __init__(self):
    print("Preparing to read UCINET data into pandas DataFrame...\n")

def read_ucinet(ucinet_filepath):
    # First read in UCINET DL dataset
    ucinet_file = open(ucinet_filepath, "r")
    ucinet_graph = []
    for line in ucinet_file.readlines():
            if (line[0].isalpha() == False):
                add_row = []
                for edge in line:
                    if (edge >= '0'):
                        add_row.append(int(edge))
                ucinet_graph.append(add_row)
    ucinet_file.close()
    pd_ucinet_graph = pd.DataFrame(data=ucinet_graph)
    print(pd_ucinet_graph)
    return pd_ucinet_graph


