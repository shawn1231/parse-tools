# -- coding: utf-8 --
"""

Author: Shawn Herrington
Modified by: Simeon 
Written: 9/16/2019

Purpose: Very basic csv plotter for data analysis.

Last edited: Monday 9/16/2019 8:22PM

Change Log:
    9/17/2019 3:24PM Commented out the vertical line trigger mark. We changed the RPY to 

"""
import pandas as pd
import os
from matplotlib import pyplot as plt
from tkinter.filedialog import askopenfilename
# get filename from the dialogue
filename = askopenfilename(title='Select file',filetypes=[('csv files','*.csv')])
# read in the data to a var called df (dataframe)
df = pd.read_csv(filename, index_col=0, header=0)
df['time_seconds'] = df.index/(10.0**6)


just_the_pathname, just_the_filename = os.path.split(filename)
#illumination = int(input('Time of illumination (s):     '))


#Graph R/P/Y
plt.figure()
plt.plot(df['time_seconds'],df['q[0]'])
plt.plot(df['time_seconds'],df['q[1]'])
plt.plot(df['time_seconds'],df['q[2]'])
#plt.axvline(x=illumination, linewidth=0.5, color='red')
plt.title('R/P/Y')
plt.xlabel('Time, s')
plt.ylabel('Radians per Sec')
plt.legend(['Roll','Pitch','Yaw'])
plt.savefig(os.path.join(os.path.dirname(os.path.dirname(just_the_pathname)),'Plots',just_the_filename[:-4]+'_R_P_Y_State.png'),dpi=600,bbox_inche='tight')



#Graph Accelerometer
plt.figure()
plt.plot(df['time_seconds'],df['accelerometer_m_s2[0]'])
plt.plot(df['time_seconds'],df['accelerometer_m_s2[1]'])
plt.plot(df['time_seconds'],df['accelerometer_m_s2[2]'])
#plt.axvline(x=illumination, linewidth=0.5, color='red')
plt.title('Accelerometer')
plt.xlabel('Time, s')
plt.ylabel('m/s^2')
plt.legend(['x-axis','y-axis','z-axis'])
plt.savefig(os.path.join(os.path.dirname(os.path.dirname(just_the_pathname)),'Plots',just_the_filename[:-4]+'_Accelerometer.png'),dpi=600,bbox_inche='tight')



#Graph Gyroscope
plt.figure()
plt.plot(df['time_seconds'],df['gyro_rad[0]'])
plt.plot(df['time_seconds'],df['gyro_rad[1]'])
plt.plot(df['time_seconds'],df['gyro_rad[2]'])
#plt.axvline(x=illumination, linewidth=0.5, color='red')
plt.title('Gyroscope')
plt.xlabel('Time, s')
plt.ylabel('Radians')
plt.legend(['x-axis','y-axis','z-axis'])
plt.savefig(os.path.join(os.path.dirname(os.path.dirname(just_the_pathname)),'Plots',just_the_filename[:-4]+'_Gyroscope.png'),dpi=600,bbox_inche='tight')



#Graph Nav State
plt.figure()
plt.plot(df['time_seconds'],df['nav_state'])
#plt.axvline(x=illumination, linewidth=0.5, color='red')
plt.title('Nav State')
plt.xlabel('Time, s')
plt.ylabel('Value')
plt.legend(['Navigational State'])
plt.savefig(os.path.join(os.path.dirname(os.path.dirname(just_the_pathname)),'Plots',just_the_filename[:-4]+'_NavState.png'),dpi=600,bbox_inche='tight')




#Graph Trigger
plt.figure()
plt.plot(df['time_seconds'],df['values[5]'])
#plt.axvline(x=illumination, linewidth=0.5, color='red')
plt.title('High to Low = Trigger')
plt.xlabel('Time, s')
plt.ylabel('ON/OFF')
plt.legend(['Input'])
plt.savefig(os.path.join(os.path.dirname(os.path.dirname(just_the_pathname)),'Plots',just_the_filename[:-4]+'_Accelerometer.png'),dpi=600,bbox_inche='tight')