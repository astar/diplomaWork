#!/usr/bin/python
"""This example shows how to submit a list of ra,dec positions to SDSS DR5
running 4 in parallel.
"""

import sys, time
import math
import random

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

# Define the command to execute and the pool size (4 in parallel)
pool = easy_pool(cone.execute)
pool.start_threads(4)

# Send the commands to the pool
for i in range(nsrc):
    input = (ra[i], dec[i], radius[i])
    pool.put(input)
    
# Print information while executing
i=0
while 1:
    p = pool.qinfo()
    print "Time: %3d sec    Queued: %2d    Running: %2d    Finished: %2d" % \
                                        (i, p[1], nsrc-p[1]-p[3], p[3])
    time.sleep(2)
    i=i+2
    if p[3]==nsrc: break
    
pool.stop_threads()

# Save results to local disk
i=0
for res in pool.get_all():
	i = i+1
	open('sdss%02d.vot' % i, 'w').write(res)
	
