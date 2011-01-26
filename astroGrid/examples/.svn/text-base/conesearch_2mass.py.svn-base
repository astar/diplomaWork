#!/usr/bin/python
"""
Given an input list od objects, queries the 2MASS catalogue returning a 
VOTable for each object.
"""
import os
from astrogrid import ConeSearch
from astrogrid.utils import broadcast, read_votable

# Get the table from the web
import urllib
urllib.urlretrieve('http://www2.astrogrid.org/science/documentation/workbench-advanced/advanced-usage/scripting-user-s-guide/sample.vot', 'sample.vot')

# Read input list of ra, decs from VOTable
vot=read_votable('sample.vot')
id = vot['ID_IDENTIFIER']
ra = map(float, vot['POS_EQ_RA_MAIN'])
dec = map(float, vot['POS_EQ_DEC_MAIN'])

# We are going to query 2MASS at RoE
ivorn = 'ivo://wfau.roe.ac.uk/twomass-dsa/cone'
cone = ConeSearch(ivorn)

nsrc = len(ra) # Number of sources
radius=0.1  # Search radius in degrees

print 'Starting Query: %d objects' % nsrc

# However this is just an example so we select a couple
nsrc = 2

# Create out/ directory in local disk.
if not os.access('out', os.R_OK): os.makedirs('out')

for i in range(nsrc):
	res = cone.execute(ra[i], dec[i], radius)
	# Uncomment the following line if you want to send the output to TOPCAT
	# broadcast(res)
	ofile = id[i].replace(' ','_')
	print 'Writting 2mass_%s.vot' % ofile
	open(os.path.join('out', '2mass_%s.vot' % ofile), 'w').write(res)

