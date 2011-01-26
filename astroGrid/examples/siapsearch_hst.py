#!/usr/bin/python
"""
Given a list of object names perform a SIAP search to the HST archive and retrieve the
list of images (Note: not the images)

"""
import os, time
from optparse import OptionParser
from astrogrid import acr, sesame
from astrogrid import SiapSearch

# Read command line arguments
parser = OptionParser()
parser.add_option("-b", "--broadcast", action='store_true', default=False)
(options, args) = parser.parse_args()

# If we are going to send the tables to TOPCAT then start the plastic hub
if options.broadcast:
	acr.startplastic()
	time.sleep(2)

# Define list of objects
objects=['HH111', 'HH30', 'HH211', 'HH47', 'M16', 'Trifid', 'HH524',
         'Sigma Orionis', 'DG Tau', 'HL Tau', 'M16', 'IRAS 04302+2247']

# Define the name resolver service
s = sesame()

# Define the endpoint of the search service
siap = SiapSearch('ivo://cadc.nrc.ca/siap/hst')

# Create output directory if it does not exist
if not os.path.isdir('hst'):
	os.mkdir('hst')

# Loop for each object
for obj in objects:
	coords, ra, dec = s.resolve(obj)
	ofile = 'hst/%s.vot' % obj.replace(' ','_').replace('+','p')
	if not os.access(ofile, os.F_OK):
		res = siap.execute(ra, dec, 30.0/3600.0)
		open(ofile,'w').write(res)
		print obj, ofile
	if options.broadcast:
		acr.plastic.broadcast(ofile, 'TOPCAT')

	