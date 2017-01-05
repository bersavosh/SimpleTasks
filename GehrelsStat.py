#! /bin/python
# A small code to estimate confidence intervals for low-count events
# Based on Gehrels+86

import numpy as np
import sys
import scipy.stats as sts


def gehrels(x,cl=0.8413, step = 0.001):
    """
    The main function to compute the interval:
    Parameters:

    x: number of observations/events

    cl: confidence level to estimate, default value = 0.8413 (1-sigma)

    step: size of steps (smaller more accurate), default value = 0.001
    """
    if x < 0.0:
        print 'Error: negative values not accepted.'
        return None

    if x == 0:
        lower = 0.0

    else:
        lower = x
        while abs(sts.poisson.cdf(x-1,lower)-cl) > step:
            lower -= step
    
    upper = x
    while abs(1-sts.poisson.cdf(x,upper)-cl) > step:
        upper += step
    
    return round(lower,5),round(upper,5)

CL = 0.8413
Step = 0.001

if len(sys.argv) == 2:
    obs = eval(sys.argv[1])
elif len(sys.argv) == 3:
    obs = eval(sys.argv[1])
    CL = eval(sys.argv[2])
elif len(sys.argv) == 4:
    obs = eval(sys.argv[1])
    CL = eval(sys.argv[2])
    Step = eval(sys.argv[3])
elif len(sys.argv) > 4:
    print 'Error: too many arguments.'
    print 'To use: > gehrels <N_OBSERVATION> [CONFIDENCE INTERVAL] [STEP SIZE]'
    quit()

if len(sys.argv) < 2:
    print 'To use: > gehrels <N_OBSERVATION> [CONFIDENCE INTERVAL] [STEP SIZE]'
    print 'example: gehrels 34 0.84'
    quit()

res = gehrels(obs,CL,Step)
print 'For',obs,'events,',CL,'confidence level limits are:'
print res[0],res[1]


