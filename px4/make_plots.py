# -- coding: utf-8 --
"""

Written by:     Shawn Herrington, Simeon Karnes, Cody Smith
Date:           9/16/2019
Purpose:        Modified from simple example and converted to create and save
                plots automatically inside of automated parser
Notes:          Modified original file to accept filename from auto parser,
                most of the rest of the script is unchanged
Change Log:     Thomas Cacy
Date:           07/08/2020
                changed so it works with unified parsing script's new headers
                and removed convertions that happen in the combine_and_resample
                script. Removed gragh of trigger
"""

import pandas as pd
import os
from matplotlib import pyplot as plt
#from tkinter.filedialog import askopenfilename
# get filename from the dialogue
#filename = askopenfilename(title='Select file',filetypes=[('csv files','*.csv')])

def make_plots(filename_in):
       
    filename = os.path.join(os.getcwd(),filename_in)
    
    print('Creating and saving plots from:')
    
    print(filename_in)

    # read in the data to a var called df (dataframe)
    df = pd.read_csv(filename, index_col=0, header=0)
    df['time_seconds'] = df.index
    
    just_the_pathname, just_the_filename = os.path.split(filename)
    #illumination = int(input('Time of illumination (s):     '))
    
    print('Plot Roll Pitch Yaw')
    
    #Create a new figure to graph r p y
    plt.figure()
    plt.plot(df['time_seconds'],df["Att.roll"])
    plt.plot(df['time_seconds'],df["Att.pitch"])
    plt.plot(df['time_seconds'],df["Att.yaw"])
    #plt.axvline(x=illumination, linewidth=0.5, color='red')
    plt.title('R/P/Y')
    plt.xlabel('Time, s')
    plt.ylabel('Radians per Sec')
    plt.legend(['Roll','Pitch','Yaw'])
    plt.savefig(os.path.join(os.path.dirname(os.path.dirname(just_the_pathname)),'Plots',just_the_filename[:-4]+'_R_P_Y_State.png'),dpi=600,bbox_inche='tight')
    
    print('Plot Accelerometer')
    
    #Graph Accelerometer
    plt.figure()
    plt.plot(df['time_seconds'],df['Accel.x'])
    plt.plot(df['time_seconds'],df['Accel.y'])
    plt.plot(df['time_seconds'],df['Accel.z'])
    #plt.axvline(x=illumination, linewidth=0.5, color='red')
    plt.title('Accelerometer')
    plt.xlabel('Time, s')
    plt.ylabel('m/s^2')
    plt.legend(['x-axis','y-axis','z-axis'])
    plt.savefig(os.path.join(os.path.dirname(os.path.dirname(just_the_pathname)),'Plots',just_the_filename[:-4]+'_Accelerometer.png'),dpi=600,bbox_inche='tight')
    
    print('Plot Gyroscope')
    
    #Graph Gyroscope
    plt.figure()
    plt.plot(df['time_seconds'],df['Gyro.x'])
    plt.plot(df['time_seconds'],df['Gyro.y'])
    plt.plot(df['time_seconds'],df['Gyro.z'])
    #plt.axvline(x=illumination, linewidth=0.5, color='red')
    plt.title('Gyroscope')
    plt.xlabel('Time, s')
    plt.ylabel('Radians')
    plt.legend(['x-axis','y-axis','z-axis'])
    plt.savefig(os.path.join(os.path.dirname(os.path.dirname(just_the_pathname)),'Plots',just_the_filename[:-4]+'_Gyroscope.png'),dpi=600,bbox_inche='tight')
    
    print('Plot Nav State')
    
    #Graph Nav State
    plt.figure()
    plt.plot(df['time_seconds'],df['Nav State'])
    #plt.axvline(x=illumination, linewidth=0.5, color='red')
    plt.title('Nav State')
    plt.xlabel('Time, s')
    plt.ylabel('Value')
    plt.legend(['Navigational State'])
    plt.savefig(os.path.join(os.path.dirname(os.path.dirname(just_the_pathname)),'Plots',just_the_filename[:-4]+'_NavState.png'),dpi=600,bbox_inche='tight')
    
    plt.close('all')