#!/usr/bin/python
import sys, pyfits, numpy as np, pylab as p, matplotlib.pyplot as plt

#show position of some lines
Halpha = 6564.614


if len(sys.argv) == 2:
    file = sys.argv[1]
else:
    print 'This utility plot fits file passed as argument'


def read(file):
    """ Read fits file. Convert wavelength to angstroms """ 
    data = pyfits.getdata(file)
    w = lambda x : 10.0**(3.5796 + x*10.0**(-4))
    x = np.arange(1,data[0].size + 1)
    xx  = w(x) # convert to actual wavelenght
    return np.asarray([xx, data[0]])

def plot(file,xdata,ydata,spLine):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    graph = ax.plot(xdata,ydata, 'r')
    ax.set_title(file)
    ax.set_xlabel("$Wavelenght [\\AA]$")                                                                            
    ax.set_ylabel("$Energy [10^{-17} erg/s/cm^2/\\AA]$")
    ax.axvline(x=spLine, color = 'g', ls ='--')
    
    #fig.savefig(file[:-4] + '.png')
    #spLines
    #ax.annotate(
    #    r'$H_{\alpha}$', xy=(spLine, 200),  xycoords='data',
    #            xytext=(-30, -30), textcoords='offset points',
    #            arrowprops=dict(arrowstyle="->",
    #                            connectionstyle="arc3,rad=.2")
    #            )


    plt.show()

data = read(file)
plot(file, data[0,:], data[1,:], Halpha)


