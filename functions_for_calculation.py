import numpy as np
L1 = np.sqrt(np.square(5)+np.square(26))
L2 = np.sqrt(15*15+36*36)
L2_precise = np.sqrt(15*15+36*36+7*7)

ctau = 1
beta = 1
gamma = 1
weight_approx = np.exp(-L1/(ctau*beta*gamma))-np.exp(-L2/(ctau*beta*gamma))

def f_function(mc, mb): # The real f_function is not this one
    mc = 1.27
    mb = 4.18
    return mc/mb


def calculate_Sin(mphi, Br1 = 6*10**(-8), Br2 = 0.9, g = 2):
    default_Br1 = 6*10**(-8)
    default_Br2 = 0.9
    default_g = 2
    mt = 172.76 
    mb = 4.18
    mw = 80.379
    mc = 1.27
    Vts = -0.0405
    Vtb = 0.9991
    Vcb = 0.041
    para1 = (256 * np.square(np.pi))/(27 * np.square(g))
    para2 = (np.square(mt)*np.square(mt))/(np.square(mb)*np.square(mw))
    para3 = np.square(1-(mphi/mb))/f_function(mc, mb)
    para4 = np.square(Vts*Vtb/Vcb)
    Sin_square = (Br1/Br2) * para1 / (para2 * para3 * para4)
    return Sin_square

# The calculation formula is in "Searching for Long-lived Particles: A Compact Detector for Exotics at LHCb
#By Vladimir V. Gligorov,1 Simon Knapen,2, 3 Michele Papucci,2, 3 and Dean J. Robinson4"
