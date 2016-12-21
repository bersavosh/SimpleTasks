# SimpleTasks:
A small collection of simple scripts and notes I've written for simple tasks or to remember something.

## Scripts:

### 1. GehrelsStat:
A quick script to calculate confidence interval and significance for poisson distribution of events in the photon-starved regime. This is a lazy brute-force implementation of [Gehrels 1986](http://adsabs.harvard.edu/abs/1986ApJ...303..336G).

#### To use: 
* Download `GehrelsStat.py`.
* set the  the first line of the code to match your python (you can find your python by typing `which python` in the terminal).
* give the file permision to execute (e.g., `chmod +x GehrelsStat.py`)
* Set an alias for this file:
If you are using bash, then something like this in your `.bashrc` file:

`
alias gehrels="/PATH/TO/gehrelsStat.py"
`

* Now it is ready for use in the command line.

`
$ gehrels <N_OBSERVATION> [CONFIDENCE INTERVAL] [STEP SIZE]
`

If only number of observations is provided, limits for 1-sigma confidence are returned and default step size is assumed.

### 2. NormStat:
I'm too forgetful to remember how many 9s there are after the decimal in a 5-sigma confidence or what are the chances of occurrence for it. So this small script spits it out.

Usage is similar as GeherlsStat. Download `NormStat.py` and set alias for it. Then in the terminal you can type:

`
$ normstat <OBSERVED VALUE> [MEAN] [STANDARD DEVIATION]
`

### 3. GCcat:
A command line tool that returns information about a globular cluster from the [Harris Catalog](http://adsabs.harvard.edu/abs/1996AJ....112.1487H) ([2010 edition](http://www.physics.mcmaster.ca/~harris/Databases.html)).

## Notes:

### 1. 
