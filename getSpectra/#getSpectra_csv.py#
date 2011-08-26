#!/usr/bin/python
import sys, re, numpy as np, astropysics.coords.coordsys as ac

if len(sys.argv) == 2:
    file = sys.argv[1]
else:
    file = 'test.fit'

print 'file: ' + file


def readInput(file):
    """ Read input data file with objects in format: """
    """ 12 54 36.8865\t-57 10 07.214 \n """
    #f = open(file,'r')                  
    #data = f.readlines()
    #f.close()
    data = np.loadtxt(file)
    return data

def createQuery(data):
    """ From raw data construct ra, dec """
    """ Convert to degrees """

    #ra = list()
    #dec = list()
    ssa = list()
    for line in data:
#        ra = ac.AngularCoordinate(line[0:10]).degrees # convert ra to degrees
#        dec = ac.AngularCoordinate(line[-13:-1]).degrees # convert dec to degrees
        ra = line[0]
        dec = line[1]
        ssaTemp = 'http://tvoserver/coude/coude.cgi?c=ssac&n=coude_ssa&REQUEST=queryData&POS=<ra>,<dec>&SIZE=1'
        ssaTemp = ssaTemp.replace('<ra>',"%0.3f" % ra)
        ssaTemp = ssaTemp.replace('<dec>',"%0.3f" % dec)
        ssa.append(ssaTemp)

    return ssa

def saveQuery(file, data):
    """ Just save the data """
    """"""
    f = open(file,'w')
    f.write("\n".join(map(lambda x: str(x), data)) + "\n")
    f.close()
 
    
data = readInput(file)
ssa = createQuery(data)
saveQuery('ssa_hip',ssa)
