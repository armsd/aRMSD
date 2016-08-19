"""
aRMSD: Version 1.0rc1
==================================
aRMSD is a Python module/program that allows for a fast and comprehensive
analysis of molecular structures parsed from different files. Unique features
are a support of crystallographic data, error propagation and specific types
of graphical representations.

Key features:
* Parses data from various file formats
* Establishes consistency and matches coordinate sequences of two molecules
* Aligns two molecular structures based on the Kabsch algorithm
* Supports different weighting functions for the superposition
* Supports error propagation for experimental structures
* Generates different visualization types of the superposition results
* Writes outfiles that can be passed to other programs

Dependencies:
* numpy
* matplotlib
* vtk
* uncertainties
* [openbabel/pybel]

It is highly recommended to install all dependencies directly from python wheels
prior to the installation of aRMSD.

Recent changes:
* MAJOR
- Source code has been completely rewritten and optimized
- Results are visualized with VTK directly from the program
- A logger has been added as user-interface and to keep track of the progress
- Atoms at identical positions (e.g. disorder) are checked for
- Supports matching within a PSE group (e.g. F<->Cl<->Br<->I)
- Structural changes can be resetted
- Implementation of Hungarian algorithm as additional matching solver
- Added improved data export to every menu
- Two substructures can be defined and their contributions to the superposition is evaluated
- Structural parameters (atoms, bonds, angles, dihedrals) can be picked and compared in aRMSD representation
  and information about their values in both structures is printed out to the user
- Added formal support for .cif files (however structure expansion is at an initial stage)
- Viewer for .cif files and custom symmetry operations, the menu allows for structure export
- Error propagation for experimental structures is supported through 'uncertainties' package
  Uncertainties are also implemented for RMSD and similarity parameters
- Added script for rendering with blender

* MINOR
- Overall improved menus and better user interface
- Function for consistency establishment has been substantially improved
- Bonds can be added or removed for the final representations
- New similarity descriptors are now available
- New features for consistency establishment
- Changed some plotting defaults
- File handling more robust
- Better visualization + plots are more customizable
- Simplyfied user input for True/False questions
- Improved logfile output
- Improved VTK screenshots
- Extended and improved handling of external settings
- MPL and uncertainties modules are optional, reducing the dependencies to numpy and VTK
- Reads and writes information to new file format (.xyzs - coordinates + standard deviations + plotting information)
- Added generation of z-matrices and RMSD decomposition in distances, angles and dihedral angles (incl. uncertainties)
- Added GARD descriptor (J. Chem. Inf. Model. 2009, 49, 1889-1900)
- Cartesian gradient in computational data can be used as standard deviations

* KNOWN ISSUES AND FUTURE DEVELOPMENT
- Shader problem with vtk 7 (Rollback to 6.2)
- Full compatability with Python 3.5+
- Add: Parser for .res, .mol2
- Add: group symbols for bond types
- Add: more output for interpolation
- Fix: RMSD results formatting
- Fix: outfile without standard deviations
- Fix: openbabel support (supp. file types and determine required .obf files)
- Fix: percentages in substructure contributions
- Fix: Camera in blender for some orientations
- Improve: internal coordinates with highest deviations
- Improve: logfile
- Improve: VTK: colorbar text size and colorbar widget and settings
- Improve: VTK: better labels
- Improve: spacing in statistics text
- Fix: bond radii for export (wireframe) + include scaling factor
- Write: Documentation and examples

* Documentation: See https://github.com/armsd/aRMSD for further information

(c) 2016 by Arne Wagner <arne.wagner@aci.uni-heidelberg.de>.
Please send feature requests, bugs and feedback to this address.

This software is released under a dual license. (1) The MIT license.
(2) Any other license, as long as it is obtained from the original
author.
"""

# Authors: Arne Wagner
# License: MIT

from __future__ import absolute_import

from aRMSD import run, __aRMSD_version__, __author__

__version__ = __aRMSD_version__
