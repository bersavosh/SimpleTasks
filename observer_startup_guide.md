# A check list for setting up observational astronomy softwares and libraries

Prepared by: A. Bahramian, E. W. Koch, A. J. Tetarenko, B. E. Tetarenko
Draft version: May 2016

**Note 1: The instructions below are just general suggestions, and do not apply to all projects. Check with your supervisor which of these you need.**

**Note 2: Most packages below are available for common system types (Linux,OS X, Windows). But some are system-specific.**

## Part 1: General Setup
### Development tools for basic compilers:
 - For Mac:
 	- [XCode](https://developer.apple.com/xcode/download/)
	
		Note 1: Only for Mac systems, if you’re using linux, you don’t need this.
	
		Note 2: Install a stable version. I.e., don’t install a “beta” version.
	
		Note 3: To start XCode, you need to read and accept its terms/conditions. Do so by typing `xcodebuild -license` in the terminal.
	
		Note 4: Most likely you will need to install command line tools as well. If so, you will need to type this in the terminal: “xcode-select --install”.
			
- For Linux:

	Most linux builds have basic compilers, however some (e.g., Vanilla Ubuntu / CentOS) will often need the package `build-essential` which puts in the less common compilers like gfortran bindings. This package can be installed through a package manager (see below for details on package managers). 
	
	E.g.: `apt-get install build-essential`

### Package Manager:
For many packages and software dependencies, it’s more convenient to use a package manager instead of manual install. 
- For Mac:
Recommended: Either Homebrew (http://brew.sh/) or MacPorts (https://www.macports.org/)
		Note 1: Only install one of these, not both.
	For Linux:
Package managers are already installed. Typically this will be apt-get (debian distributions) or yum (fedora/red-hat)

- A Scientific python distribution:
	Recommended: Anaconda (https://www.continuum.io/downloads). This comes with a fantastic package manager - conda - which will make your life much easier! It can do other things too (such as creating new python environments for testing). Here’s a basic tutorial on its use: http://conda.pydata.org/docs/using/using.html
Note 1: Most likely you will need Python 2.7 (and not 3.5). Check with your supervisor before choosing a version.
Note 2: Anaconda contains basic tools for scientific use of python (e.g., numpy, scipy, matplotlib, etc.) plus many other useful analysis/demonstration packages: 
Astropy (http://www.astropy.org/) 
AstroML (http://www.astroml.org/index.html)
Jupyter (http://jupyter.org/) (formerly the ipython notebook)
Numpy - fast, basic numerical routines
Scipy - A continuation of the numpy capabilities, including signal analysis and many fitting routines
Matplotlib - the python standard of plotting. Highly flexible, but easy to use for basic plotting (most of the time)
Pandas - Provides many, many tools for handling data in the form of tables (say catalogs of objects). 
Depending on your work some of these packages can help in your analysis.

-  A text editor:
Your work most likely includes writing codes or opening astronomical data sets, thus a programming-oriented text editor can be beneficial.
Recommended: Sublime (https://www.sublimetext.com/) 
Note 1: If you’re using sublime for scripting, it would be useful to install sublime package control (https://packagecontrol.io/) and use it to find and install packages which can assist you in scripting. Here are some handy Sublime add-ons:
Anaconda - python IDE and linter (NOT the same as the Anaconda distributions mentioned above). Provides auto-completion of defined variables, call-sequences for functions/classes, and checks for simple syntax errors in real-time.
BracketHighlighter - more options than you could ever use/want for your bracket highlighting needs
GitGutter - show which lines have changed since your last git commit
LaTeXing - very handy tools when compiling/writing latex documents (requires having a latex distribution installed; see section 4)
Material Theme & Material Color Scheme - It makes everything pretty (there are plenty of other custom themes for sublime too)
Origami - fine-tune split-window configurations
SideBarEnhancements - do more in the sidebar (create files, move directories/files, etc)
Sublimerge Pro - side-by-side comparison of different versions of a files (technically asks for its own license, but is free to use indefinitely as is Sublime)

- XQuartz or X11:
For some packages and tasks, you might need XQuartz (X11) in order to enable graphical user interface.
XQuarts: http://www.xquartz.org/
X11: http://www.x.org/wiki/
Note 1: If you’re using Linux, it’s possible that it is already installed on your system. 

Part 2: Tools for computational projects
If your project is code-intensive and/or computationally extensive:
- Setting up github account and install git-desktop (https://github.com/) 

- If you are required to use Cloud resources: Your supervisor will provide you with an account if you need one.

- Jupyter notebooks are helpful for small code testing, data presentation and keeping notes on your scripts. Jupyter is included in Anaconda. If you need an advanced integrated development environment (IDE), PyCharm can be a good choice (http://www.jetbrains.com/pycharm/).

Part 3: Astro-oriented packages
Most of the Astronomy packages you might need are listed here: http://heasarc.gsfc.nasa.gov/docs/heasarc/astro-update/

Here, we go over a few common ones which our group uses frequently:

General note: Many of the packages below have a few dependencies which you need to install prior to installing the packages. You can find the list of such dependencies in each package’s installation guide (or on their websites). Generally, these dependencies can be installed using a package manager (e.g., MacPorts, HomeBrew, Apt-Get, etc.). Make sure to check this before attempting to install dependencies manually. 

Part 3.1: General (multi-wavelength)
- DS9: For visualization of astronomical data:
	Link: http://ds9.si.edu/site/Download.html
Note 1: If installing on Mac, make sure to use the disk image installers (i.e., click on the links next to the Apple logo, instead of the ones next to the “X”)

- Astropy: For general astronomical data analysis (http://docs.astropy.org/en/stable/).
Astropy is already included in Anaconda, we mention it here to emphasize on its importance. There are a variety of useful tools available, with more becoming available with every new release (see the documentation link above). Some of the more common packages in Astropy are:
Astropy.io.ascii: For reading/writing data in ascii format 
Astropy.io.fits: For reading/writing data in FITS format
	Astropy.table: for dealing with data tables

Astropy also has a variety of affiliated packages for more specific analyses: http://www.astropy.org/affiliated/

Part 3.2: X-rays (and UV)
- HEASoft: High-Energy astrophysics software package:
Link: http://heasarc.gsfc.nasa.gov/docs/software/lheasoft/
Note 1: You might not need all the tools within HEASoft. When downloading the install package you can choose which tools you want to install. Check with your supervisors which tools you’ll need.
Note 2: It’s recommended to use the “source code” installation, instead of system-specific binaries. This is especially important if you’re planning to use XSpec with local models or PyXSpec (see below).
Note 3: For some mission-specific tasks (Specially Swift and NuSTAR), you need to setup calibration database remote access: http://heasarc.gsfc.nasa.gov/docs/heasarc/caldb/caldb_remote_access.html 
Note 4: HEASoft contains data analysis packages for Swift and NuSTAR among many other X-ray telescopes.
Note 5: If using XSpec, it’s recommended to apply the most recent patch, for details visit: http://heasarc.gsfc.nasa.gov/docs/xanadu/xspec/issues/issues.html
Note 6: If you want to use PyXSpec it is recommended that you build/install the full HEASoft software package on a Linux based machine (e.g., ubuntu, redhat etc.). PyXSpec does not play well with Anaconda Python on MAC. Steps are as follows:
build/install HEASoft, make sure to set the appropriate python path before the build (e.g., /home/ubuntu/miniconda2/bin/python)
Edit your .bashrc, and create an alias for the HEASoft start-up script.
Start xspec command-line in your home directory by typing ‘xspec’. This will create a .xspec directory for your user.
Fix gfortran library issue: the Anaconda/miniconda distribution by default will try to use libgfortran, rather than libgcc (i.e., the package that xspec needs for some functions). To remedy this, first remove libgfortran, install libgcc, and force anaconda to use libgcc with the following commands: conda remove libgfortran and conda install libgcc --force. Second, as this will cause issues with the python system module you now need to uninstall, then re-install this module with the following commands: conda remove system and conda install system.
Lastly, if you still encounter errors when trying to import the xspec module, there may be issues with your current version of scipy. To fix this, remove the current version of scipy (conda remove scipy) and install scipy 0.15.1 (conda install version=0.15.1).
For PyXSpec documentation see: https://heasarc.gsfc.nasa.gov/xanadu/xspec/python/html/index.html

- CIAO: Chandra Interactive Analysis of Observations
Link: http://cxc.harvard.edu/ciao/download/
Note 1: Install only if you are going to analyse Chandra X-ray data
	
- SAS: XMM-Newton Science Analysis Software
	Link: http://www.cosmos.esa.int/web/xmm-newton/download-and-install-sas
	Note 1: Install only if you are going to analyse XMM-Newton data

- ACIS_Extract: for analysis of data from Chandra/ACIS
	Link: http://www2.astro.psu.edu/xray/docs/TARA/ae_users_guide.html
	Note 1: ACIS_Extract requires IDL and IDL astronomy package.
	Note 2: Install only if your supervisor asks you to.

- MaLTPyNT: For accurate analysis of NuSTAR data
	Link: https://bitbucket.org/mbachett/maltpynt
Note 1: Install only if you need to perform accurate analysis of NuSTAR data (with focus on Timing analysis)

Part 3.3: UV/Optical/NIR
- IRAF and PyRAF: Image reduction and analysis facility
	Link 1 (NOAO IRAF): http://iraf.noao.edu/
Link 2 (Ureka IRAF): http://ssb.stsci.edu/ureka/	
Note 1: Ureka is easier to install and it has all the generic packages included in IRAF.
Note 2: If you are to use IRAF for analysis of Gemini data, Ureka is recommended. Although Ureka is deprecated and will not be updated any more, it still has the main tools for IRAF and Gemini data analysis. For Gemini toolkit go to: http://www.gemini.edu/sciops/data-and-results?q=node/11823

- AstroConda: A package for astronomical data analysis
	Link: http://astroconda.readthedocs.io/en/latest/
	Note 1: Anaconda Python distribution recommended
Note 2: Although AstroConda contains tools for various fields of astronomy, it is focused on optical (e.g., HST) analysis data analysis. See list of included packages here: http://astroconda.readthedocs.io/en/latest/package_manifest.html

- SExtractor: simple source detection package
	Link: https://sourceforge.net/projects/sextractor/
Note 1: Many observatory-specific analysis packages have their own implementation of source detection tools and so you might not need this. Install, only if necessary.

- pyspeckit (http://pyspeckit.bitbucket.org/html/sphinx/index.html) - a python package for robust spectral-line fitting for a variety of cases

Part 3.4: (Sub)-millimeter/Radio
- CASA:  For calibration, reduction, and imaging of VLA, ALMA and GBT data (amongst others). Download it here: https://casa.nrao.edu/casa_obtaining.shtml (if using Linux, grab the Red Hat 6 version). There are all sorts of handy tutorials (https://casaguides.nrao.edu/index.php/Main_Page); choose the one most relevant to your project and follow along. Nearly all of the tutorials provide a complete example, from raw data to a final image/analysis. 
-Note: These days almost any interferometric data can be imported into CASA in some way, shape or form. For scripts that convert an SMA data set to CASA MS see https://www.cfa.harvard.edu/sma/casa  . For how to convert NOEMA/PdBI calibrated data into CASA format see http://www.iram.fr/IRAMFR/ARC/documents/filler/casa-gildas.pdf .

-CasaPython (https://github.com/radio-astro-tools/casa-python )- Package which makes it easy to install additional python packages for use in CASA (since CASA contains its own python version). After following the installation instructions, you should have “casa-python” and “casa-pip” available as commands in the terminal. 

-AnalysisUtilities (https://casaguides.nrao.edu/index.php?title=Analysis_Utilities )- Useful third party CASA tools.

- radio-astro-tools (http://radio-astro-tools.github.io/) - provides easy, efficient handling of spectral line data cubes and a variety of analysis tools. And some of the developers are at the UofA! So you can come bug Eric or Erik if any issues arise.

- pyspeckit (http://pyspeckit.bitbucket.org/html/sphinx/index.html) - a python package for robust spectral-line fitting for a variety of cases

-MIRIAD (SMA-https://www.cfa.harvard.edu/sma/miriad/; ATCA-http://www.atnf.csiro.au/computing/software/miriad/;
CARMA-http://bima.astro.umd.edu/miriad/)- Similar to CASA, for calibration, reduction, and imaging of interferometric data, notably used with SMA, ATCA, and CARMA (personally I prefer to use CASA instead, when possible). Note that if you have to use this, there is a different version of MIRIAD for different telescopes, make sure to download the right one!

-GILDAS/CLASS/ASTRO (https://www.iram.fr/IRAMFR/GILDAS/ )- NOEMA/PdBI’s native calibration, reduction, and imaging package. Also contains sensitivity calculator and other proposal tools.
-MIR (https://www.cfa.harvard.edu/sma/mir/ )- Original SMA data reduction package (I think). It is written in IDL and can only flag and calibrate data, no imaging. Not easy to use, avoid at all costs!

-STARLINK (http://starlink.eao.hawaii.edu/starlink/ )- JCMT’s native reduction software. There are lots of help pages/tutorials on the EAO website and in the cookbooks linked there (http://www.eaobservatory.org/jcmt/observing/ ).

Part 4: Helpful links/suggestions
- For script errors, bugs, software issues, etc.:
	Googling the error message is a very helpful way. Example: http://bfy.tw/5XMJ

Note that in the example above first link is from the website https://stackoverflow.com/. This site is very helpful for most errors/problems you might face. First look for discussions regarding the problem you’re interested in and if you couldn’t find the answer there, you can submit your own question.

- Bash scripting:
If you need to write a Bash script, this guide might help:	http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html

- For plotting data/results:
- GNUplot is a basic and easy to use package: http://www.gnuplot.info/. You can find some helpful tips/commands here: http://www.gnuplot.info/docs_4.0/gpcard.pdf

- If you need more sophisticated/better looking plots, Matplotlib is a good python package for it: http://matplotlib.org/index.html. You can find some examples and recipes here: http://matplotlib.org/users/recipes.html. Note that matplotlib is already included in Anaconda.
	
- For Writing articles in Latex:
- TexLive is an easy to use package: https://www.tug.org/texlive/. You can install it with a package manager as well.
- If you feel comfortable using your text editor to write the article, LatexMK can be a great alternative: http://mg.readthedocs.io/latexmk.html. You can also use a package manager to download and install LatexMK.
- Here is a small guide for math symbols and equations in Latex: ftp://ftp.ams.org/ams/doc/amsmath/short-math-guide.pdf

 - Simple one-line calculations:
	- You can just type it in Wolframalpha: http://www.wolframalpha.com/
- Or you can install an astro-aware calculator for your command line: http://hea-www.harvard.edu/~alexey/calc.html

