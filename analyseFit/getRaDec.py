#!/usr/bin/python
import os, sys, pyfits as pf, shutil as sh, string as s

def read(file, param):
    """ Read fits file. Retrun valeu of parameter """
    hdu = pf.open(file)
    value = hdu[0].header[param]
    return value

def saveRaDec(file,ra,dec):
    name, ext = os.path.splitext(file)
    f = open('result_ra_dec.dat','a')
    sep = '\t'
    f.write(name  + sep + str(ra) + sep + str(dec) +  '\n')
    f.close()


if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    print 'This analyse file passed as argument'
    sys.exit(1)

ra = read(file,'RAOBJ')
dec = read(file,'DECOBJ')
saveRaDec(file,ra,dec)

