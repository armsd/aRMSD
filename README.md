
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

Simply download the project from GitHub and navigate to the armsd folder and run aRMSD.py, e.g. from command line

```bash
python aRMSD.py
```

b) Usage as Python module:

```bash
pip ...
```

c) Compilation via Pyinstaller:

Download the latest version of the master branch and install [Pyinstaller] (http://www.pyinstaller.org/).

```bash
pip install pyinstaller
```

Download the master branch of aRMSD, extract the files and navigate to the main folder. Execute the compile_aRMSD.bat script (under Windows) which will create a single executable file in the armsd folder. Temporary files will be created during this process (compilation will take around 15 min) and afterward deleted.

# Documentation and Tutorial
will be added in the near future.

# License
This package and its documentation are released under the [MIT License] (./LICENSE)
