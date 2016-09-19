Installation details
------------------------

aRMSD uses several packages that are actively developed and continuously change in the future. Therefore keeping track of changes in other packages is important to ensure that aRMSD will continue to work with newer package versions. The program was developed and tested with the following versions of the directly used thrid party packages. 

**Module versions**

         - numpy 1.11.1+mkl
         - matplotlib 1.5.1
         - vtk 6.2.0
         - future 0.15.2
         - uncertainties 3.0.1
         - cython 0.24.1
         - openbabel 1.8.4

Due to changes from vtk 5 to 6, aRMSD currently does not support any other vtk version than 6.2 and a backwards compatibility to the older vtk 5 engine is not planned (unless it is frequently requested). As of now there are some issues when vtk 7.0 is used and a part of the active development is concerned with the vtk 7 support.

**Compilation arguments**

The following arguments can be passed to the installation script and specify the usage of Cython and openbabel in the compilation. All arguments are optional and if none are given neither Cython nor openbabel will be used. The specification of the C compiler may not be needed if your defaults are properly set, however setting it explicitly should ensure a successful installation.

         - --use_cython (True / False)
         - --cython_compiler (any valid C compiler used by Cython, e.g. msvc)
         - --use_openbabel (True / False)
         - --overwrite (True / False)

During the installation, the existence of an openbabel hook file in the PyInstaller hook path is checked. If no hook exists, a respective file will be created. In case of an existing hook, the file can be overwritten if the --overwrite variable is set to True.


Future developments
------------------------

Several new features and improvements are planned which will hopefully be continuously added in the future, some of which are: 

         - Support of Python 3.5 and vtk 7
         - Improvements for 2D and 3D plots (mostly text annotation)
         - Better formatting for the output and improved [Blender] (http://www.blender.org) interface
         - Structural interpolation in internal coordinates
         - Better support of substructures

Any ideas are always welcome and requested features will be added if time allows it.