# 11/11/18
# Copy files from a CSV named files_map.csv to indicated paths and names.

import os
import shutil
import errno
import csv
import sys

if not os.path.isfile('file_map.csv'):
    print('Please create a file named file_map.csv in the current directory.')
    sys.exit()

with open('file_map.csv', 'r') as f:
    rdr = csv.reader(f, delimiter=',', quotechar='"')

    count = 0
    for line in rdr:
        # skip the header line
        if count > 0:

            # create directory paths if they don't exist
            if ('/' in line[1]) and (not os.path.exists(os.path.dirname(line[1]))):
                try:
                    os.makedirs(os.path.dirname(line[1]))
                except OSError as exc:  # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise

            # os.rename(line[0], line[1])
            try:
                shutil.copy2(line[0], line[1])
            except OSError:
                print('This file wasn\'t found in this folder: {}'.format(line[0]))

        count += 1
