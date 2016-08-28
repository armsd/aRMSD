
![alt tag](./aRMSD_logo.png)

An open toolbox for structural comparison between two molecules with various capabilities to explore different aspects of structural similarity and diversity. Using data from common file formats the minimum RMSD is found by combining the functionalities of the Hungarian and the Kabsch algorithm. Crystallographic data provided from cif files is fully supported and the results can be rendered with the help of the [vtk] (http://www.vtk.org/) package. 

# Installation
aRMSD can be installed in two ways, either via pip (in this case it will be used as a Python module or Python application) or you can download the source code and use the .spec file to compile it into a single standalone executable. In any case some modules are required which are listed below including their versions which were tested so far:

    * Python 2.7
    * numpy (1.11.1+mkl)
    * vtk (6.2.0)
    * matplotlib (1.5.1)
    * future (0.15.2)
    * uncertainties (3.0.1)

optional (Python module/application only):

    * openbabel / pybel (1.8.4) [additional file formats]

In order adjust the source code by yourself, always make sure to have the required Python pacakges installed and download the latest version of the master branch. Whenever possible it is recommended to add and update packages using pre-compiled Python [wheels] (http://www.lfd.uci.edu/~gohlke/pythonlibs/) suited for your operating system which can be installed via pip. If you add features or wish to have an idea implemented or a bug fixed, contact me or make a [request] (https://github.com/armsd/aRMSD/issues).

a) Usage as Python application:

- The easiest way to use aRMSD.

Simply clone the project or download the zip file from GitHub, navigate to the armsd folder and run aRMSD.py, e.g. from command line

```bash
python aRMSD.py
```

b) Usage as Python module:

- This will install aRMSD as a Python module that can be imported and used in other applications. This allows for both the most extensive utilization of the code and provides the possibility to keep an eye on the ongoing development via pip.

Install the program by typing

```bash
pip [to be added]
```

in your command line.

c) Executable compiled with Pyinstaller:

- Produces a single file which can be copied anlongside the settings.cfg and the xsf folder to different machines with the same architecture. Once the program has been compiled, this is probably the easiest way to use aRMSD - especially for users that are unfamiliar with Python. 

First ensure that you have the latest version of [Pyinstaller] (http://www.pyinstaller.org/) or install it with pip.

```bash
pip install pyinstaller
```

Download the current master branch of aRMSD, extract the files and navigate to the main folder. Execute the compilation script from command line by typing

```bash
python compile_aRMSD.py
```
or run the file in a Python shell. This will create a single executable file in the armsd folder and should work for all operating systems. Temporary files will be created during this process (compilation will take around 25 min) and deleted after the process is finished. To use the program

# Documentation and Tutorial
Will be added in the near future.

# License
This package and its documentation are released under the [MIT License] (./LICENSE)
