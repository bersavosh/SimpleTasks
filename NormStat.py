#! /astro_sw/anaconda2/bin/python
# A simple scripts to calculate sigma values and confidence levels for normal distribution.

import numpy as np
import sys
import scipy.stats as sts

def norm(obs=3, mean=0.0, sd = 1.0):
    dif = abs(mean-obs)
    print obs,'is',abs(mean-obs)/sd,'sigma away from mean of',mean,'with sd of',sd
    print abs(mean-obs)/sd,'sigma confidence corresponds to:'
    print (sts.norm.cdf(mean+dif,mean,sd)-sts.norm.cdf(mean-dif,mean,sd))*100, '% Confidence level (two-sided)'
    print '1 in ',round(1/(1-(sts.norm.cdf(mean+dif,mean,sd)-sts.norm.cdf(mean-dif,mean,sd))))
    print sts.norm.cdf(mean+dif,mean,sd)*100, '% Confidence level (one-sided)'
    print '1 in ',round(1/(1-sts.norm.cdf(obs,mean,sd)))

mean = 0.0
sd = 1.0

if len(sys.argv) == 2:
    obs = eval(sys.argv[1])
elif len(sys.argv) == 3:
    obs = eval(sys.argv[1])
    mean = eval(sys.argv[2])
elif len(sys.argv) == 4:
    obs = eval(sys.argv[1])
    mean = eval(sys.argv[2])
    sd = eval(sys.argv[3])
elif len(sys.argv) > 4:
    print 'Error: too many arguments.'
    print 'To use: > normstat <OBSERVED VALUE> [MEAN] [STANDARD DEVIATION]'
    quit()

if len(sys.argv) < 2:
    print 'To use: > normstat <OBSERVED VALUE> [MEAN] [STANDARD DEVIATION]'
    quit()

norm(obs,mean,sd)
