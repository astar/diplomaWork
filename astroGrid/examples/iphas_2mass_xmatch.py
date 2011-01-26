#!/usr/bin/python

# author: Eduardo Gonzalez-Solares 	- 20070821
# mods:   Nicholas Walton		- 20080111

# this is a cross match of 2MASS against IPHAS
# so gives j,h,k and r,i, Ha fluxes for sources around IC5070 

import sys
from math import cos, radians
import time
from astrogrid import acr
from astrogrid import Applications, DSA, MySpace

# Log in
acr.login('leicester')

# Coords for IC 5070
ra, dec = 312.75, 44.37

# Output directory
output_dir = '#iphas'

# Define box bounding box
ra1 = ra - 0.25 / cos(radians(ra))
dec1 = dec - 0.25
ra2 = ra + 0.25 / cos(radians(ra))
dec2 = dec + 0.25

# Query 2MASS
twomass = DSA('ivo://wfau.roe.ac.uk/twomass-dsa/wsa/ceaApplication')
job1 = twomass.query('select * from twomass_psc as x where x.ra between %s and %s and x."dec" between %s and %s' % (ra1, ra2, dec1, dec2),
                     saveAs='%s/twomass.vot' % output_dir)

while job1.status() in ['INITIALIZING', 'RUNNING', 'UNKNOWN']:
	time.sleep(10)
	
if job1.status() == 'ERROR':
	print 'Error querying 2MASS database'
	print job1.results()[0]
	sys.exit()
	
print '2MASS Query: ',job1.status()


# Query IPHAS
iphas = DSA('ivo://uk.ac.cam.ast/iphas-dsa-catalog/IDR/ceaApplication')
job2 = iphas.query('select * from PhotoObjBest as x where x.ra between %s and %s and x."dec" between %s and %s' % (ra1, ra2, dec1, dec2),
                     saveAs='%s/iphas.vot' % output_dir)

while job2.status() in ['INITIALIZING', 'RUNNING', 'UNKNOWN']:
	time.sleep(10)
	
if job2.status() == 'ERROR':
	print 'Error querying IPHAS database'
	print job2.results()[0]
	sys.exit()
	
print 'IPHAS Query: ',job1.status()

m = MySpace()

# Perform Xmatch using 1.5 arcsec radius

# this uses the TopCat STILTS library to perform the cross match

app = Applications('ivo://uk.ac.starlink/stilts', 'tmatch2')
app.inputs['tmatch2_in1']['value'] = '%s/iphas.vot' % output_dir
app.inputs['tmatch2_in2']['value'] = '%s/twomass.vot' % output_dir
app.inputs['tmatch2_values1']['value'] = 'ra dec'
app.inputs['tmatch2_values2']['value'] = 'ra dec'
app.inputs['tmatch2_params']['value'] = '1.5'
app.inputs['tmatch2_ifmt1']['value'] = '(auto)'
app.inputs['tmatch2_ifmt2']['value'] = '(auto)'
app.inputs['tmatch2_ofmt']['value'] = 'vot'

app.inputs.pop('tmatch2_icmd1')
app.inputs.pop('tmatch2_icmd2')
app.inputs.pop('tmatch2_ocmd')

app.outputs['tmatch2_out']['value'] = '%s/iphas_twomass.vot' % output_dir
job = app.submit()


while job.status() in ['INITIALIZING', 'RUNNING', 'UNKNOWN']:
	time.sleep(10)
	
if job.status() == 'ERROR':
	print 'Error running xmatch'
	sys.exit()
	
print 'Xmatch: ', job.status()

# If completed ok the retrieve the result. Print the error message otherwise.	
if job.status()=='COMPLETED':
	url = job.results()[0]
	m = MySpace()
	m.readfile(url, ofile='iphas2mass-xmatch.vot')
else:
	print job.results()[0]
	





