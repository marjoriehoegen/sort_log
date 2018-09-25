import os
import glob
from heapq import merge
from itertools import count, islice
from contextlib import ExitStack


filenames = []

# open file
with open('huge_dummy.log') as input_file:
    for file_number in count(1):
        # read in next 20k lines and sort them
        sorted_file = sorted(islice(input_file, 20000))
        if not sorted_file:
            # when reached the end of input
            break

        # create files
        filename = 'filename_{}.chk'.format(file_number)
        # append new file and write
        filenames.append(filename)
        with open(filename, 'w') as file:
            file.writelines(sorted_file)

# merge all files
with ExitStack() as stack, open('output.txt', 'w') as output_file:
    files = [stack.enter_context(open(file)) for file in filenames]
    output_file.writelines(merge(*files))

# remove temporary files

for f in glob.glob("filename_*.chk"):
	os.remove(f)
