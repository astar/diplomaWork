#!/usr/bin/python

import math as m, os, sys, pyfits as pf, numpy as np, matplotlib.pyplot as plt

if len(sys.argv) == 2:
    file = sys.argv[1]
else:
    file = 'test.fit'

print 'file: ' + file

bin = 4

def readFile(file):
    """ Read fits file """
    hdu = pf.open(file)
    data = hdu[1].data

    # original
    x = data.field('WAVE')
    y = data.field('FLUX')
    return x,y
    
def reduce(x,y,bin):
    """ Reduce bin pixel into 1"""
    size = x.size/bin
    l = 0
    xx = x[:x.size-1:bin]
    yy = list()
    for i in range(0,size):
        s = 0
        for j in range(0,bin):
            s = s + y[l]
            l+=1
        yy.append(s/bin)
    return xx, yy

def convolution(x,y,sigma):
    """ perform convolution on data """

    yy = 1/(m.sqrt(2*np.pi)*sigma)*np.exp(-x**2/(2*sigma**2))


def plot(x,y,xx,yy):
    """ Plot the result with shared axes"""
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    graph1 = ax1.plot(x,y, 'r')
    
    ax2 = fig.add_subplot(212,sharex=ax1,sharey=ax1  )
    graph2 = ax2.plot(xx,yy, 'r')
    ax2.set_xlabel("$Wavelenght [\\AA]$")                                                                            
#    ax2.set_ylabel("$Energy [10^{-17} erg/s/cm^2/\\AA]$") 
    plt.draw()
    plt.show()

def saveData(file,xx,yy):
    sep = '\t'
    f = open(file,'w')
    for x, y in zip(xx,yy):
        f.write(str(x) + sep + str(y) + '\n')    
    f.close()


x,y = readFile(file)
xx, yy = reduce(x,y,bin)
plot(x,y,xx,yy)
name, ext = os.path.splitext(file)
#saveData(name + '.dat',xx,yy)
