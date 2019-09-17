# -*- coding: utf-8 -*-
"""
Written by:     Shawn Herrington
Date:           09/17/2019
Purpose:        Quick and dirty quat2eul converter to be used in px4 parsing
                routine
"""

import math

def quat2eul(Qx, Qy, Qz, Qw):
    
    roll = []
    pitch = []
    yaw = []
    
    for qx, qy, qz, qw in zip(Qx, Qy, Qz, Qw):
        yaw.append(math.degrees(math.atan2(2*qy*qw-2*qz*qz, 1-2*qy**2-2*qz**2)))
        pitch.append(math.degrees(math.asin(2*qx*qy+2*qz*qw)))
        roll.append(math.degrees(math.atan2(2*qx*qw-2*qy*qz, 1-2*qx**2-2*qz**2)))
    
    return yaw,pitch,roll