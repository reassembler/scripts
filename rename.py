import os

import sys


old_extension = 'hid2'


for filename in os.listdir(sys.argv[1]):
  if filename.endswith(old_extension):
    parts = filename.split('.')

    length = len(parts)

    new_parts = []

    for i in range(0, length - 1):
      new_parts.append(parts[i])


    new_name = '.'.join(new_parts)


    print "{0} - {1}".format(filename, new_name)

    os.rename(filename, new_name)

   

