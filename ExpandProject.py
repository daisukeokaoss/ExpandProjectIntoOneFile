# -*- coding: utf-8 -*-

import tarfile
import glob
import os

tar = tarfile.open("SourceFolder/httpd-2.2.31.tar.gz")
tar.extractall("ExpandedFile/")
tar.close()

filepath = "ExpandedFile"

os.mkdir("Destination/")

f = open('Destination/join.txt','w')



def DrillDownFunction(filepath):
    files =glob.glob(filepath+"/*")
    for filename in files:
        if os.path.isdir(filename):
            DrillDownFunction(filename)
        else:
            line2=  "filename:" + filename + "\n"
            f.write(line2)
            for line in open(filename):
                line2 = line + "\n"
                f.write(line2)


DrillDownFunction(filepath)

f.close()
