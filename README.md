# pytail
An extremely simple (and crude) implementation of tail that works even for files too large to fit into memory
# testing notes
To test this quickly, run it with a file with only a few lines (smaller than 8192 bytes), then run it again with the largest file you wish to try.  A simple way to see it work is to create a medium size file by doing something like "man proc > file.txt" and then profile this script to see that it seeks to the end and does NOT read the entire file into memory.
