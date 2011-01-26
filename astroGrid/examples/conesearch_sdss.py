#!/usr/bin/python
"""This example shows how to submit a list of ra,dec positions to SDSS DR5.
"""

import sys, time
import random
import math

from astrogrid import ConeSearch
from astrogrid.threadpool import easy_pool

# Define the service endpoint IVORN
cone=ConeSearch('ivo://wfau.roe.ac.uk/sdssdr5-dsa/dsa', dsatab='PhotoObjAll')

# Generate 20 random positions.
# In real astronomy these would be read from a file
nsrc=20
ra=[random.random()*math.pi*2*math.degrees(1) for i in range(nsrc)]
dec=[(random.random()*math.pi-math.pi/2.)*math.degrees(1) for i in range(nsrc)]
radius=[0.001]*nsrc

for i in range(nsrc):
	res = cone.execute(ra[i], dec[i], radius[i])
	open('sdss%02d.vot' % (i+1), 'w').write(res)
	print i+1, 'sdss%02d.vot' % (i+1)
