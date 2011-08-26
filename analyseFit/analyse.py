#!/usr/bin/python
import sys, pyfits as pf, shutil as sh, string as s

def read(file, param):
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

good = 6200
plusMinus = 100
value = read(file,'CRVAL1')
name = read(file,'OBJECT')
name = s.replace(name,' ','_')          # change spaces to _
if value > good - plusMinus  and value < plusMinus + good:
    move(file,name)
    print "good:\t", name, value
else:
    print "bad:\t", name, value
