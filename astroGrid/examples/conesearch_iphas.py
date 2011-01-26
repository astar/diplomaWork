#!/usr/bin/python
"""
Given the coordinates of an objects in the command line and a search
radius -- all in degrees -- search the IPHAS catalogue for objects
within the search radius from the given position.

Example:

   conesearch_iphas.py -o iphas.vot 15.45 60.0 0.1
"""
__id__='$Id: conesearch_iphas.py 62 2007-05-10 13:04:34Z eddie $'

import os
from astrogrid import ConeSearch
from astrogrid.plastic import broadcast
from optparse import OptionParser

parser=OptionParser()
parser.add_option("-o", "--out", default='iphas.vot',
                  help="Output file.")
(options, args) = parser.parse_args()

ra, dec, radius = args

# We add here the IVORN of the IPHAS service
ivorn = 'ivo://uk.ac.cam.ast/iphas-dsa-catalog/IDR'
cone = ConeSearch(ivorn)

print 'Querying %s %s %s' % (ra, dec, radius)
res = cone.execute(ra, dec, radius, dsatab='PhotoObjBest')
# Uncomment the following line if you want to send the output to TOPCAT
# broadcast(res)
print 'Writting %s' % options.out
open(options.out, 'w').write(res)


