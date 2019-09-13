# -*- coding: utf-8 -*-
"""
Example csv read and plot creator
"""

import pandas as pd
from matplotlib import pyplot as plt
from tkinter.filedialog import askopenfilename

# get filename from the dialogue
filename = askopenfilename(title='Select file',filetypes=[('csv files','*.csv')])

# read in the data to a var called df (dataframe)
df = pd.read_csv(filename, index_col=0, header=0)

df['time_seconds'] = df.index/(10.0**6)

plt.figure()
plt.plot(df['time_seconds'],df['control[0]'])
plt.plot(df['time_seconds'],df['control[1]'])
plt.plot(df['time_seconds'],df['control[2]'])
plt.plot(df['time_seconds'],df['control[3]'])
plt.plot(df['time_seconds'],df['control[4]'])
plt.plot(df['time_seconds'],df['control[5]'])
plt.plot(df['time_seconds'],df['control[6]'])
plt.plot(df['time_seconds'],df['control[7]'])

plt.xlabel('Time, s')
plt.ylabel('Some label, units')

plt.legend(['control[0]','control[1]','control[2]','control[3]','control[4]','control[5]','control[6]','control[7]'])

plt.figure()
plt.plot(df['time_seconds'],df['accelerometer_m_s2[0]'])
plt.plot(df['time_seconds'],df['accelerometer_m_s2[1]'])
plt.plot(df['time_seconds'],df['accelerometer_m_s2[2]'])

plt.xlabel('Time, s')
plt.ylabel('Acceleration, '+r'$\frac{m}{s^2}$')

plt.legend(['x','y','z'])


