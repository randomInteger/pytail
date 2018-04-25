# pytail
An extremely simple (and crude) implementation of tail that works even for files too large to fit into memory
# testing notes
To test this quickly, run it with a file with only a few lines (smaller than 8192 bytes), then run it again with the largest file you wish to try.  A simple way to see it work is to create a large file of numbered lines like this "seq 1 100000 > file.txt".  Then profile the script as it runs and you will see it seeks to near the end and does not attempt to read the file into memory.

Example:

<img src="https://github.com/randomInteger/pytail/blob/master/example.pngx" width="600" heighth="400">
