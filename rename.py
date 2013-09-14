import os

import sys





dir = sys.argv[1]

from_ext = sys.argv[2]
to_ext = sys.argv[3]

for filename in os.listdir(dir):
  if filename.endswith(from_ext):
    parts = filename.split('.')

    length = len(parts)

    new_parts = []

    for i in range(0, length - 1):
      new_parts.append(parts[i])


    new_parts.append(to_ext)

    new_name = '.'.join(new_parts)



    if to_ext == "test":
        print "{0}".format(filename)
    else:
        print "{0} - {1}".format(filename, new_name)

        os.rename(filename, new_name)
   

