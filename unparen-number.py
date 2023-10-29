from glob import glob
import os
import re
import sys

source_re = re.compile("(?P<main>.+)\s\((?P<iterator>\d+)\)\.(?P<extension>.*)")


files = glob(sys.argv[1])
for f in files:
    match = source_re.match(f)
    if match:
        new_filename = f"{match.group('main')}-{match.group('iterator')}.{match.group('extension')}"
        print(f"{f} -> {new_filename}")
        os.rename(f, new_filename)
