#!/usr/bin/python
"""
Given a list containing just the name of the objects, resolve them and perform 
a SIAP search saving the resultant VOTables to the local disk.

This version uses direct XMLRPC calls to the ACR.
"""

from astrogrid import acr

inputfile='objects.txt'

# Read file skipping lines which start with hash
objects = [items.strip() for items in open(inputfile).readlines() if items[0]<>'#']

# Initialize siap service search and name resolver
siap = acr.ivoa.siap
sesame = acr.vizier.sesame

# Loop for each object of the list, query Vizier to get coordinates and execute
# the SIAP search. The resultant VOTable is then saved to a file in the local
# directory named after the object.
for obj in objects:
    info = sesame(obj)
    query = siap.constructQueryF('ivo://roe.ac.uk/services/SIAPDR4-images', \
	        info['ra'], info['dec'], 30.0/3600.0, 'ALL')
    votable = siap.executeVotable(query)
    open('%s.vot' % obj, 'w').write(votable)
    
# Same loop as above. Now we save the VOTables to MySpace
# We convert spaces to underscores in the saved filename due to MySpace complains
# We do not overwrite existing files. We have to login first...    
acr.astrogrid.community.login(username, password, community)
for obj in objects:
	info = sesame(obj)
	query = siap.constructQueryF('ivo://roe.ac.uk/services/SIAPDR4-images', \
	        info['ra'], info['dec'], 30.0/3600.0, 'ALL')
	ofile = '#siap/%s.vot' % obj.replace(' ','_')
	home = acr.astrogrid.myspace.getHome()
	ofile = home + ofile
	if acr.astrogrid.myspace.exists(ofile):
		continue
	siap.executeAndSave(query, ofile)
	
	
