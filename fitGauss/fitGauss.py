#!/usr/bin/python

import sys, numpy as np, matplotlib.pyplot as plt, scipy.optimize as opt, scipy.stats as stats


if len(sys.argv) == 2:
    file = sys.argv[1]
else:
    file = 'gauss.dat'

print 'file: ' + file


spLine = 6560
spRange = 20
title = r'$H_{\alpha}$ for ' + file

data = np.loadtxt(file)

line = data[(data[:,0]< spLine + spRange) & (data[:,0] > spLine - spRange)]
xdata = line[:,0]
ydata = line[:,1]

# fit

def model(t, coeffs):
    return coeffs[0] + coeffs[1] * np.exp( - ((t-coeffs[2])/coeffs[3])**2 )


def plot(file,xdata,ydata,model,x,title):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    dGraph = ax.plot(xdata, ydata, 'r')
    mGraph = ax.plot(xdata, model(xdata, x),'b')
    ax.set_title(title)
    fig.savefig(file[:-4] + '.png')
    fig.show()
def saveData(name,emisson,value):
    f = open('emission.dat','a')
    sep = ','
    f.write(name + sep + str(emission) + sep + str(value) + '\n')
    f.close()

# try to figure out whether pos or neg based on the minimum width of the pos/neg peaks

Lstddev = xdata[ydata<ydata.mean()].std()
Hstddev = xdata[ydata>ydata.mean()].std()

if Hstddev <= Lstddev:
    emission = 1
    amplitude = ydata.max() - np.median(ydata)
else:
    emission = 0
    amplitude = ydata.min() - np.median(ydata)

# initial guess
noise = np.median(ydata)
center = spLine
width = 1

x0 = np.array([noise, amplitude, spLine, width], dtype=float)

def residuals(coeffs, y, t):
    return y - model(t, coeffs)

x, flag = opt.leastsq(residuals, x0, args=(ydata, xdata))


if 1:
    print amplitude, x[1]
    print 'emission: ' + str(emission)
    print 'fit: ' +  str(x)
    plot(file,xdata, ydata, model, x, title )
    saveData(file, emission, x[1])
