#!/usr/bin/python
#import sys
#sys.path.append("../getFits/")
import sys, getFits, numpy as np

if len(sys.argv) == 2:
    file = sys.argv[1]
else:
    file = 'test.fit'

print 'file: ' + file


#spLines = [6564.614, 4861.363,4342,4103, 6506]
spLines = [6564.614]
spRange = 25
spMinHight = 0                          # save threshold
data = np.loadtxt(file)
yy = list()


for spLine in spLines:
    yy.append( data[(data[:,0]< spLine + spRange) & (data[:,0] > spLine - spRange),1])

def saveData(name,value):
    f = open('ond.dat','a')
    sep = ','
    f.write(name  + sep + sep.join(value) + '\n')
    f.close()


#if yy[0] + spMinHight < yy.max() and yy[-1] +  spMinHight < yy.max() :
#    saveData(file, yy.max() - yy.mean())
#else:
#    print "no emission"

data = list()

for y in yy:
    data.append( str(y.max() - np.median(y)))

# We only test H-aplha emission    
if yy[0].max() - np.median(yy[0]) > np.median(yy[0]) - yy[0].min():
    saveData(file, data)
else:
    print file + ":\t no emission"
