import sys, numpy as np, matplotlib.pyplot as plt, pyfits as pf

if len(sys.argv) == 2:
    file = sys.argv[1]
else:
    file = 'test.fit'

print 'file: ' + file

def gauss(size, s):
    """ Returns a normalized 2D gauss kernel array for convolutions """
    size = int(size)    
    #print size, sizey    
    sigma = float(np.sqrt(s))
    x = np.arange(-size, size)
    g = 1/(np.sqrt(2*np.pi)*sigma)*np.exp(-x**2/(2.0*sigma**2))
    return x, g / g.sum()

def readFile(file):
    """ Read fits file """
    hdu = pf.open(file)
    data = hdu[1].data

    # original
    x = data.field('WAVE')
    y = data.field('FLUX')
    return x,y

def getData(file):
    """ Load data from file"""
    data = np.loadtxt(file)
    x = data[:,0]
    y = data[:,1]
    return x, y

def convolution(f, g):
    """ Convolve two functions"""
    fg = np.convolve(g,f,'same')
    return fg

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

def plot(xx,yy):
    """ Plot the result with shared axes"""
    fig = plt.figure()
    nsp = len(xx)
    sp = range(1,nsp+1)              # number of subplots
    ax = list()
    for x,y,s in zip(xx,yy,sp):
        subplot = int(str(nsp) + '1' + str(s))
        if s > 2:
            ax.append(fig.add_subplot(subplot, sharex=ax[1],sharey=ax[1]   ))
        else:
            ax.append(fig.add_subplot(subplot))
            
        graph = ax[s-1].plot(x,y, 'r')
#    ax2 = fig.add_subplot(412  )
#    graph2 = ax2.plot(xx,yy, 'r')

#    ax2.set_ylabel("$Energy [10^{-17} erg/s/cm^2/\\AA]$") 

#    ax3 = fig.add_subplot(413,sharex=ax2,sharey=ax2  )
#    graph3 = ax3.plot(xxx,yyy, 'r')

#    ax4 = fig.add_subplot(414,sharex=ax2,sharey=ax2  )
#    graph4 = ax4.plot(xxxx,yyyy, 'r')

#    ax3.set_xlabel("$Wavelenght [\\AA]$")                                                                            
    plt.draw()
    plt.show()

gSize = 100
s = 39.8
gx, gy = gauss(gSize, s)
fx, fy = readFile(file)
fg = convolution(fy,gy)
rx, ry = reduce(fx,fg,4)
#plot(gx,gy,fx,fy,fx,fg,rx,ry)
plot([gx,fx,fx,rx],[gy,fy,fg,ry])
