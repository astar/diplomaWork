#!/usr/bin/python
"""
Run the Montage application at IPAC.

Demonstrates how to remotely run a task and retrieve the results.

"""

import sys
import time, urllib
from astrogrid import acr
from astrogrid import Applications, MySpace
from astrogrid.utils import mkURI

# We need to login.
# Insert the credentials here if not already in ~/.python-acr
# acr.login(username, password, community)
acr.login()

# MySpace
m = MySpace()

# Application ID. This is the name of the application we are going to run.
# It can be obtained from a registry search.
id = 'ivo://astrogrid.cam/Montage/prototype/2MASS-mosaic'

# We fill in the application parameters
app = Applications(id)

# The inputs parameters are available by printing app.info
app.inputs['ra']['value'] = 312.75
app.inputs['dec']['value'] = 44.37
app.inputs['size']['value'] = 0.3
app.inputs['band']['value'] = 'K'

# We can construct a MySpace IVORN also using mkURI('#2mass/mosaic.fits')
app.outputs['out.fits']['value'] = '#2mass/mosaic.fits'

# We submit the application
task=app.submit()

# Wait until completed
time.sleep(10)
while task.status() <> 'COMPLETED':
	time.sleep(10)
	
print 'Image written to\n%s' % task.results()

# We read the mosaic from MySpace and save it to local disk
ofile = task.results()[1]
mosaic = m.readfile(ofile)
open('mosaic.fits', 'wb').write(mosaic)

# Now with Aladin running we can display the image 
acr.plastic.broadcast('#2mass/mosaic.fits')

acr.__del__()

