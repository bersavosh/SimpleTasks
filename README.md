# LazyTools:
A small collection of naive scripts I've written to run things from the command line.

## 1. GehrelsStat:
A quick script to calculate confidence interval and significance for poisson distribution of events in the photon-starved regime. This is a lazy brute-force implementation of [Gehrels 1986](http://adsabs.harvard.edu/abs/1986ApJ...303..336G).

### To use: 
* Download the code.
* set the  the first line of the code to match your python (you can find your python by typing `which python` in the terminal).
* and set an alias for this file.
If you are using bash, then something like this in your `.bashrc` file:
`
alias gehrels="/PATH/TO/gehrels.py"
`
* Then it is ready for use in the command line.

### Examples:
`
$ gehrels <N_OBSERVATION> [CONFIDENCE INTERVAL] [STEP SIZE]
`
If only number of observations is provided, limits for 1-sigma confidence are returned and default step size is assumed.

## 2. NormStat:
Same as above but for gaussian distribution. Because I'm too forgetful to remember how many 9s there are after the decimal in a 5-sigma confidence!

## 3. GCcat:
A command line tool that returns information about a globular cluster from the [Harris Catalog](http://adsabs.harvard.edu/abs/1996AJ....112.1487H) ([2010 edition](http://www.physics.mcmaster.ca/~harris/Databases.html)).
