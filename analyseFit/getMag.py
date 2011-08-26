#!/usr/bin/python
import os, sys, pyfits as pf, shutil as sh, string as s

def read(param):
    """ Read fits file. Retrun valeu of parameter """
    hdu = pf.open(file)
    value = hdu[0].header[param]
    return value

def move(file, name):
    """ move file to directory """
    sh.copyfile(file, name.lower() + ".fit")

if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    print 'This analyse file passed as argument'
    sys.exit(1)


params = ['RAOBJ','DECOBJ','MAG']
values = map(read,params)
baseName = os.path.basename(file)
name, ext = os.path.splitext(baseName)
print name, ' '.join(map(str,values))

