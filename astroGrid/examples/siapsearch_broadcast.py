#!/usr/bin/python

import sys
from astrogrid import acr
from astrogrid import MySpace

idir='#siap/'+sys.argv[1]
print 'Reading images from %s' % idir

m = MySpace()
for filename in [f[2] for f in m.ls(idir) if f[2][-4:]=='fits']:
	print 'Loading %s' % filename
	acr.plastic.broadcast(idir+'/'+filename, 'Aladin')
	
	
	