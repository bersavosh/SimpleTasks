# SimpleTasks:
A small collection of simple scripts and notes I've written for simple tasks or to remember something.

## Scripts:

### 1. GehrelsStat:
A quick script to calculate confidence interval and significance for poisson distribution of events in the photon-starved regime. This is a lazy brute-force implementation of [Gehrels 1986](http://adsabs.harvard.edu/abs/1986ApJ...303..336G).

#### To use: 
* Download [`GehrelsStat.py`](https://github.com/bersavosh/SimpleTasks/blob/master/GehrelsStat.py).
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

Usage is similar as GeherlsStat. Download [`NormStat.py`](https://github.com/bersavosh/SimpleTasks/blob/master/NormStat.py) and set permissions and an alias for it. Then in the terminal you can type:

`
$ normstat <OBSERVED VALUE> [MEAN] [STANDARD DEVIATION]
`

### 3. Xspec Configurations:
If you use [`Xspec`](http://heasarc.gsfc.nasa.gov/docs/xanadu/xspec/index.html) for spectral analysis, you might need to set a few parameters to your desired configuration every time you run it (e.g., element abundance table, cross sections, etc.). One easy way to make Xspec load your configuration every time is to have a configuration file somewhere and make Xspec run it everytime it starts. 

The [xspec_mod.conf](https://github.com/bersavosh/SimpleTasks/blob/master/xspec_mod.conf) file here is a simple example of this. It sets the solar abundances and cross section tables, initiates the plotting device (Xwindows here), sets default response to Xspec queries to yes and sets default plotting to energy (instead of channel).

You can run it at the begining of an Xspec session by:
`
$ xspec - /PATH/TO/xspec_mod.conf
`
Or you can make an alias for it to load it by default:
`
alias xspec="xspec - /PATH/TO/xspec_mod.conf"
`
### 4. GCcat:
A command line tool that returns information about a globular cluster from the [Harris Catalog](http://adsabs.harvard.edu/abs/1996AJ....112.1487H) ([2010 edition](http://www.physics.mcmaster.ca/~harris/Databases.html)).

## Notes:

### 1. [acknowledg_checklist](https://github.com/bersavosh/SimpleTasks/blob/master/acknowledg_checklist.md)
A small checklist for acknowledgments in a paper.

### 2. [Astro software checklist](https://github.com/bersavosh/SimpleTasks/blob/master/observer_startup_guide.md)
A checklist of softwares and packages needed for observational astronomy. 
