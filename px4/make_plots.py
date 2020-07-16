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
                script. Removed gragh of trigger. Moved the creation of the 
                'Plots' directory to this program. Added var names for paths
                so the same calculation is not preformed many times. Program 
                will not figure out what plots are missing and only save those
                it needs
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
    
    just_the_pathname, just_the_filename = os.path.split(filename)
    #illumination = int(input('Time of illumination (s):     '))
    
    plot_r_p_y = True
    plot_accel = True
    plot_gyro = True
    plot_nav = True
    
    # directory that contains Plots directory
    path_to_Plots = os.path.join(os.path.dirname(os.path.dirname(just_the_pathname)),'Plots')
    
    # path to the file
    dir_Plots = path_to_Plots+'/'+just_the_filename[:-4]
    
    # plot file location
    r_p_y_path = dir_Plots+'_R_P_Y_State.png'
    accel_path = dir_Plots+'_Accelerometer.png'
    gyro_path = dir_Plots+'_Gyroscope.png'
    nav_path = dir_Plots+'_NavState.png'
    
    # make a directory to save the plots if one does not exist and determine 
    # what needs to be plotted
    if(not(os.path.isdir(path_to_Plots))):
        os.mkdir(path_to_Plots)
    if os.path.isfile(r_p_y_path):
        plot_r_p_y = False
    if os.path.isfile(accel_path):
        plot_accel = False
    if os.path.isfile(gyro_path):
        plot_gyro = False
    if os.path.isfile(nav_path):
        plot_nav = False
    
    # read in the data to a var called df (dataframe)
    df = pd.read_csv(filename, index_col=0, header=0)
    df['time_seconds'] = df.index
    
    # check if the r p y plot exists
    if plot_r_p_y:
        
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
        
        plt.savefig(r_p_y_path,dpi=600,bbox_inche='tight')
        
    else: 
        print('Roll Pitch Yaw plot already exists for: '+just_the_filename[:-4])
    
    # check if the accel plot exists
    if plot_accel:
    
        try:
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
            plt.savefig(accel_path,dpi=600,bbox_inche='tight')
            
        except: print('Accelerometer data not found')
        
    else: 
        print('Accelerometer plot already exists for: '+just_the_filename[:-4])
        
    # check if gyro plot exist
    if plot_gyro:
        
        try:
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
            plt.savefig(gyro_path,dpi=600,bbox_inche='tight')
            
        except: print('Gyroscope data not found')
            
    else: 
        print('Gyro plot already exists for: '+just_the_filename[:-4])
        
    # check if nave plot exist
    if plot_nav:
        
        try:
            print('Plot Nav State')
            
            #Graph Nav State
            plt.figure()
            plt.plot(df['time_seconds'],df['Nav State'])
            #plt.axvline(x=illumination, linewidth=0.5, color='red')
            plt.title('Nav State')
            plt.xlabel('Time, s')
            plt.ylabel('Value')
            plt.legend(['Navigational State'])
            plt.savefig(nav_path,dpi=600,bbox_inche='tight')
            
        except: print('Nav State data not found')
    
    else: 
        print('Navigational State plot already exists for: '+just_the_filename[:-4])
    
        
    plt.close('all')