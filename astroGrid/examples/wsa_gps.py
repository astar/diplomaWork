#!/usr/bin/python
"""
Sends a query to the WFCAM Science Archive UKIDSS DR1
and saves the result to a file in local disk.

Usage:

    python wsa_gps.py

will write a file named wsa_gps_res.vot to the current directory. 

History:

   20071212 Written by E. A. Gonzalez-Solares

"""
import urllib
from time import sleep
from astrogrid import acr, DSA, MySpace

# Uncomment if automatic login is not enabled
acr.login()

# Define SQL here
# This query selects for each source, the x and y position in the detector as well as the
# size of the detector in which it was detected and the pixel scale. Only sources which are
# more than 10 arcsec away from the chip edges are returned in a search box
sql="""SELECT TOP 10000
          s.sourceID, s.ra, s."dec", s.jmhPnt, s.pStar, s.pGalaxy, s.pNoise, s.pSaturated, 
          s.jAperMag3, s.jAperMag3Err, s.jClass, s.hAperMag3, s.hAperMag3Err, s.hClass, 
          s.k_1AperMag3, s.k_1AperMag3Err, s.k_1Class, d.x, d.y, m.xSize, m.ySize, c.xPixSize, 
          c.yPixSize 
      FROM 
          gpsSource AS s, gpsDetection AS d, MultiframeDetector AS m, CurrentAstrometry AS c 
      WHERE
          s.k_1ObjId = d.objID AND d.multiframeID = m.multiframeID AND d.extNum = m.extNum AND
          d.multiframeID = c.multiframeID AND d.extNum = c.extNum AND
          d.x*c.xPixSize>10 AND d.y*c.yPixSize>10 AND
          (m.xSize-d.x)*c.xPixSize>10 AND (m.ySize-d.y)*c.yPixSize>10"""
			
# Define the enpoint service
dsa=DSA('ivo://wfau.roe.ac.uk/ukidssDR1-dsa/wsa/ceaApplication')

# Write all the SQL in one line
sql = ' '.join(sql.split())

# Submit query and save result to VOSpace
r=dsa.query(sql, saveAs='#dsa/wsa_gps.vot')

# Wait until query status is completed
while r.status()<>'COMPLETED':
	sleep(10)
	
# If completed ok the retrieve the result. Print the error message otherwise.	
if r.status()=='COMPLETED':
	url = r.results()[0]
	m = MySpace()
	m.readfile(url, ofile='wsa-gps.vot')
else:
	print job.results()[0]
