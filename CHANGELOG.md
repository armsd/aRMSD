Version     0.9.5 (24 October 2018, development)
------------------------

**Improvements**

         - deployment of aRMSD under Linux Debian 9 (buster/sid) is facilitated
           by a script collecting and installing the *.deb dependicies
         - provision of an initial, illustrated primer about the progam
           altogether with additional test data BZAMID-A / BZAMID-B both in 
           *.xyz and *.pdb

**Bugfixes**

         - aRMSD's color scheme to display of model and reference compared with
           each other prior and after the Kabsch test now is the same
         - addition of a time stamp about the analysis (log file)
         - gently change of aRMSD's log line limit to 80 chars now allows a
           smoother display in either terminal / text editor, or word processor


Version     0.9.4 (26 January 2017, development)
------------------------
     
**Improvements:**

         - aRMSD is now running under both Python 2.7 and 3.6
         - better file handling and openbabel interface
         - added a new coloring scheme for the aRMSD representation
         - added .mol/.sdf/.sd file support
         - updated installer for Python 3 environment
    
**Bugfixes:**

         - fixed incorrect / missing versioning for pybel / openbabel
         - fixed some bugs in the outfile creation


Version     0.9.3 (25 September 2016, development)
------------------------
     
**Improvements:**

         - added SHELX .res/.ins/.lst and .mol2 file support
    
**Bugfixes:**

         - fixed a bug in the addition / removal of bonds


Version     0.9.2 (15 September 2016, development)
------------------------
     
**Improvements:**

         - added openbabel support for the compiled program version
         - updated installer to generate required files on-the-fly
    
**Bugfixes:**

         - none


Version     0.9.1 (31 August 2016, development)
------------------------
     
**Improvements:**

         - none
    
**Bugfixes:**

         - fixed a few bugs that were introduced during the rewrite for
           Python 2.7/3.5 compatability
         - corrected some typos


Version     0.9.0 (29 August 2016, development)
------------------------
 Initial public release
    
**Improvements:**

         - none
    
**Bugfixes:**

         - none
