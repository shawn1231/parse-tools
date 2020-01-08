# -- coding: utf-8 --
"""

Written by:     Shawn Herrington, Simeon Karnes, Cody Smith
Date:           9/16/2019
Purpose:        Modified from simple example and converted to create and save
                plots automatically inside of automated parser
Notes:          Modified original file to accept filename from auto parser,
                most of the rest of the script is unchanged.
                
Changelog:
9/20/2019   Simeon Karnes
            Added "try-except" conditions around the Nav State and Trigger
            Plots. The RPY plotter y-axis label is now "Degrees" and the
            quat2eul conversion works with it.
9/24/2019   Simeon Karnes
            Added plotting CPU and RAM usage, then I organized every individual
            plotting into try/except blocks.
09/26/2019  Shawn Herrington
            Updated some plots to account for the newly renamed resampled csv
            Column names now contain constituent csv file name as well to
            prevent overwriting of duplicates.  Some fixes have been applied
            here but not all.  Further work needs to be done to fix other plots
            and/or clean up the way this was done (it's kind of sloppy)
09/27/2019  Paul Klappa
            Updated df column call for cpu load and ram
            The make_plots code will now create load and ram plots
            Added loc='best' for legend parameter to place legend box in 'best'
            location to avoid overlaying on top of data lines
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
        csv_file_prefix = 'vehicle_attitude_0'
        
        plt.figure()
        
#        print(csv_file_prefix+'_'+'q[0]')
        
        # make euler angles from quaternions
        r,p,y = quat2eul.quat2eul(df[csv_file_prefix+'_'+'q[0]'],df[csv_file_prefix+'_'+'q[1]'],df[csv_file_prefix+'_'+'q[2]'],df[csv_file_prefix+'_'+'q[3]'])
        
        plt.plot(df['time_seconds'],r)
        plt.plot(df['time_seconds'],p)
        plt.plot(df['time_seconds'],y)
        #plt.axvline(x=illumination, linewidth=0.5, color='red')
        plt.title('R/P/Y')
        plt.xlabel('Time, s')
        plt.ylabel('Degrees')
        plt.legend(['Roll','Pitch','Yaw'],loc='best')
        plt.savefig(os.path.join(os.path.dirname(os.path.dirname(just_the_pathname)),'Plots',just_the_filename[:-4] + '_'+csv_file_prefix + '_R_P_Y_State.png'),dpi=600,bbox_inche='tight')
        print('Roll, pitch, and yaw DONE.')
    except:
        print('No roll, pitch, and yaw.')

    
#Graph Accelerometer
    try:
        csv_file_prefix = 'sensor_combined_0'        
        plt.figure()
        plt.plot(df['time_seconds'],df[csv_file_prefix+'_'+'accelerometer_m_s2[0]'])
        plt.plot(df['time_seconds'],df[csv_file_prefix+'_'+'accelerometer_m_s2[1]'])
        plt.plot(df['time_seconds'],df[csv_file_prefix+'_'+'accelerometer_m_s2[2]'])
        #plt.axvline(x=illumination, linewidth=0.5, color='red')
        plt.title('Accelerometer')
        plt.xlabel('Time, s')
        plt.ylabel('m/s^2')
        plt.legend(['x-axis','y-axis','z-axis'],loc='best')
        plt.savefig(os.path.join(os.path.dirname(os.path.dirname(just_the_pathname)),'Plots',just_the_filename[:-4] + '_' + csv_file_prefix + '_Accelerometer.png'),dpi=600,bbox_inche='tight')
        print('Accelerometer DONE.')
    except:
        print('No accelerometer.')
   
#Graph Gyroscope    
    try:
        csv_file_prefix = 'sensor_combined_0' 
        plt.figure()
        plt.plot(df['time_seconds'],df[csv_file_prefix+'_'+'gyro_rad[0]'])
        plt.plot(df['time_seconds'],df[csv_file_prefix+'_'+'gyro_rad[1]'])
        plt.plot(df['time_seconds'],df[csv_file_prefix+'_'+'gyro_rad[2]'])
        #plt.axvline(x=illumination, linewidth=0.5, color='red')
        plt.title('Gyroscope')
        plt.xlabel('Time, s')
        plt.ylabel('Radians')
        plt.legend(['x-axis','y-axis','z-axis'],loc='best')
        plt.savefig(os.path.join(os.path.dirname(os.path.dirname(just_the_pathname)),'Plots',just_the_filename[:-4] + '_' + csv_file_prefix + '_Gyroscope.png'),dpi=600,bbox_inche='tight')
        print('Gyroscope DONE.')   
    except:
        print('No gyroscope.')

#Graph Voltage    
    try:
        csv_file_prefix = 'system_power_0' 
        plt.figure()
        plt.plot(df['time_seconds'],df[csv_file_prefix+'_'+'voltage5v_v'])
        plt.plot(df['time_seconds'],df[csv_file_prefix+'_'+'voltage3v3_v'])
        #plt.axvline(x=illumination, linewidth=0.5, color='red')
        plt.title('Power Module Voltage')
        plt.xlabel('Time, s')
        plt.ylabel('Volt')
        plt.legend(['5V','3V'],loc='best')
        plt.savefig(os.path.join(os.path.dirname(os.path.dirname(just_the_pathname)),'Plots',just_the_filename[:-4] + '_' + csv_file_prefix + '_PMUVoltage.png'),dpi=600,bbox_inche='tight')
        print('Power DONE.')   
    except:
        print('No power.')
 
#Graph Current    
    try:
        csv_file_prefix = 'battery_status_0' 
        plt.figure()
        plt.plot(df['time_seconds'],df[csv_file_prefix+'_'+'current_a'])
        plt.plot(df['time_seconds'],df[csv_file_prefix+'_'+'current_filtered_a'])
        plt.plot(df['time_seconds'],df[csv_file_prefix+'_'+'average_current_a'])
        #plt.axvline(x=illumination, linewidth=0.5, color='red')
        plt.title('Battery Current')
        plt.xlabel('Time, s')
        plt.ylabel('Amp')
        plt.legend(['current','filtered','average'],loc='best')
        plt.savefig(os.path.join(os.path.dirname(os.path.dirname(just_the_pathname)),'Plots',just_the_filename[:-4] + '_' + csv_file_prefix + '_BatteryCurrent.png'),dpi=600,bbox_inche='tight')
        print('Battery Current DONE.')   
    except:
        print('No battery current.')
        
#Graph Other Voltage
    try:
        csv_file_prefix = 'battery_status_0' 
        plt.figure()
        plt.plot(df['time_seconds'],df[csv_file_prefix+'_'+'voltage_v'])
        plt.plot(df['time_seconds'],df[csv_file_prefix+'_'+'voltage_filtered_v'])
        #plt.axvline(x=illumination, linewidth=0.5, color='red')
        plt.title('Battery Voltage')
        plt.xlabel('Time, s')
        plt.ylabel('Amp')
        plt.legend(['voltage','filtered'],loc='best')
        plt.savefig(os.path.join(os.path.dirname(os.path.dirname(just_the_pathname)),'Plots',just_the_filename[:-4] + '_' + csv_file_prefix + '_BatteryVoltage.png'),dpi=600,bbox_inche='tight')
        print('Battery Voltage DONE.')   
    except:
        print('No battery voltage.')

#Graph Mag    
    try:
        csv_file_prefix = 'vehicle_magnetometer_0' 
        plt.figure()
        plt.plot(df['time_seconds'],df[csv_file_prefix+'_'+'magnetometer_ga[0]'])
        plt.plot(df['time_seconds'],df[csv_file_prefix+'_'+'magnetometer_ga[1]'])
        plt.plot(df['time_seconds'],df[csv_file_prefix+'_'+'magnetometer_ga[2]'])
        #plt.axvline(x=illumination, linewidth=0.5, color='red')
        plt.title('Magnetometer')
        plt.xlabel('Time, s')
        plt.ylabel('Gauss')
        plt.legend(['x-axis','y-axis','z-axis'],loc='best')
        plt.savefig(os.path.join(os.path.dirname(os.path.dirname(just_the_pathname)),'Plots',just_the_filename[:-4] + '_' + csv_file_prefix + '_Magnetometer.png'),dpi=600,bbox_inche='tight')
        print('Magentometer DONE.')   
    except:
        print('No magnetometer.')
        
#Graph Nav State
    try:
        csv_file_prefix = 'vehicle_status_0'
        plt.figure()
        plt.plot(df['time_seconds'],df[csv_file_prefix+'_'+'nav_state'])
        #plt.axvline(x=illumination, linewidth=0.5, color='red')
        plt.title('Nav State')
        plt.xlabel('Time, s')
        plt.ylabel('Value')
        plt.legend(['Navigational State'],loc='best')
        plt.savefig(os.path.join(os.path.dirname(os.path.dirname(just_the_pathname)),'Plots',just_the_filename[:-4] + '_' + csv_file_prefix + '_NavState.png'),dpi=600,bbox_inche='tight')
        print('Nav state DONE.')
    except:
        print('No nav state.')

              
#Graph Trigger
        #Using the new trigger method, mode swith should form a square pulse
        #about 3s prior
    try:
        csv_file_prefix = 'input_rc_0'
        plt.figure()
        plt.plot(df['time_seconds'],df[csv_file_prefix+'_'+'values[5]'])
        #plt.axvline(x=illumination, linewidth=0.5, color='red')
        plt.title('RC Channel 5 (trigger)')
        plt.xlabel('Time, s')
        plt.ylabel('Value')
        plt.legend(['Channel 5'],loc='best')
        plt.savefig(os.path.join(os.path.dirname(os.path.dirname(just_the_pathname)),'Plots',just_the_filename[:-4] + '_' + csv_file_prefix + '_RC.png'),dpi=600,bbox_inche='tight')
        print('RC DONE.')
    except:
        print('No RC.')
    
#RAM Usage  
    try:
        csv_file_prefix = 'cpuload_0'
        plt.figure()
        plt.plot(df['time_seconds'],df[csv_file_prefix+'_'+'ram_usage'])
        #plt.axvline(x=illumination, linewidth=0.5, color='red')
        plt.title('Ram Usage')
        plt.xlabel('Time, s')
        plt.ylabel('Ram Usage')
        plt.ylim(0,1)
        plt.legend(['Ram'],loc='best')
        plt.savefig(os.path.join(os.path.dirname(os.path.dirname(just_the_pathname)),'Plots',just_the_filename[:-4]+'_RAM_Usage.png'),dpi=600,bbox_inche='tight')
        print('RAM usage DONE.')
    except:
        print('No RAM.')

#CPU Load
    try:
        csv_file_prefix = 'cpuload_0'
        plt.figure()
        plt.plot(df['time_seconds'],df[csv_file_prefix+'_'+'load'])
        #plt.axvline(x=illumination, linewidth=0.5, color='red')
        plt.title('CPU Load')
        plt.xlabel('Time, s')
        plt.ylabel('Load')
        plt.ylim(0,1)
        plt.legend(['Load'],loc='best')
        plt.savefig(os.path.join(os.path.dirname(os.path.dirname(just_the_pathname)),'Plots',just_the_filename[:-4]+'_CPU_Load.png'),dpi=600,bbox_inche='tight')
        print('CPU load DONE.')
    except:
        print('No CPU load.')
        
#Graph Number of Satellites
    try:
        csv_file_prefix = 'vehicle_gps_position_0'
        plt.figure()
        plt.plot(df['time_seconds'],df[csv_file_prefix+'_'+'satellites_used'])
        plt.title('GPS Number of Satellites')
        plt.xlabel('Time, s')
        plt.ylabel('Value')
        plt.legend(['Satellites'],loc='best')
        plt.savefig(os.path.join(os.path.dirname(os.path.dirname(just_the_pathname)),'Plots',just_the_filename[:-4] + '_Satellites.png'),dpi=600,bbox_inche='tight')
        print('GPS Satellites DONE.')   
    except:
        print('No satellites.')
        
    plt.close('all')
    
