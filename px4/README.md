# Parse Tools for PX4 Ulog Files

In order to run the automated parser routine download all of the following:
*  `convert_and_split.py`
*  `combine_and_resample_px4_nogui.py`
*  `make_plots.py`
*  `quat2eul.py`

### Concept of Operations

PX4 outputs log files in a binary .ulg (Ulog) file.  Ulog files must be parsed into human readable data.  The user runs the script convert_and_split.py which invokes the ulog2csv function from the [pyulog repo](https://github.com/PX4/pyulog).  Then the script combine_and_resample_px4_nogui.py is automatically called and combines all the constituent .csv files into a master .csv which is resampled according to the maximum sample rate contained in the constituent files.

### Notes

The parse method described here has been tested on Windows (in the Spyder IDE) and Ubuntu (from the terminal and from the Spyder IDE) on Python 2 and Python 3.  At least two version of PX4 firmware are confirmed working as well.

## Pre-requisites

1.  Install a working Python environment on your machine.  This can be a standalone environment or an IDE like Spyder.  Comprehensive support for getting different Python environments is not going to provided here.  Installing and running scripts in Spyder seems to be the easiest and most consistent way of getting this up and running.
1.  Pyulog must be installed in order for the script to work.
    1.  If you are using Spyder (installed via Anaconda), the best way to install the pre-requisite packages if not installed already is to open up an Anaconda prompt and issue the command `pip install pyulog`.  You may also want to install pandas if not already installed (`pip install pandas`).
    1.  If you are not using Spyder (Windows or Ubuntu (not tested on Mac)), you will need to issue the command `pip install pyulog` at the command line or terminal.  There may be issues with ensuring that your PATH variable is set correctly.  If you are having issues with this please refer to Python install help.  You should also install other missing packages in the same way, for example `pip install pandas`.

## Directory Preparation

1.  Prepare a folder containing .ulg files to be parsed.  The folder should be free of other extraneous files and should contain only .ulg files.
1.  Download the scripts `combine_and_resample_px4_nogui.py` and `convert_and_split.py` to the same directory.
1.  Your directory should now have one or more .ulg files as well as two python scripts.

## Running the Script

1.  Run the script `convert_and_split.py`
    1.  Open Spyder and open up the script `convert_and_split.py` inside of the Spyder editor.  Click the **run** button.
    1.  From the command line or terminal issue the command `python convert_and_split.py`
1.  The script will step through the list of .ulg files and create a directory for each .ulg using the name of the .ulg file as the name for the root directory.
1.  Within each directory, the expanded .csv files will be saved inside a directory named `FlightData`.
1.  Within the same directory, .txt files are created containing the output of the `ulog_messages`, `ulog_info`, and `ulog_params` commands (which are also part of the [pyulog repo](https://github.com/PX4/pyulog)).
1.  The combined file containing all the output data resampled to 250Hz will be saved in a directory inside of `FlightData` called `combined`.
1.  Plots are also now created and stored in the `Plots` directory.  Plot parameters can be changed and plots can be added omitted by modifying `make_plots.py`.

## Cautions

1.  The other script in this directory `combine_and_resample_px4.py` can be used for expanding and resampling exactly one instance of .csv files created by the `ulog2csv` function.  This script is not required for the automatic expansion and resampling.
1.  Recently, the `combine_and_resample_px4_nogui.py` was modified to fix the resample rate at 250Hz.  This was done because some PX4 log files from different firmware versions have inconsistencies in the timestamp recording which was causing the script to error out.  The script was previously calculating the fastest sample time for a given set of .csv files automatically.  This is no longer supported since the constituent .csv files are inconsistent.  The fastest message was verified manually for a handful of files at 250Hz so this rate has been hard-coded.  In the future it may be possible to add in automatic calculation functionality.
 
 ## Other Scripts
 
 The script `example_readcsvandplot.py` was added as a quick example of how to open the combined .csv and generate some plots from data.  Included is a gui file chooser and an example block to make multiple plots from a dataframe.
