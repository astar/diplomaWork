#!/usr/bin/python
"""
Given a list of RA and Dec positions perform a SIAP search saving the 
resultant VOTables and images to MySpace.
"""

import os
from time import sleep
from astrogrid import acr
from astrogrid import SiapSearch

acr.login()

# List of ra and dec. These can be read from a file.
ra = [180.0, 181.0]
dec = [0.0, 0.1]

# Initialize siap service search and name resolver
siap = SiapSearch('ivo://nasa.heasarc/skyview/sdss')

# Loop for each object of the list, query Vizier to get coordinates and execute
# the SIAP search. 

for i in range(len(ra)):
    odir = '#siap/sdss/obj%02d' % (i+1)
    out, th = siap.execute(ra[i], dec[i], 30.0/3600.0, saveAs=odir+'/sdss.vot', saveDatasets=odir, clobber=True)
    while th.isAlive():
    	sleep(10)
		
