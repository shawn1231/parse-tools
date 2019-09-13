#!/usr/bin/python3

'''
Created 9/1/2019
Written by:     Paul Klappa, Shawn Herrington
Purpose:        Process PX4 data logs into some kind of digestable chunk, 
                previously this script was making a bunch of plots, now it has
                been modified to do things a bit differently but the central
                idea is that we are processing a binary file into some kind of
                human readable format (csv in this case) then we are reducing
                the csv data somehow to be useful (first it was by generating
                a bunch of plots)
Changelog:
09/05/2019  Shawn Herrington
            Include code written by Paul Klappa to make lots of plot from PX4
            data
09/12/2019  Shawn Herrington
            Remove code written by Paul Klappa to make lots of plots,
            incorporate a function written by Shawn Herrington which takes all
            constituent csv files and puts them into a single csv (also
            a new directory)
'''

# os library used for directory handing and traversing
import os
# this will be used for calling terminal command directly from python
from subprocess import call
import shutil
from combine_and_resample_px4_nogui import combine_and_resample_px4_nogui

# this will get a list of all files in the current directory ending with ".ulg"
files = [f for f in os.listdir('.') if f.endswith(".ulg")]

for current_file in files:

    # create the required directory name from the name of the current_file
    # we are going to remove 4 chars from the end to get rid of ".ulg"
    endlen = len(current_file)
    dir_name = current_file[:endlen-4]

    # if statement to determine if directory exists
    if(not(os.path.isdir(dir_name))):
        # if no directory exists, create the directory
        #call(["mkdir",dir_name])
        os.mkdir(dir_name)

    # populate the directory with the data file, "-n" is copy without replacing
    # saves us from using another if statement to check if the data file exists
    #call(["cp","-n",current_file,dir_name])
    shutil.copy2(current_file,dir_name)

    # change to the directory we are currently concerned with
    os.chdir(dir_name)

    # create list of subdirectories so we can create them as necessary in a fancy way
    subdir_names = ["Flight_Data","Plots"]

    for current_name in subdir_names:
        # check for subdirectories and create if necessary
        if(not(os.path.isdir(current_name))):
            #call(['mkdir',current_name])
            os.mkdir(current_name)

    # now we know subdirectories exists, let's move the local .ulg file into the 
    # Fight_Data subdirectory to be consistent
    #call(['mv',"-n",current_file,subdir_names[0]])
    if not os.path.exists(os.path.join(subdir_names[0],current_file)):
        shutil.move(current_file,subdir_names[0])

    # now we need to change to the subdirectory to run the ulog2csv converter
    os.chdir(subdir_names[0])

    # invoke the ulog2csv application, send the current_file as argument
    # this should create many csv in the current directory from a single ulg file
    call(["ulog2csv",current_file])

    # create a path var to print out and to send to the other parse function
    # AVOID MASKING SYSTEM VAR "path" by giving it a different name
    print_path = os.getcwd()

    # print a progress report as the name of the current directory as we work
    # through the files
    print(print_path)

    # pass the progress report path to the combine_and_resample_px4_nogui() 
    # function, it will combine all csvs then stick them in a new directory
    combine_and_resample_px4_nogui(print_path)
    
    # go back up two levels so that we can keep iterating on the directory
    os.chdir(os.path.join('..','..'))
    
    print('\n')
