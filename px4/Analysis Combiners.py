# -*- coding: utf-8 -*-
"""

Analysis combiners

@author: Harrison Terry

Combines all previously created Statistical csvs into one concatenated file

Not ready for running 

"""

import os
import shutil
import glob
import pandas as pd

#Overarching folder that holds subfolders with combined files
src_dir = "Insertdirectory"
#Directory for degradation files
dst_dir= "Insertdestination"
for root, dirs, files in os.walk(src_dir):
    for f in files:
        if f.endswith('Data.csv'):
            shutil.copy(os.path.join(root,f), dst_dir)
        if f.endswith('Statistics.csv'):
            shutil.copy(os.path.join(root,f), dst_dir)
            
os.chdir(dst_dir)

all_files = glob.glob(dst_dir + "/*.csv")

lis = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    lis.append(df)
    
frame = pd.concat(lis)

