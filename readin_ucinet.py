# READIN_UCINET.PY
# Author: Hezekiah Branch
# Date: September 24, 2020
# Purpose: Read in UCINET DL dataset as pandas DF

import os
import pandas as pd

# First read in UCINET DL dataset
ucinet_filepath = input("Enter path of dataset: ")
os.chdir(ucinet_filepath)
ucinet_file = open(input("Enter name of file: "), "r")
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