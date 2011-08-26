import core, rec, numpy as np

def read(file):
    """ Read fits file. Convert wavelength to angstroms """ 
    data = core.getdata(file)
    w = lambda x : 10.0**(3.5796 + x*10.0**(-4))
    x = np.arange(1,data[0].size + 1)
    xx  = w(x) # convert to actual wavelenght
    return np.asarray([xx, data[0]])

