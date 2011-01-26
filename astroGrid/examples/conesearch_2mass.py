#!/usr/bin/python
"""
Given an input table containig a list of objects, 
queries the 2MASS catalogue returning a VOTable for each object.

History:
   Mar 2008. Updated IVORN for registry version 1 included in VODesktop 1.0 [EGS]
   Written by E. A. Gonzalez-Solares [EGS]

"""

import os
from astrogrid import ConeSearch
from astrogrid.utils import read_votable

# Get the table from the web but this can be a file in local disk
# (in which case you can remove the next three lines)
import urllib
url = 'http://help.astrogrid.org/raw-attachment/wiki/Help/IntroScripting/AstrogridPython/sample.vot'
urllib.urlretrieve(url, 'sample.vot')

# Read input list of ra, decs from VOTable
vot=read_votable('sample.vot')
id = vot['ID_IDENTIFIER']
ra = map(float, vot['POS_EQ_RA_MAIN'])
dec = map(float, vot['POS_EQ_DEC_MAIN'])

# We are going to query 2MASS at RoE
ivorn = 'ivo://wfau.roe.ac.uk/twomass-dsa/wsa'
cone = ConeSearch(ivorn)

nsrc = len(ra) # Number of sources
radius = 0.1  # Search radius in degrees

print 'Starting Query: %d objects' % nsrc

# However this is just an example so we select a couple
nsrc = 2

# Uncomment the following line to perform the search for all objects
#nsrc = len(ra)

# Create out/ directory in local disk if it does not exist
if not os.access('out', os.R_OK): os.makedirs('out')

# Loop for each object
for i in range(nsrc):
	res = cone.execute(ra[i], dec[i], radius, dsatab='twomass_psc')
	ofile = id[i].replace(' ','_')
	print 'Writting 2mass_%s.vot' % ofile
	if res:
		open(os.path.join('out', '2mass_%s.vot' % ofile), 'w').write(res)

