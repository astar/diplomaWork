import pyfits, numpy as np

def getFits(file):
    """ Read fits file. Convert wavelength to angstroms """ 
    data = pyfits.getdata('test.fit')
    w = lambda x : 10.0**(3.5796 + x*10.0**(-4))
    x = np.arange(1,data[0].size + 1)
    xx  = w(x) # convert to actual wavelenght
    return xx, data[0]

