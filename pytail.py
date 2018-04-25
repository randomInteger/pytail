#!/usr/bin/env python3
#pytail.py
#Very simple tail implementation in python3
#Author:  Christopher Gleeson, April 2018

#Note:  Need a big enough test file?  try:  man proc > bigfile.txt

import os
import sys

#buffer as much as two blocks
block_size = 4096
buffer_size = 2 * block_size

#This is not great input argument handling and we should use a nice package like
#getopt
if len(sys.argv) < 3:
    print("Please call this tool with <filename> <numlines> as arguments")
    print("Exiting")
    sys.exit(1)
file_name = sys.argv[1] # file path, absolute
num_lines = int(sys.argv[2])  # num_lines requested
file_size = os.stat(file_name).st_size  # size of file in bytes, no more seek relative to end :-(

lines = []

#special case if the file is super small, do it the easy way
if file_size < buffer_size:
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines[-num_lines:]:
            print(line, end='') #Else you get double newlines...
        sys.exit(0)

#Continuing means we can seek to buffer_size...
i = 0  #counter variable, we may have to go back a few times to get enough lines
with open(file_name) as f:
    while True:
        i += 1
        f.seek(file_size - buffer_size*i) #Seek to the end of the file - the buffer * count
        lines.extend(f.readlines())  #We don't want a list of lists, just extend the list
        if len(lines) >= num_lines or f.tell() == 0:  #stop when we have enough lines or we are at the last line
            for line in lines[-num_lines:]:
                print(line, end='')
            break
