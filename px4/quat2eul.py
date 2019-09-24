# -*- coding: utf-8 -*-
"""
Written by:     Shawn Herrington
Date:           09/17/2019
Purpose:        Quick and dirty quat2eul converter to be used in px4 parsing
                routine
"""

import math

#def quat2eul(Qx, Qy, Qz, Qw):
#    
#    roll = []
#    pitch = []
#    yaw = []
#    
#    for qx, qy, qz, qw in zip(Qx, Qy, Qz, Qw):
#        yaw.append(math.degrees(math.atan2(2*qy*qw-2*qz*qz, 1-2*qy**2-2*qz**2)))
#        pitch.append(math.degrees(math.asin(2*qx*qy+2*qz*qw)))
#        roll.append(math.degrees(math.atan2(2*qx*qw-2*qy*qz, 1-2*qx**2-2*qz**2)))
#    
#    return yaw,pitch,roll


def quat2eul(Qx, Qy, Qz, Qw):
    
    roll = []
    pitch = []
    yaw = []
    
    for q_0, q_1, q_2, q_3 in zip(Qx, Qy, Qz, Qw):
        
        roll.append(math.degrees(math.atan2((q_2*q_3) + (q_0*q_1) , 0.5-((q_1**2)+(q_2**2)))))
        pitch.append(math.degrees(math.asin(-2*((q_1*q_3)-(q_0*q_2)))))
        yaw.append(math.degrees(math.atan2((q_1*q_2)+(q_0*q_3) , 0.5-(q_2**2+q_3**2))))
    
    return roll,pitch,yaw