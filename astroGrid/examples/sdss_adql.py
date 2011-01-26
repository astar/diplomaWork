#!/usr/bin/python

import time, urllib
from astrogrid import acr, DSA, MySpace

# Login in Leicester account
acr.login()

m = MySpace()

# Define the service to query
dsa=DSA('ivo://wfau.roe.ac.uk/sdssdr5-dsa/dsa/ceaApplication')

# Construct the SQL
tsql = """SELECT a.ra, a."dec", a.psfMag_g, a.psfMag_r FROM PhotoTag AS a """
tsql += """WHERE a.ra>110 AND a.ra<230 AND a."dec">%s AND a."dec"<=%s AND  (a.psfMag_g-a.psfMag_r <0.4 )  AND """
tsql += """a.psfMag_r>20.0 AND a.psfMag_g>0 AND a.mode=1 AND a.probPSF=1"""

# Looop for range of declinations
for i in range(0, 60, 2):
	sql = tsql % (i, i+2)
	r = dsa.query(sql, saveAs='#cam/ndec%02d-%02d.vot' % (i,i+2))

	# Wait until completed
	time.sleep(10)
	while r.status() not in ['COMPLETED' , 'ERROR']:
		print r.status()
		time.sleep(10)

	print r.status()
	# If completed extract the URL of the saved file and save it to local disk
	# Note: this can change slightly in the next beta release
	if r.status() == 'COMPLETED':
		url = r.results()[0]
		m.readfile(url, ofile='ndec%02d-%02d.vot' % (i,i+2))
		print 'ndec%02d-%02d.vot' % (i,i+2)
		
	


