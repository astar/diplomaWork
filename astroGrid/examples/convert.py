#!/usr/bin/python
"""
Convert a file from one format to another using STILTS.
"""

import time, urllib
from astrogrid import acr
from astrogrid import Applications, MySpace, ConeSearch

acr.login()

# Perform a cone search to NED to obtain a VOTable
cone = ConeSearch("ivo://ned.ipac/Basic_Data_Near_Position")
vot = cone.execute(242.811, 54.596, 0.1, saveAs='#cones/ned.vot')

# Use tcopy (STILTS) to do the conversion
app = Applications('ivo://uk.ac.starlink/stilts','tcopy')

app.inputs['tcopy_in']['value']='#cones/ned.vot'
app.inputs['tcopy_ifmt']['value']='VOTABLE'
app.inputs['tcopy_ofmt']['value']="FITS"

app.outputs['tcopy_out']['value']='#cones/ned.fits'

res=app.submit()
