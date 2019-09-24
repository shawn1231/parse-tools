# -- coding: utf-8 --
"""

Written by:     Shawn Herrington, Simeon Karnes, Cody Smith
Date:           9/16/2019
Purpose:        Modified from simple example and converted to create and save
                plots automatically inside of automated parser
Notes:          Modified original file to accept filename from auto parser,
                most of the rest of the script is unchanged.
                
Changelog:
9/20/2019 Simeon Karnes
          Added "try-except" conditions around the Nav State and Trigger Plots.
          The RPY plotter y-axis label is now "Degrees" and the quat2eul conversion works with it.
9/24/2019 Simeon Karnes
          Added plotting CPU and RAM usage, then I organized every individual plotting into try/except blocks.
"""

import pandas as pd
import os
from matplotlib import pyplot as plt
import quat2eul
#from tkinter.filedialog import askopenfilename
# get filename from the dialogue
#filename = askopenfilename(title='Select file',filetypes=[('csv files','*.csv')])

def make_plots(filename_in):
       
    filename = os.path.join(os.getcwd(),filename_in)
    
    print('Creating and saving plots from this filename:')
    
    print(filename_in)

    # read in the data to a var called df (dataframe)
    df = pd.read_csv(filename, index_col=0, header=0)
    df['time_seconds'] = df.index/(10.0**6)
    
    just_the_pathname, just_the_filename = os.path.split(filename)
    #illumination = int(input('Time of illumination (s):     '))
    
    
#Graph R/P/Y
    try:
       plt.figure()
       
       # make euler angles from quaternions
       r,p,y = quat2eul.quat2eul(df['q[0]'],df['q[1]'],df['q[2]'],df['q[3]'])
    
       plt.plot(df['time_seconds'],r)
       plt.plot(df['time_seconds'],p)
       plt.plot(df['time_seconds'],y)
       #plt.axvline(x=illumination, linewidth=0.5, color='red')
       plt.title('R/P/Y')
       plt.xlabel('Time, s')
       plt.ylabel('Degrees')
       plt.legend(['Roll','Pitch','Yaw'])
       plt.savefig(os.path.join(os.path.dirname(os.path.dirname(just_the_pathname)),'Plots',just_the_filename[:-4]+'_R_P_Y_State.png'),dpi=600,bbox_inche='tight')
       print('Roll, pitch, and yaw DONE.')
    except:
       print('No roll, pitch, and yaw.')

    
#Graph Accelerometer
    try:
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
        print('Accelerometer DONE.')
    except:
        print('No accelerometer.')
   
#Graph Gyroscope    
    try:
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
       print('Gyroscope DONE.')   
    except:
       print('No gyroscope.')

#Graph Nav State
    try:
        plt.figure()
        plt.plot(df['time_seconds'],df['nav_state'])
        #plt.axvline(x=illumination, linewidth=0.5, color='red')
        plt.title('Nav State')
        plt.xlabel('Time, s')
        plt.ylabel('Value')
        plt.legend(['Navigational State'])
        plt.savefig(os.path.join(os.path.dirname(os.path.dirname(just_the_pathname)),'Plots',just_the_filename[:-4]+'_NavState.png'),dpi=600,bbox_inche='tight')
        print('Nav state DONE.')
    except:
        print('No nav state.')
        
#Graph Trigger
        #This is not yet a reliable way to determine the trigger time.
    try:
        plt.figure()
        plt.plot(df['time_seconds'],df['values[5]'])
        #plt.axvline(x=illumination, linewidth=0.5, color='red')
        plt.title('High to Low = Trigger')
        plt.xlabel('Time, s')
        plt.ylabel('ON/OFF')
        plt.legend(['Input'])
        plt.savefig(os.path.join(os.path.dirname(os.path.dirname(just_the_pathname)),'Plots',just_the_filename[:-4]+'_Trigger.png'),dpi=600,bbox_inche='tight')
        print('Trigger DONE.')
    except:
        print('No trigger.')
    
#RAM Usage  
    try:
        plt.figure()
        plt.plot(df['time_seconds'],df['ram_usage'])
        #plt.axvline(x=illumination, linewidth=0.5, color='red')
        plt.title('Ram Usage')
        plt.xlabel('Time, s')
        plt.ylabel('Ram Usage')
        plt.ylim(0,1)
        plt.legend(['Ram'])
        plt.savefig(os.path.join(os.path.dirname(os.path.dirname(just_the_pathname)),'Plots',just_the_filename[:-4]+'_RAM_Usage.png'),dpi=600,bbox_inche='tight')
        print('RAM usage DONE.')
    except:
        print('No RAM.')

#CPU Load
    try:
        plt.figure()
        plt.plot(df['time_seconds'],df['load'])
        #plt.axvline(x=illumination, linewidth=0.5, color='red')
        plt.title('CPU Load')
        plt.xlabel('Time, s')
        plt.ylabel('Load')
        plt.ylim(0,1)
        plt.legend(['Load'])
        plt.savefig(os.path.join(os.path.dirname(os.path.dirname(just_the_pathname)),'Plots',just_the_filename[:-4]+'_CPU_Load.png'),dpi=600,bbox_inche='tight')
        print('CPU load DONE.')
    except:
        print('No CPU load.')
        
    plt.close('all')
    
