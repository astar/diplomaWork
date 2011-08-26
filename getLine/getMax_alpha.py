#!/usr/bin/python
import os, sys, numpy as np, pyfits as pf
#import os, sys, numpy as np, matplotlib.pyplot as plt, pyfits as pf

if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    file = '4_her.dat'

ond = 0
if len(sys.argv) == 3:
    if sys.argv[2] == '1':
        ond = 1 # Ondrejov Fit

print 'file: ' + file


def getOnd(file):
    """ Load data from file"""
    data = np.loadtxt(file)
    x = data[:,0]
    y = data[:,1]
    # x = x[(x < spLines[0] + spRange) & (x > spLines[0] - spRange)]
    # y = y[(x < spLines[0] + spRange) & (x > spLines[0] - spRange)]
    return x, y

def getSDSS(file,range):
    """ Load data from file"""
    data = pf.getdata(file)
    w = lambda x : 10.0**(3.5796 + x*10.0**(-4))
    xx = np.arange(1,data[0].size + 1)
    x  = w(xx) # convert to actual wavelenght
    y = data[0]
    xx = x[(x < range[1]) & (x >range[0]  )]
    yy = y[(x < range[1]) & (x >range[0]  )]

    return xx, yy


def saveData(file,xx,yy):
    name, ext = os.path.splitext(file)
    name = name + '.nrm'
    print 'saving to file: \t' + name
    sep = '\t'
    f = open(name,'w')
    for x, y in zip(xx,yy):
        f.write(str(x) + sep + str(y) + '\n')    
    f.close()

def saveMax(file,value):
    name, ext = os.path.splitext(file)
    f = open('result_alpha.dat','a')
    sep = '\t'
    f.write(name  + sep + str(value) + '\n')
    f.close()

    


def plot(x,y,fx,fy,nx,ny,rx,m):
    """ Plot the result """

    xrange = [6270,6700]
#    xrange = [4750,5010]
    xticks = np.arange(6300,6700,50)
#    xticks = np.arange(4760,5020,50)
    
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)

    
#    plt.xlim(xrange[0],xrange[1])
#    plt.xticks(xticks)

    graph1 = ax1.plot(x,y,'b',fx,fy, 'r')
    graph2 = ax2.plot(nx,ny,'b',rx,m,'r')

    ax1.set_xlim(xrange[0],xrange[1])
    ax2.set_xlim(xrange[0],xrange[1])

    ax1.set_xticks(xticks)
    ax2.set_xticks(xticks)

#    ax1.set_ylabel("$Energy [10^{4} ADU]$")
    ax1.set_ylabel("$Energy [10^{-17} erg/s/cm^2/\\AA]$")
    ax2.set_ylabel("$Energy [normalized]$")
    ax2.set_xlabel("$Wavelenght [\\AA]$")

    
    plt.draw()
    plt.show()

def getMax(x,y,line,range):
    """ Return maximum value of range in the spectrum"""
    xrange = x[(x < line + range) & (x > line - range)]
    yrange = y[(x < line + range) & (x > line - range)] - 1
    maximum = yrange.max()
    minimum = yrange.min()
    if abs(maximum)  > abs(minimum):
        extrem = ( maximum + 1)
        sgn = np.sign(maximum)
    else:
        extrem = (minimum + 1)
        sgn = np.sign(minimum)
        
    return xrange, extrem, sgn

# def getMax(x,y,line,range):             # 
#     """ Return maximum value of range in the spectrum"""
# #    xrange = x[(x < line + range) & (x > line - range)]
# #    yrange = y[(x < line + range) & (x > line - range)] - 1
#     y = y - 1
#     maximum = y.max()
#     minimum = y.min()
#     if maximum  > abs(minimum):
#         extrem = maximum + 1
#     else:
#         extrem = minimum + 1
#     return x, extrem



# MAIN

spLines = [6564.614,4861.363 ]
spRange = 25
spMinHight = 0                          # save threshold

start = 10
size = 50

ondRange = [[6252,6764],[4759,5011]]                # Ondrejov range of wavelenghts

# Create function to fit
# (take first and last <size> elements from spectra) 

if ond:
    x,y = getOnd(file)
else:
    x,y = getSDSS(file,ondRange[0])    

    
x1 = x[start:start+size]
x2 = x[-1*(start+size):-1*(start)]
y1 = y[start:start+size]
y2 = y[-1*(start+size):-1*(start)]

xx = np.append(x1,x2)
yy = np.append(y1,y2)

#fit line
(a,b) = np.polyfit(xx,yy,1)

# define line function
fy = a*x + b

#normalize spectrum

ny = y/fy 

#Save normalized spectrum
#saveData(file,x,ny)

#Save max value of the range
#xrange, maximum = getMax(x,ny,spLines[0],spRange) # Halpha
xrange, maximum, sgn = getMax(x,ny,spLines[0],spRange) # HBeta
saveMax(file,sgn*maximum)

ymax = np.zeros(xrange.size) + maximum

#plot(x,y/10**4,x,fy/10**4,x,ny,xrange,ymax)
#plot(x,y,x,fy,x,ny,xrange,ymax)

