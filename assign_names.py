# -*- coding: utf-8 -*-
"""
Written: Thomas Cacy
Date: 07/10/2020
Purpose: To assign new names to the columns of the results.csv for the unified
parsing project

"""
# function creates a list of the new column headers in the correct order
def assign_names(keyword, new_headers):
    
    #assign the new header to the current header by the keyword
    if (keyword == 'lat'):
        new_headers.append('GPS.lat')
    if (keyword == 'lon'):
         new_headers.append('GPS.lon')
    if (keyword =='alt'):
         new_headers.append('GPS.alt')                        
    if (keyword == 'hdop'):
         new_headers.append('GPS.hdop')
    if (keyword == 'vdop'):
         new_headers.append('GPS.vdop')
    if (keyword == 'mode_slot'):
         new_headers.append('Mode')
    if (keyword == 'accelerometer_m_s2[0]'):
         new_headers.append('Accel.x')
    if (keyword == 'accelerometer_m_s2[1]'):
         new_headers.append('Accel.y')
    if (keyword == 'accelerometer_m_s2[2]'):
        new_headers.append('Accel.z')
    if (keyword == 'gyro_rad[0]'):
         new_headers.append('Gyro.x')
    if (keyword == 'gyro_rad[1]'):
         new_headers.append('Gyro.y')
    if (keyword == 'gyro_rad[2]'):
         new_headers.append('Gyro.z')
    if (keyword == 'magnetometer_ga[0]'):
         new_headers.append('Mag.x')
    if (keyword == 'magnetometer_ga[1]'):
         new_headers.append('Mag.y')
    if (keyword == 'magnetometer_ga[2]'):
         new_headers.append('Mag.z')
    if (keyword == 'failsafe'):
         new_headers.append('RCfailsafe')
    if (keyword == 'voltage_v'):
         new_headers.append('Voltage')
    if (keyword == 'rssi'):
         new_headers.append('RCsignalstrength')
    if (keyword == 'channel'):
         new_headers.append('RCin')
    if (keyword == 'q[0]'):
         new_headers.append('Att.Qx')
    if (keyword == 'q[1]'):
         new_headers.append('Att.Qy')
    if (keyword == 'q[2]'):
         new_headers.append('Att.Qz')
    if (keyword == 'q[3]'):
         new_headers.append('Att.Qw')
    if (keyword == 'baro_alt'):
         new_headers.append('BaroAlt')
    if (keyword == 'nav_state'):
         new_headers.append('Nav State')

