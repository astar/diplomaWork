#!/usr/bin/python
"""
Executes two cone searches to UKIDSS DR1 and SDSS and cross matches the resultant tables
retrieving the cross match outout to local disk.
"""

import time, urllib
from astrogrid import acr
from astrogrid import Applications, ConeSearch, MySpace

# Log in (we need this to save the results in VOSpace)
acr.login()

# Perform cone searches to UKIDSS and SDSS. We are saving the results to VOSpace and these
# will be the two tables we want to cross match.

ra = 152.8
dec = 8.5
radius = 0.1

cone1 = ConeSearch("ivo://wfau.roe.ac.uk/ukidssDR1-dsa/wsa")
vot1 = cone1.execute(ra, dec, radius, saveAs='#cones/ukidsslas.vot', dsatab='lasSource', clobber=True)

cone2=ConeSearch('ivo://wfau.roe.ac.uk/sdssdr5-dsa/dsa')
vot2 = cone2.execute(ra, dec, radius, dsatab='PhotoObjAll', saveAs='#cones/sdsslas.vot', clobber=True)

# Define the cross match application to use and fill in parameters
# See http://www.star.bris.ac.uk/~mbt/stilts/sun256/secA.14.1.html for more info
app = Applications('ivo://uk.ac.starlink/stilts', 'tmatch2')

# .. inputs
app.inputs['tmatch2_in1']['value']=vot1
app.inputs['tmatch2_in2']['value']=vot2
app.inputs['tmatch2_params']['value']="1.0"
app.inputs['tmatch2_values1']['value']="ra dec"
app.inputs['tmatch2_values2']['value']="ra dec"
app.inputs['tmatch2_ofmt']['value'] = 'votable-tabledata'

# .. outputs
app.outputs['tmatch2_out']['value']='#cones/lassdss-xmatch.vot'

# .. remove unncessary (optional) parameters
app.inputs.pop('tmatch2_icmd1')
app.inputs.pop('tmatch2_icmd2')
app.inputs.pop('tmatch2_ocmd')

# Submit the application to the system and wait for completion
job = app.submit()

while job.status() not in ['COMPLETED', 'ERROR']:
	time.sleep(10)
	
# If completed ok the retrieve the result. Print the error message otherwise.
if job.status()=='COMPLETED':
	url = job.results()[0]
	m = MySpace()
	m.readfile(url, ofile='lassdss-xmatch.vot')
else:
	print job.results()[0]
	
	
