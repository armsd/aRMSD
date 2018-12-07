The goal of the primer is to enable you to perform a basic comparison
of two molecular structures with `aRMSD`, including proper
installation of the program.  Here and there, the primer merely will
*hint* you to additional features implemented in `aRMSD`.


# setup of `aRMSD`

Initially, Arne Wagner developed `aRMSD` under Windows.  Hence, the
corresponding section below retains all the relevant recommendations
by him as left in 2017 in the original branch of the project of
`aRMSD`.  The copy is verbatim, with the exception of putting the
information into one place, a reformat, and a spell check.  As
outlined in branch `compilerIssueWindows`, however, it is possible
that the original script `compile_aRMSD.py` does not work.  If so,
either checkout branch `compilerIssueWindows` with an updated
compiler script (different name), or use a setup in Linux Debian
(testing) as outlined below.

*This* forked branch is based on the original version 0.9.6 by Arne
Wagner.  It was developed further in Debian 10 (Sid/buster) because
`aRMSD` was used side-by-side with other programs already deployed
successfully in Linux.  The installation process differs from the
one in Windows, as `pip` and `PyInstaller` are omitted, and the
installation of dependencies is automated by a script.


## setup in Windows

`aRMSD` can be in two ways, either via `pip` (in this case it will
be used as a Python module or Python application) or you can
download the source code and compile it into a single standalone
executable. In any case some packages are required which are listed
below:

-   `Python` (version 2.7 or 3.6)
-   `numpy` (version 1.11.1 / 1.12)
-   `vtk` (version 6.2.0 / 7.0)
-   `matplotlib` (version 1.5.2 / 2.0)
-   `PyQt4`
-   `uncertainties` (version 3.0.1)

optional:

-   `Cython` [performance improvements] (version 0.25.2)
-   `openbabel` / `pybel` [additional file formats] (version 2.4.1)

Due to changes from `vtk 5` to `6`, `aRMSD` does not support an
older `vtk` version than `6.2` and a backwards compatibility to the
older `vtk 5` engine is not planned.

In order to adjust the source code by yourself, always make sure to
have the required Python packages installed and download the latest
version of the master branch. Whenever possible it is recommended
to add and update packages using pre-compiled Python `wheels`
(<http://www.lfd.uci.edu/~gohlke/pythonlibs/>) suited for your
operating system which can be installed via `pip`.


### Compilation arguments

The following arguments can be passed to the installation script
and specify the usage of `Cython` and `openbabel` in the
compilation. All arguments are optional and if none are given
neither `Cython` nor `openbabel` will be used. The specification
of the `C compiler` may not be needed if your defaults are
properly set, however setting it explicitly should ensure a
successful installation.

-   `--use_cython` (`True / False`)
-   `--cython_compiler` (any valid `C compiler` used by `Cython`,
    e.g. `msvc`)
-   `--use_openbabel` (`True / False`)
-   `--overwrite` (`True / False`)

During the installation, the existence of an `openbabel` hook file
in the `PyInstaller` hook path is checked. If no hook exists, a
respective file will be created. In case of an existing hook, the
file can be overwritten if the `--overwrite` variable is set to
`True`.


### Executable compiled with `PyInstaller`

This produces a single file which can be copied alongside the
`settings.cfg` and the `xsf folder` to different machines with the
same architecture. Once the program has been compiled, this is
probably the easiest way to use `aRMSD` &#x2013; especially for users
that are unfamiliar with Python.

First ensure that you have the latest version of `PyInstaller`
(<http://www.pyinstaller.org/>) or install it with `pip`:

    pip install pyinstaller

Download the current master branch of `aRMSD`, extract the files
and navigate to the main folder. Run the compilation script in an
interactive Python shell or from command line by typing

    python compile_aRMSD.py

This will create a single executable file in the `armsd` folder
and should work for all operating systems. Temporary files will be
created during this process (the compilation will take around
30 min, depending on the machine) and deleted after the executable
is created. Optional arguments can be given to make use of
`Cython` (<http://cython.org/>) and `openbabel`
(<http://openbabel.org/wiki/Main_Page>). Note that the `Cython C
    compiler` should be specified if several options are available:

    python compile_aRMSD.py --use_cython=True --cython_compiler=msvc --use_openbabel=True --overwrite=True

If you are using Python 3.6, there is a bug in the `PyInstaller`
entry script and typing `pyinstaller` in a shell will not start a
correct process. To fix this, go in the Python installation folder
and edit the `pyinstaller-script.py` file: add quotes around the
path in the first program line (e.g. `"c:\program
    files\python36\python.exe"`).


# Setup of aRMSD in Linux Debian / Ubuntu

In addition to the `*.zip` archive available on GitHub, `aRMSD`
depends on libraries most likely not installed on your computer.
Anticipate about 0.2 to 0.3 GB of disk space needed for them.

For a facile, semi-automatic set-up, the top directory of the
extracted archive contains script `debcollector_aRMSD.py` which you
shall run once from the CLI prior to any use of `aRMSD`:

    python debcollector.py

This script is dedicated to the deployment under Linux Debian (e.g.,
Debian 9 (Sid/buster), or Xubuntu (Xubuntu 18.04 LTS).  It will
request the administrator password, and triggers the system to fetch
and install the dependencies of `aRMSD` in one run.  Possibly, user
interaction is needed since this process may recursively install
modules *in addition* to the ones explicitly listed in the script.

If you use a different operating system, or prefer a manual package
installation, here are the relevant modules I use on a reference
system (Debian 9, Sid/buster) to work with `aRMSD`:

-   `python` (version 2.7.15+) and `python3` (version 3.6.6)

-   `cython` (version 0.28.4-1)

-   `openbabel`, `libopenbabel5`, `python-openbabel` (all in version
    2.4.1+dfsg-2)

-   `python-matplotlib`, `python-matplotlib-data`, `python3-matplotlib` (all
    in version 2.2.2-4+b1)

-   `python-uncertainties`, `python3-uncertainties` (all in version
    2.4.4-1)

-   `libvtk6.3`, `libvtk6.3-qt`, `python-vtk6`, `vtk6` (all in version
    6.3.0+dfsg2-2+b3); `libvtk7.1`, `libvtk7.1-qt`, `python3-vtk7`,
    `vtk7` (all in version 7.1.1+dfsg1-5)

Again, note that according to Arne Wagner's description about
`aRMSD` running in Windows, you may skip `cython` wich will provide
an *optional* gain in performance.

After completed installation of these dependencies, enter the top
directory of the decompressed archive with your shell, and start
`aRMSD`:

    python armsd/aRMSD.py 

The first start of the program is slower than the subsequent ones,
but your terminal should display a welcome screen similar to the one
in figure [40](#orgaaa3449).

![img](./docSources/aRMSD-smallWelcome.png "Initial screen display of `aRMSD` in a 80 &times; 24 character terminal.")

While it is possible to work in the default dimension of a terminal
with 80 &times; 24 characters, you may miss some of the intermediate
output provided by `aRMSD` by omission of vertical scrolling.
Hence, a taller terminal is recommended, e.g., 80 &times;
43 characters, as shown in figure [42](#orge85f849).  However, a
terminal wider than 80 characters per line will not provide
additional benefit.

![img](./docSources/aRMSD-largeWelcome.png "Initial screen display of `aRMSD` in a 80 &times; 43 character terminal.")

Like other python scripts run in the CLI, at any stage of working
with `aRMSD` the program may be closed safely from the terminal with
the command  `Ctrl + C`.

The `vtk` related modules are *essential* to work with `aRMSD`.
Still, it is possible to access a subset of functions provided by
`aRMSD` with a few of the other modules modules missing.  In
particular, this is if 

-   your system does not spot `libopenbabel`.  Then, file format
    conversions provided by `babel` will be unavailable to `aRMSD`.
    In this situation, the only model file type accessible to the
    program is `*.xyz`.

-   your system lacks `matplotlib`.  Then, there will be no provision
    of the 2D statistics plots.  Since the corresponding sub-routine
    in `aRMSD` equally contributes some numerical results, the
    eventual log generated by `aRMSD` will miss portions of the
    diagnostic data.

In both cases the welcome screen will tell you about the modules
missing / not recognized by the installation.  Yet even in this
situation `aRMSD` still will be capable to align the structure
models, refine their alignment and provide you with some of the
results of the similarity analysis.  You are set to work with
`aRMSD`.


# Example comparing two models successfully

This chapter will detail out how to compare successfully to model
data with the basic test data provided with `aRMSD`.  It is
complemented by the next section about how to identify an
unsuccessful comparison of two model data.  In addition, the
complete CLI output by `aRMSD` as well as the log are provided in
the corresponding section of the appendix.

In sub-folder `examples`, `aRMSD` provides a few test data to
familiarize with the program.  For the sake of simplicity, this
tutorial will use model data in the most basic file format
accessible for `aRMSD` &#x2013; even if your system lacks `babel` &#x2013; which
is `*.xyz`.  Copy the model data `M1.xyz` and `M2.xyz` into the
folder `armsd`.  These two represent two different conformations of
the aspirinate anion, derived from the corresponding `*.cif` found
in the CSD data base.<sup><a id="fnr.1" class="footref" href="#fn.1">1</a></sup> They were simplified to the aspirinate
anion, retaining protons, and exported in either `*.xyz` or `*.pdb`
format with Olex2.<sup><a id="fnr.2" class="footref" href="#fn.2">2</a></sup>

-   From the top directory of `aRMSD`, launch the program from the
    shell with
    
        python armsd/aRMSD.py
    
    After the simulated prompt (the `>` sign), enter the complete file
    name (including the file extension) of the first model to load.
    Contrary to the shell, there is no tab-assisted auto-completion of
    the file name.  If you err with the file name, and the model does
    not exist, you are offered a new prompt.  If you err with the file
    name pointing to an exisiting model, but are not interested to
    compare with an other model, the simplest rectification is to
    close `aRMSD` with `Ctrl + C` and to start the program freshly
    again.  
    
    The confirmation of the input (`Enter`) will cause `aRMSD` to read
    the data set and to prompt you for the input of the second model
    datum (fig [53](#org8e68104)).
    
    ![img](./docSources/aRMSD-loadingModels.png "Model loading and consistency check by `aRMSD`.")
    
    The atom coordinates provided in either `*.xyz` (*this* example)
    or `*.pdb` format provide the the atom coordinates as a tuple of
    three numbers only.  This contrasts to the `*.cif` format where
    the coordinates are provided including their standard deviations.
    So, `aRMSD` *indicates* the user about this information missing.
    Based on the file type of the model data, you may continue the
    analysis neglecting this.
    
    *Hint:* Indeed, it is possible to load different models of
    different file type (with different file extensions), such as
    `M1.xyz` for the first, and `M2.pdb` for the second model to
    compare with each other.  At this stage of the analysis, `aRMSD`
    will proceed successfully provided both models share the same
    molecular constitution.  This is tested in the `Consistency Check`
    mentioned in the lower part of the depicted output.

-   Consideration of hydrogen atoms
    
    `aRMSD` allows you to include all, or to exclude a selection of
    hydrogens (bond to carbons, or bond to group-14 elements), or to
    consider none of the hydrogens in the structure models from the
    Kabsch test.  This is done without editing the underlying files
    you provided, but will affect simultaneously both structure
    "model" and structure "reference".
    
    Generally speaking, compared with the comparison of "complete
    models", the exclusion of hydrogens may (and indeed most often
    will) increase the similarity of the structures perceived by
    `aRMSD`, expressed by a lower overall-RMSD.  If you know that the
    positions of the hydrogens in your model data are considerably
    less accurately determined then the one of the non-hydrogen atoms,
    then this may be good option to test.<sup><a id="fnr.3" class="footref" href="#fn.3">3</a></sup>
    
    For the purpose of this primer, however, all atoms were included
    in the scrutiny (fig [60](#orgc2016e0)), selected by key stroke `3`.
    
    ![img](./docSources/aRMSD-hydrogens.png "User defined exclusion / retention of hydrogens in `aRMSD`.")
    
    *Hint:* Beside a yes-no decision about hydrogens, `aRMSD` equally
    offers multiple more refined approaches how atoms will be
    considered in the Kabsch test.  These then scale the individual
    contribution of the atoms' position to the RMSD to the proton
    count, the atomic mass, or the scattering factor (for the more
    frequently used X-ray radiation wavelengths).  This accounts for
    the determination of the atom coordinates of heavier atoms being
    more accurate than for the lighter ones by X-ray diffraction
    analysis, an approach considered as advanced use of `aRMSD`.
    
    The program subsequently provides you a first reasonable *guess*
    how to align the two models.

-   User-assisted re-orientation of the models
    
    This is the first time `aRMSD` will launch the `vtk`-based
    structure visualizer in a window separate from the terminal,
    providing an interactive 3D rendering
    (fig. [65](#org262ca40)).  You may change the
    position and size of this window freely.  The depicted scene shows
    you *an initial* alignment of atom labeled model (red motif) and
    reference structure (green motif) in a reference coordinate system
    (blue).
    
    ![img](./docSources/aRMSD-structureVisualizerDefault-scaled.png "Vtk-based structure visualizer by `aRMSD`.")
    
    Multiple commands are at your disposition, outlined briefly in the
    table [1](#org957c10c).
    
    <table id="org957c10c" border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    <caption class="t-above"><span class="table-number">Table 1:</span> Typical commands to interact with the structure visualizer in `aRMSD`.</caption>
    
    <colgroup>
    <col  class="org-left" />
    
    <col  class="org-left" />
    </colgroup>
    <thead>
    <tr>
    <th scope="col" class="org-left">command</th>
    <th scope="col" class="org-left">function</th>
    </tr>
    </thead>
    
    <tbody>
    <tr>
    <td class="org-left">dragging with left mouse button (`LMB`)</td>
    <td class="org-left">tilt the scene</td>
    </tr>
    
    
    <tr>
    <td class="org-left">`CTRL + LMB`</td>
    <td class="org-left">roll the scene</td>
    </tr>
    
    
    <tr>
    <td class="org-left">`Shift + LMB`</td>
    <td class="org-left">pane the scene</td>
    </tr>
    
    
    <tr>
    <td class="org-left">middle mouse reel</td>
    <td class="org-left">zoom the scene</td>
    </tr>
    
    
    <tr>
    <td class="org-left">`r`</td>
    <td class="org-left">return to a home position</td>
    </tr>
    </tbody>
    
    <tbody>
    <tr>
    <td class="org-left">`3`</td>
    <td class="org-left">toggle anaglyph display</td>
    </tr>
    
    
    <tr>
    <td class="org-left">`e`, or `0`, or `q`</td>
    <td class="org-left">close the visualizer</td>
    </tr>
    
    
    <tr>
    <td class="org-left">`s`</td>
    <td class="org-left">save the scene (`*.png`)</td>
    </tr>
    </tbody>
    </table>
    
    Note that the more your mouse is out of the center of the
    visualizer's canvas, the more the mouse-assisted actions
    accelerate.  You may document the match as bitmap with key-stroke
    `s`; the visualizer, unaltered in its default dimension will write
    a `*.png` (2048 &times; 2048 px).  Repeated export of the scene,
    e.g., from different perspectives, will automatically increment
    the file names (`VTK_initial_plot.png`, `VTK_initial_plot_1.png`,
    `VTK_initial_plot_2.png`, etc.) deposit in your current working
    directory.
    
    If you are familiar about the alignment shown to you, close the
    visualizer (`q`).  If &#x2013; as in the current example &#x2013; the two
    model data do not align nicely, the terminal offers you multiple
    symmetry operations to try a better alignment
    (fig. [69](#org8491e6f)).  Each time you select one of
    the options, `aRMSD` displays a new *initial match* of the two in
    a newly opened instance of the visualizer.
    
    ![img](./docSources/aRMSD-realignmentInterface.png "Symmetry operations provided by `aRMSD` to alter and improve the initial alignment of structure "model" and "reference".")
    
    In the case of this primer, the relative arrangement has to
    undergo an inversion (key-stroke `1`), and an reflection in
    respect to the *xz*-plane (key-stroke `3`).  The approach is
    iterative, and the order of consecution of these operations does
    not matter.  The progress is shown in
    figure [71](#org4c97b08).  Intentionally both alignments
    shown share the same perspective.
    
    ![img](./docSources/aRMSD-M1M2-initialMatching.png "Example of progressively adjusting the relative alignment of structure "model" (`M1.xyz`) and "reference" (`M2.xyz`) in `aRMSD`.  a) After application of an inversion.  b) After subsequent application of inversion and reflection in respect to the *xz*-plane.")
    
    At this stage, you aim for a fit of the two model structures that
    is *good enough*.  (In the ongoing of this section, as well in
    comparison with the next chapter, you will learn what this refers
    to.)  Once two structure data do overlap &#x2013; again, it is *an
    initial* superposition only &#x2013; close the visualizer (key-stroke
    `q`) and save this change alignment obtained (with key-stroke
    `10`).

-   Re-ordering of the atoms
    
    To proceed in the refinement of the superposition successfully,
    the atoms recognized of both models have to be labeled
    consistently. *One* approach available in `aRMSD` is the so-called
    Hungarian algorithm, implemented as default strategy.  At the
    current stage of the analysis, this is triggered by hitting `-1`
    (minus one).
    
    `aRMSD` will again open a `vtk`-visualizer of the two prealigned
    models (figure [76](#org6b83f22)).  In contrast to the former
    situation, however, the labeling of the atoms of one molecule
    should match the one of the same atoms in the second molecule.  In
    addition, yellow streaks will indicate which atoms with greater
    distance to each other `aRMSD` considers as equivalent.
    
    ![img](./docSources/aRMSD-M1M2-Hungarian.png "Successful application of the Hungarian algorithm on well aligned structures "model"  and "reference".  Yellow streaks mark atoms of different molecules remote from each other which subsequently will be considered by `aRMSD` as analogous to each other. a) Display in the default perspective of `aRMSD`.  b) Altered perspective of the same "correlation".")
    
    Since the obtained match is reasonable, close the visualizer
    (key-stroke `q`), and save the intermediate result (key-stroke
    `10`).

-   Refinement of the superposition and Kabsch test
    
    To enter the menu about the Kabsch test, hit now once `0` (zero).
    The interface displayed by `aRMSD` in the terminal changes
    (figure [80](#orgd17946b)), and you are able to trigger the
    refinement of the superposition with `-1` (minus one).  The now
    following consecution of calling sub-routines is *recommended* to
    harvest the maximum of relevant data `aRMSD` provides.
    
    ![img](./docSources/aRMSD-KabschInterface.png "The CLI by `aRMSD` about the Kabsch test.")
    
    -   Key-stroke `0` (zero) again opens the interactive Vtk-based
        visualizer (figure [82](#org13797d1), left sub-figure).  This
        adapted ball-stick representation displays *atom radii* of the
        atoms proportional to the *relative contribution* of said atoms
        to the global RMSD.  The *atom colors* of the spheres scales to
        the absolute remaining difference of the two fit structures
        about said atom in Angstroms.  The lateral scale offers an
        estimate of the latter.
        
        ![img](./docSources/aRMSD-diffA-diffB.png "Structure display about the refined superposition of structure "model" (`M1.xyz`) and structure "reference" (`M2.xyz`) provided by `aRMSD`.  a) Composite representation, where the *atom radii* scale to the relative, and the *atom colors* of the atom to the absolute contribution of said atoms to the global RMSD (reference scale in Angstroms).  b) Wire-model superposition of the two models.")
        
        Some of the bonds depicted *might* bear a red band in the
        center.  This is to indicate that the same bond in the reference
        model is significantly shorter, than in the tested model.
        Conversely, a green band indicates a bond that is longer.  By
        default, the critical *length difference* to set these bands
        equals to 0.2 Angstrom.
        
        Clicking *on* a representation of one, two, three, or four atoms
        selects them to read-out to the final RMSD data about the
        corresponding position; or corresponding difference in distance,
        angle; or dihedral angle between model and reference.  These
        read-outs are non-permanent and provided *only* on the terminal
        (figure [85](#org31eec70)).
        
        ![img](./docSources/aRMSD-diffTest.png "Example of subsequent selection of atom C11, C12, C13 and C14 to readout differences in position (or angle) in the refined superposition of the two structures `M1.xyz` and `M2.xyz`.")
        
        The underlying routine providing the readouts is agnostic about
        the atom type, allowing both the selection of hydrogens, as well
        as non-H atoms.  The atoms of interest need not be adjacent,
        either, which may be of interest comparing distances and angles.
        Again, you close the visualizer with key-stroke `q`.
    
    -   A classical superposition display is obtained with key-stroke
        `1`.  Model and reference are depicted by the visualizer
        (figure [82](#org13797d1), right sub-figure) with the same color
        scheme as already known from the stage of prealignment.  As in
        all other instances using the `vtk`-visualizer, the rendering
        may be saved as `*.png` (key-stroke `s`), and closed (with
        key-stroke `q`).
    
    -   With key-stroke `2`, an additional determination of statistics,
        and generation of synoptic diagrams is provided.  This requires
        access to `matplotlib`, and opens a window separate from the
        therminal (figure [89](#org2804bf7)).
        
        ![img](./docSources/aRMSD-M1M2-statistics.png "Synoptic statistics plots about the successfully comparison comparing the refined alignment of model `M1.xyz` and `M2.xyz` by `aRMSD`.")
        
        Currently, this analysis is organized in sub-plots that may
        partially overlap with each other if the new GUI starts.
        Increasing the dimension of the window renders the diagrams more
        legible &#x2013; equally affecting the rendered permanent record.
        
        As usual for `matplotlib`, you have the options to zoom and pan
        within the sub-figures into particular regions of your interest.
        The complete analysis may be saved as bitmap (`*.jpeg`, `* .png`
        [default]), vector (`*.ps`, `*.eps`, `*.pdf`, `*.svg`), or
        tikz's `*.pgf`.  By default, you have to define manually where
        `matplotlib` should deposit the drawings generated.
        
        The window about the statistics plots may be closed either by
        mouse, or again key-stroke `q`.
    
    -   With call `3`, the program offers you a first decomposition
        about RMSD's contributions onto the terminal
        (figure [94](#orga4d90ed)).  Even if you do not see
        these results when accessing `aRMSD` from a small terminal
        (80 &times; 24 chars), it is useful to invoke this sub-routine
        once &#x2013; even blindly &#x2013;, since *its results* will enter the
        permanent record log written.
        
        ![img](./docSources/aRMSD-M1M2SuperposQuality.png "Terminal output of the refined superposition by `aRMSD`")
    
    -   Key-stroke `5` initiates `aRMSD` to write a permanent record
        `aRMSD_log-file.out`.  With exception of the structure
        representations and diagrams, this ASCII-file includes
        additional results of the similarity measurement, such as the
        rotation matrix applied to match the two structure models, or
        further figures of merit (e.g., cosine similarity, GARD
        similarity).
        
        It equally provides you an insight about the quality of
        superposition *prior* and *after* the refinement.  In the
        present case about a successful comparison of model `M1.xyz`
        with model `M2.xyz`, this is stated in line 48 onward about the
        initial best match retained:
        
            * Details of the matching process:
                Structures were matched...                              	True
                Applied matching algorithm...                           	distance
                Solver used for matching...                             	hungarian
                Solution of the matching problem...                     	regular
                Number of highest deviations to be shown...             	5
            
                The highest deviations were between the pairs...           [Angstrom]
            				H-3 -- H-3                       0.51023
            				H-5 -- H-5                       0.53943
            				H-6 -- H-6                       0.57067
            			       O-20 -- O-20                      0.59816
            			       O-17 -- O-17                      0.72202
                The RMSD after the initial matching was [Angstrom]..    	0.21397
        
        and provides details about the sitution about the *then refined*
        superposition of the two model structures:
        
            * Final Quality of the Superposition:                 
            
                RMSD (Kabsch test, refined superposition [Angstrom])... 	0.20276
                Superposition R^2 (dimensionless)...                    	0.99498
                Cosine similarity (dimensionless)...                    	0.99732
                d values for the GARD calculation...                    	0.3, 1.2
                GARD score (dimensionless)...                           	0.80827
            
                For an introduction into the GARD calculation, see J. C. Baber,
                D. C. Thompson, J. B. Cross and C. Humblet, J. Chem. Inf. Model.,
                2009, 49, 1889-1900, doi: 10.1021/ci9001074.

Last, but not least, a few words of caution:

-   It is normal that performing the same computation a twice, with
    the same files, in a different operating system yields results
    *slighlty different* from each other, e.g. between Xubuntu (point
    release 18.04.1) and Debian 10 (testing / Buster).

-   There are multiple "dialects" about the `*.pdb` format, which may
    require the model data you have to be converted into `*.xyz`, for
    example with `babel`<sup><a id="fnr.4" class="footref" href="#fn.4">4</a></sup> using a pattern of
    
        babel -ipdb input.pdb -oxyz converted.xyz
    
    As an example, the test data `M1.pdb` and `M2.pdb` were read
    successfully only to the Debian installation, but not to the
    Xubuntu analogue (cf. logs in the appendix).

-   While retaining all other parameters equal, symmetry operations
    needed to perform the model alignment successfully about model
    data in `*.pdb` format may be different from the alignment about
    model data in `*.xyz`.


# Example comparing two models unsuccessfully

The purpose of this section is to show *by strong contrast* to the
previous chapter how to recognize an unsuccessfully performed
analysis.  Assuming you understood the general work-flow outlined in
the section above, only a selected key points will be shown here.
Again, the test data in question are `M1.xyz` and `M2.xyz`.

Starting from scratch, the model data are read again.  To match the
precedent case, all hydrogen atoms are retained for the analysis.
Referring to figure [71](#org4c97b08), however, now *only*
the symmetry operation of inversion is applied (hence,
*intentionally omitting* the second operation of reflection in
respect to the *xz*-plane).

The implementation of the Hungarian algorithm still relates the
corresponding atoms successfully.  However, both the increased
number of yellow streaks as well their orientation *across* the
structure models is a first warning sign
(figure [106](#org7d94d83)).

![img](./docSources/aRMSD-badAlignmentOnlyInversion-stepA.png "Example of an ill-fated comparison of structure `M1.xyz` with structure `M2.xyz` with `aRMSD`, step 1/3.  a) The symmetry operation applied accounts only for inversion of the relative orientation of the two models.  Consequently b), the number of atoms deemed analogous to each other yet marked by yellow streaks is higher, than in the "best match" (previous chapter).  In addition, the streaks now pass largely *across* the structure models.")

The subsequently performed refinement of the superposition
consequently yields chemically unreasonable differences and pattern
(figure [108](#orgbe2e347)), equally manifested
in the statistics plots (figure [109](#orgeb1befa)).

![img](./docSources/aRMSD-badAlignmentOnlyInversion-stepB.png "Example of an ill-fated comparison of structure `M1.xyz` with structure `M2.xyz` with `aRMSD`, step 2/3.  a) Composite display, b) classical superposition representation.")

![img](./docSources/aRMSD-badAlignmentOnlyInversion-stepC.png "Example of an ill-fated comparison of structure `M1.xyz` with structure `M2.xyz` with `aRMSD`, 3/3.  Synoptic statistics plots.")

To commplement the findings, the corresponding section in the log
about the initial match states:

    * Details of the matching process:
        Structures were matched...                              	True
        Applied matching algorithm...                           	distance
        Solver used for matching...                             	hungarian
        Solution of the matching problem...                     	regular
        Number of highest deviations to be shown...             	5
    
        The highest deviations were between the pairs...           [Angstrom]
    			       C-11 -- C-11                      1.02336
    			       O-17 -- O-17                      1.41194
    			       O-20 -- O-20                      1.52207
    				H-1 -- H-1                       2.15521
    			       O-18 -- O-18                      2.51862
        The RMSD after the initial matching was [Angstrom]..    	2.01663

and provides details about the sitution about the *then refined*
superposition of the two model structures:

    * Final Quality of the Superposition:                 
    
        RMSD (Kabsch test, refined superposition [Angstrom])... 	2.01343
        Superposition R^2 (dimensionless)...                    	0.50549
        Cosine similarity (dimensionless)...                    	0.77410
        d values for the GARD calculation...                    	0.3, 1.2
        GARD score (dimensionless)...                           	0.47194
    
        For an introduction into the GARD calculation, see J. C. Baber,
        D. C. Thompson, J. B. Cross and C. Humblet, J. Chem. Inf. Model.,
        2009, 49, 1889-1900, doi: 10.1021/ci9001074.


# Supplementary data


## log-file by aRMSD about the successful comparison, xyz-data

The following is the *complete* log written by `aRMSD` about the
successful comparison of model `M1.xyz` with model `M2.xyz`.
Hosting system was Xubuntu 18.04 LTS (64 bit, point
release 18.04.1).

    +------------------------------------------------------------------------------+
    |              aRMSD - automatic RMSD Calculator (version 0.9.8)               |
    |                      Arne Wagner, Norwid Behrnd (2018)                       |
    |                                                                              |
    |    A brief description of the program can be found in the manual and in:     |
    |            A. Wagner, PhD thesis, University of Heidelberg, 2015.            |
    |                                                                              |
    |    Cite this program by:                                                     |
    |    A. Wagner, H.-J. Himmel, J. Chem. Inf. Model, 2017, 57, 428-438           |
    |    (doi: 10.1021/acs.jcim.6b00516),                                          |
    |    source (http://www.github.com/nbehrnd/armsd), and version used.           |
    +------------------------------------------------------------------------------+
    
    								     03-Dec-2018
    
    
    *** Log file about the superposition of structures ***
    
        "Model"...                                                            M1.xyz
        "Reference"...                                                        M2.xyz
    
    * Consistency establishment between the structures:
    
      The basic approach is to subsequently remove hydrogen atoms
      until the same number of atoms is found in both molecules.
      If the number of atoms is identical and the atom types belong
      to the same group in the periodic table, the molecules are
      considered as consistent.
    
        No disorder in the structures was found.                
    
        Initial number of atoms in "Model"...                   	20  (7 H atoms)
        Initial number of atoms in "Reference"...               	20  (7 H atoms)
    
        Consistency between the structures was established:
        The number of atoms in "Model"...                       	20  (7 H atoms)
        The number of atoms in "Reference"...                   	20  (7 H atoms)
    
        No further modifications were performed.           
    
        Final global atom count (number of hydrogens retained)...	20  (7 H atoms)
    
    * Transformation of the molecules into "Standard Orientation":
      1. The center of mass was shifted to the Cartesian origin.
      2. The moment of inertia tensor was constructed, diagonalized
         and the eigenvectors rotated on the x, y and z axes.
    
    * Details of the matching process:
        Structures were matched...                              	True
        Applied matching algorithm...                           	distance
        Solver used for matching...                             	hungarian
        Solution of the matching problem...                     	regular
        Number of highest deviations to be shown...             	5
    
        The highest deviations were between the pairs...           [Angstrom]
    				H-3 -- H-3                       0.51023
    				H-5 -- H-5                       0.53943
    				H-6 -- H-6                       0.57067
    			       O-20 -- O-20                      0.59816
    			       O-17 -- O-17                      0.72202
        The RMSD after the initial matching was [Angstrom]..    	0.21397
    
    * Kabsch alignment:
        # General settings
        Substructures were defined...                           	False
        Weighting function for Kabsch algorithm...              	none
        Consideration of multi-center-contributions...          	False
    
        # Differentiation criteria and color information
        Number of colors for aRMSD plot...                      	19
        Maximum RMSD value for color projection [Angstrom]..    	0.7
        Threshold for bond comparison [Angstrom]...             	0.02
        Number of distance pairs above threshold...             	12
        Percentage of the colored intersections...              	10.0
        Color for shorter bonds in "Model" vs. "Reference"...   	#006400  [HEX]
        Color for longer bonds in "Model" vs. "Reference"...    	#CD0000  [HEX]
        Number of bonds below threshold...                      	12
        Color of "Model"...                                     	#CD0000  [HEX]
        Color of "Reference"...                                 	#006400  [HEX]
    
        Final rotation matrix from 'Standard Orientation':
    
    	   |-0.99991965  -0.01140142  +0.00554066|
         U  =  |-0.01160250  +0.99922073  -0.03772691|
    	   |-0.00510620  -0.03778816  -0.99927273|
    
        # This matrix aligns Model with Reference.
        # U already includes all custom symmetry operations!
    
    
    
    * Final Quality of the Superposition:                 
    
        RMSD (Kabsch test, refined superposition [Angstrom])... 	0.20276
        Superposition R^2 (dimensionless)...                    	0.99498
        Cosine similarity (dimensionless)...                    	0.99732
        d values for the GARD calculation...                    	0.3, 1.2
        GARD score (dimensionless)...                           	0.80827
    
        For an introduction into the GARD calculation, see J. C. Baber,
        D. C. Thompson, J. B. Cross and C. Humblet, J. Chem. Inf. Model.,
        2009, 49, 1889-1900, doi: 10.1021/ci9001074.
    
    
    * Decomposition into different atom types          absolute     relative
    						  [Angstrom]      [%]
    			      C    (#  9)          0.11501      (08.47)
    			      H    (#  7)          0.20954      (28.13)
    			      O    (#  4)          0.31458      (63.40)
    
        z-matrix properties:
        # z-matrices are created for both molecules, based on
        # (3 N - 1) bond distances, (3 N - 2) bond angles and
        # (3 N - 3) dihedral angles.  Both the total RMSD and
        # the relative contributions are calculated.
        RMSD [Angstrom]...                                      	0.38110
        Contribution of distances...                            	22.92  [%]
        Contribution of angles...                               	43.59  [%]
        Contribution of dihedral angles...                      	33.49  [%]
    
    * Evaluation of structural parameters:
        # 1. The RMSE values are the root-mean-square errors
        #    between the corresponding properties of the two tructures.
        # 2. The R**2 values are the the correlation coefficients
        #    between the two data sets.
    
        Number of bonds...                                      	20
        R**2 of linear correlation (dimensionless)...           	0.95580
        RMSE [Angstrom]...                                      	0.05040
    
        Number of bond types...                                 	3
        R**2 of linear correlation (dimensionless)...           	0.95580
        RMSE [Angstrom]...                                      	0.03120
    
        Number of angles...                                     	62
        R**2 of linear correlation (dimensionless)...           	0.75713
        RMSE [degrees]...                                       	2.83420
    
        Number of dihedrals...                                  	148
        R**2 of linear correlation (dimensionless)...           	0.99617
        RMSE [degrees]...                                       	4.25830
    
    
    *** End of log file ***                               


## log-file by aRMSD about the unsuccessful comparison, xyz-data

The following is the *complete* log written by `aRMSD` about the
unsuccessful comparison of model `M1.xyz` with model `M2.xyz`.
Hosting system was Xubuntu 18.04 LTS (64 bit, point
release 18.04.1).

    +------------------------------------------------------------------------------+
    |              aRMSD - automatic RMSD Calculator (version 0.9.8)               |
    |                      Arne Wagner, Norwid Behrnd (2018)                       |
    |                                                                              |
    |    A brief description of the program can be found in the manual and in:     |
    |            A. Wagner, PhD thesis, University of Heidelberg, 2015.            |
    |                                                                              |
    |    Cite this program by:                                                     |
    |    A. Wagner, H.-J. Himmel, J. Chem. Inf. Model, 2017, 57, 428-438           |
    |    (doi: 10.1021/acs.jcim.6b00516),                                          |
    |    source (http://www.github.com/nbehrnd/armsd), and version used.           |
    +------------------------------------------------------------------------------+
    
    								     03-Dec-2018
    
    
    *** Log file about the superposition of structures ***
    
        "Model"...                                                            M1.xyz
        "Reference"...                                                        M2.xyz
    
    * Consistency establishment between the structures:
    
      The basic approach is to subsequently remove hydrogen atoms
      until the same number of atoms is found in both molecules.
      If the number of atoms is identical and the atom types belong
      to the same group in the periodic table, the molecules are
      considered as consistent.
    
        No disorder in the structures was found.                
    
        Initial number of atoms in "Model"...                   	20  (7 H atoms)
        Initial number of atoms in "Reference"...               	20  (7 H atoms)
    
        Consistency between the structures was established:
        The number of atoms in "Model"...                       	20  (7 H atoms)
        The number of atoms in "Reference"...                   	20  (7 H atoms)
    
        No further modifications were performed.           
    
        Final global atom count (number of hydrogens retained)...	20  (7 H atoms)
    
    * Transformation of the molecules into "Standard Orientation":
      1. The center of mass was shifted to the Cartesian origin.
      2. The moment of inertia tensor was constructed, diagonalized
         and the eigenvectors rotated on the x, y and z axes.
    
    * Details of the matching process:
        Structures were matched...                              	True
        Applied matching algorithm...                           	distance
        Solver used for matching...                             	hungarian
        Solution of the matching problem...                     	regular
        Number of highest deviations to be shown...             	5
    
        The highest deviations were between the pairs...           [Angstrom]
    			       C-11 -- C-11                      1.02336
    			       O-17 -- O-17                      1.41194
    			       O-20 -- O-20                      1.52207
    				H-1 -- H-1                       2.15521
    			       O-18 -- O-18                      2.51862
        The RMSD after the initial matching was [Angstrom]..    	2.01663
    
    * Kabsch alignment:
        # General settings
        Substructures were defined...                           	False
        Weighting function for Kabsch algorithm...              	none
        Consideration of multi-center-contributions...          	False
    
        # Differentiation criteria and color information
        Number of colors for aRMSD plot...                      	19
        Maximum RMSD value for color projection [Angstrom]..    	0.7
        Threshold for bond comparison [Angstrom]...             	0.02
        Number of distance pairs above threshold...             	16
        Percentage of the colored intersections...              	10.0
        Color for shorter bonds in "Model" vs. "Reference"...   	#006400  [HEX]
        Color for longer bonds in "Model" vs. "Reference"...    	#CD0000  [HEX]
        Number of bonds below threshold...                      	16
        Color of "Model"...                                     	#CD0000  [HEX]
        Color of "Reference"...                                 	#006400  [HEX]
    
        Final rotation matrix from 'Standard Orientation':
    
    	   |-0.99890300  -0.04569042  +0.01025632|
         U  =  |+0.04565583  -0.99895081  -0.00358193|
    	   |-0.01040922  +0.00310974  -0.99994099|
    
        # This matrix aligns Model with Reference.
        # U already includes all custom symmetry operations!
    
    
    
    * Final Quality of the Superposition:                 
    
        RMSD (Kabsch test, refined superposition [Angstrom])... 	2.01343
        Superposition R^2 (dimensionless)...                    	0.50549
        Cosine similarity (dimensionless)...                    	0.77410
        d values for the GARD calculation...                    	0.3, 1.2
        GARD score (dimensionless)...                           	0.47194
    
        For an introduction into the GARD calculation, see J. C. Baber,
        D. C. Thompson, J. B. Cross and C. Humblet, J. Chem. Inf. Model.,
        2009, 49, 1889-1900, doi: 10.1021/ci9001074.
    
    
    * Decomposition into different atom types          absolute     relative
    						  [Angstrom]      [%]
    			      C    (#  9)          0.86236      (04.46)
    			      H    (#  7)          1.88536      (21.32)
    			      O    (#  4)          3.51793      (74.22)
    
        z-matrix properties:
        # z-matrices are created for both molecules, based on
        # (3 N - 1) bond distances, (3 N - 2) bond angles and
        # (3 N - 3) dihedral angles.  Both the total RMSD and
        # the relative contributions are calculated.
        RMSD [Angstrom]...                                      	0.51559
        Contribution of distances...                            	27.97  [%]
        Contribution of angles...                               	56.78  [%]
        Contribution of dihedral angles...                      	15.24  [%]
    
    * Evaluation of structural parameters:
        # 1. The RMSE values are the root-mean-square errors
        #    between the corresponding properties of the two tructures.
        # 2. The R**2 values are the the correlation coefficients
        #    between the two data sets.
    
        Number of bonds...                                      	20
        R**2 of linear correlation (dimensionless)...           	0.00370
        RMSE [Angstrom]...                                      	1.35760
    
        Number of bond types...                                 	3
        R**2 of linear correlation (dimensionless)...           	0.00370
        RMSE [Angstrom]...                                      	1.04920
    
        Number of angles...                                     	62
        R**2 of linear correlation (dimensionless)...           	0.00251
        RMSE [degrees]...                                       	43.83380
    
        Number of dihedrals...                                  	199
        R**2 of linear correlation (dimensionless)...           	0.92064
        RMSE [degrees]...                                       	19.27750
    
    
    *** End of log file ***                               


## log-file by aRMSD about the successful comparison, pdb-data

In contrast to the `*.xyz` format, there are multiple "dialects"
about the `*.pdb` format, which may represent an obstacle already
loading the model data.  At the moment, the cause is not yet
understood.  A low-level resort may be to convert the files into
the `*.xyz` format, e.g. with `babel` in a pattern of

    babel -ipdb input.pdb -oxyz output.xyz

In present case, loading the `*.pdb` successfully was possible in
the reference system (Debian 10), but not with Xubuntu 18.04 (point
release 18.04.1), despite the installations of `openbabel` in both
systems seemingly were identical.

The following is the *complete* log written by `aRMSD` about the
successful comparison of model `M1.pdb` with model `M2.pdb`.

    +------------------------------------------------------------------------------+
    |              aRMSD - automatic RMSD Calculator (version 0.9.8)               |
    |                      Arne Wagner, Norwid Behrnd (2018)                       |
    |                                                                              |
    |    A brief description of the program can be found in the manual and in:     |
    |            A. Wagner, PhD thesis, University of Heidelberg, 2015.            |
    |                                                                              |
    |    Cite this program by:                                                     |
    |    A. Wagner, H.-J. Himmel, J. Chem. Inf. Model, 2017, 57, 428-438           |
    |    (doi: 10.1021/acs.jcim.6b00516),                                          |
    |    source (http://www.github.com/nbehrnd/armsd), and version used.           |
    +------------------------------------------------------------------------------+
    
    								     03-Dec-2018
    
    
    *** Log file about the superposition of structures ***
    
        "Model"...                                                            M1.xyz
        "Reference"...                                                        M2.xyz
    
    * Consistency establishment between the structures:
    
      The basic approach is to subsequently remove hydrogen atoms
      until the same number of atoms is found in both molecules.
      If the number of atoms is identical and the atom types belong
      to the same group in the periodic table, the molecules are
      considered as consistent.
    
        No disorder in the structures was found.                
    
        Initial number of atoms in "Model"...                   	20  (7 H atoms)
        Initial number of atoms in "Reference"...               	20  (7 H atoms)
    
        Consistency between the structures was established:
        The number of atoms in "Model"...                       	20  (7 H atoms)
        The number of atoms in "Reference"...                   	20  (7 H atoms)
    
        No further modifications were performed.           
    
        Final global atom count (number of hydrogens retained)...	20  (7 H atoms)
    
    * Transformation of the molecules into "Standard Orientation":
      1. The center of mass was shifted to the Cartesian origin.
      2. The moment of inertia tensor was constructed, diagonalized
         and the eigenvectors rotated on the x, y and z axes.
    
    * Details of the matching process:
        Structures were matched...                              	True
        Applied matching algorithm...                           	distance
        Solver used for matching...                             	hungarian
        Solution of the matching problem...                     	regular
        Number of highest deviations to be shown...             	5
    
        The highest deviations were between the pairs...           [Angstrom]
    				H-3 -- H-3                       0.51023
    				H-5 -- H-5                       0.53943
    				H-6 -- H-6                       0.57067
    			       O-20 -- O-20                      0.59816
    			       O-17 -- O-17                      0.72202
        The RMSD after the initial matching was [Angstrom]..    	0.21397
    
    * Kabsch alignment:
        # General settings
        Substructures were defined...                           	False
        Weighting function for Kabsch algorithm...              	none
        Consideration of multi-center-contributions...          	False
    
        # Differentiation criteria and color information
        Number of colors for aRMSD plot...                      	19
        Maximum RMSD value for color projection [Angstrom]..    	0.7
        Threshold for bond comparison [Angstrom]...             	0.02
        Number of distance pairs above threshold...             	12
        Percentage of the colored intersections...              	10.0
        Color for shorter bonds in "Model" vs. "Reference"...   	#006400  [HEX]
        Color for longer bonds in "Model" vs. "Reference"...    	#CD0000  [HEX]
        Number of bonds below threshold...                      	12
        Color of "Model"...                                     	#CD0000  [HEX]
        Color of "Reference"...                                 	#006400  [HEX]
    
        Final rotation matrix from 'Standard Orientation':
    
    	   |-0.99991965  -0.01140142  +0.00554066|
         U  =  |-0.01160250  +0.99922073  -0.03772691|
    	   |-0.00510620  -0.03778816  -0.99927273|
    
        # This matrix aligns Model with Reference.
        # U already includes all custom symmetry operations!
    
    
    
    * Final Quality of the Superposition:                 
    
        RMSD (Kabsch test, refined superposition [Angstrom])... 	0.20276
        Superposition R^2 (dimensionless)...                    	0.99498
        Cosine similarity (dimensionless)...                    	0.99732
        d values for the GARD calculation...                    	0.3, 1.2
        GARD score (dimensionless)...                           	0.80827
    
        For an introduction into the GARD calculation, see J. C. Baber,
        D. C. Thompson, J. B. Cross and C. Humblet, J. Chem. Inf. Model.,
        2009, 49, 1889-1900, doi: 10.1021/ci9001074.
    
    
    * Decomposition into different atom types          absolute     relative
    						  [Angstrom]      [%]
    			      C    (#  9)          0.11501      (08.47)
    			      H    (#  7)          0.20954      (28.13)
    			      O    (#  4)          0.31458      (63.40)
    
        z-matrix properties:
        # z-matrices are created for both molecules, based on
        # (3 N - 1) bond distances, (3 N - 2) bond angles and
        # (3 N - 3) dihedral angles.  Both the total RMSD and
        # the relative contributions are calculated.
        RMSD [Angstrom]...                                      	0.38110
        Contribution of distances...                            	22.92  [%]
        Contribution of angles...                               	43.59  [%]
        Contribution of dihedral angles...                      	33.49  [%]
    
    * Evaluation of structural parameters:
        # 1. The RMSE values are the root-mean-square errors
        #    between the corresponding properties of the two tructures.
        # 2. The R**2 values are the the correlation coefficients
        #    between the two data sets.
    
        Number of bonds...                                      	20
        R**2 of linear correlation (dimensionless)...           	0.95580
        RMSE [Angstrom]...                                      	0.05040
    
        Number of bond types...                                 	3
        R**2 of linear correlation (dimensionless)...           	0.95580
        RMSE [Angstrom]...                                      	0.03120
    
        Number of angles...                                     	62
        R**2 of linear correlation (dimensionless)...           	0.75713
        RMSE [degrees]...                                       	2.83420
    
        Number of dihedrals...                                  	148
        R**2 of linear correlation (dimensionless)...           	0.99617
        RMSE [degrees]...                                       	4.25830
    
    
    *** End of log file ***                               


## complete *terminal log* by aRMSD for the successful comparison of xyz-data

The following is the *complete* output `aRMSD` generates on the
terminal while comparing model `M1.xyz` with model `M2.xyz`
*successfully*.  Operating system was Xubuntu 18.04.1.

    ================================================================================
    			  aRMSD (version 0.9.8, 2018)                           
    ================================================================================
    	       A. Wagner, University of Heidelberg (2015, 2017),                
    			   forked by N. Behrnd (2018)                           
    
    --------------------------------- Description ----------------------------------
    Key features:
    * Parses data from various file formats
    * Establishes consistency and matches coordinate sequences of two molecules
    * Aligns two molecular structures based on the Kabsch algorithm
    * Supports different weighting functions for the superposition
    * Supports error propagation for experimental structures
    * Generates different visualization types of the superposition results
    * Writes outfiles that can be passed to other programs
    * The original version was created by A. Wagner under Windows.  You find it
          hosted on GitHub: https://github.com/armsd/aRMSD.
    * You are using a derivative fork based on the former, developed under Linux
          by N. Behrnd, hosted on GitHub: https://github.com/nbehrnd/aRMSD.
    
    *** Cite this program as:
        A. Wagner, H.-J. Himmel, J. Chem. Inf. Model, 2017, 57, 428-438
        (doi: 10.1021/acs.jcim.6b00516); with address and version of aRMSD used.
    
    Release dates of the individual modules:
    - core module:    	'2018-10-24'
    - plot module:    	'2016-11-03'
    - log  module:    	'2018-11-28'
    
    Module check:
    - numpy         	'1.13.3'
    - VTK           	'6.3.0'
    - matplotlib    	'2.1.1'
    - uncertainties 	'2.4.4'
    - openbabel     	'2.3.2'
    --------------------------------------------------------------------------------
    
    Enter the file name with extension for the first file (comp./model)
    >> M1.xyz
    
    > 'M1.xyz' has been loaded successfully! (#Atoms: 20)
    
    Enter the file name with extension for the second file (exp./reference)
    >> M2.xyz
    
    > 'M2.xyz' has been loaded successfully! (#Atoms: 20)
    --------------------------------------------------------------------------------
    ... Files have been loaded!
    
    --------------------------------------------------------------------------------
    > Checking for coordinate standard deviations...
    ... No standard deviations were found!
    --------------------------------------------------------------------------------
    
      Checking length unit of xyz coordinates ...
      The coordinate unit is [Angstrom]
    
      Checking length unit of xyz coordinates ...
      The coordinate unit is [Angstrom]
    
    > The current status was saved successfully!
    
    
    --------------------------------------------------------------------------------
    ================ Consistency Checks and Structural Modification ================
    --------------------------------------------------------------------------------
    
    > Performing consistency checks ... (Number of atoms: 20, 20)
      There are (7 & 7) H atoms in the molecules
    
    > The structures of both molecules are consistent.
    
    --------------------------------------------------------------------------------
        What should happen to the remaining 7 H-atoms?
    --------------------------------------------------------------------------------
        Info: The exclusion of H-atoms in RMSD calculations is recommended if
    	  they were not located and refined in the X-ray experiment
    --------------------------------------------------------------------------------
    0   ... remove all hydrogen atoms (7)
    3   ... keep all hydrogen atoms
    --------------------------------------------------------------------------------
    
    >>  Enter your choice: 3
    
    > The molecules were rotated into 'Standard Orientation' ...
    
    > The current status was saved successfully!
    
    --------------------------------------------------------------------------------
    =================== Symmetry Adjustments & Sequence Matching ===================
    --------------------------------------------------------------------------------
    -6  Set number of deviations which are highlighted in the plot (current = 5)
    -5  Load the saved status (save point available: 'True')
    -4  Change plot settings
    -3  Manually swap atoms in Model structure
    -2  Change matching algorithm or solver
    -1  Match molecular sequences based on current alignment
    --------------------------------------------------------------------------------
        Current matching algorithm  : 'distance'
        Current matching solver     : 'hungarian'
        Structures were matched     : 'False'
    --------------------------------------------------------------------------------
    0   ... exit the menu (no return)
    1   ... inversion at the origin
    2   ... reflection at the xy plane
    3   ... reflection at the xz plane
    4   ... reflection at the yz plane
    5   ... rotation around the x axis
    6   ... rotation around the y axis
    7   ... rotation around the z axis
    8   ... show the molecules again
    --------------------------------------------------------------------------------
    10  ... save current changes (status was saved: 'True')
    20  ... export structures
    --------------------------------------------------------------------------------
    
    > Results are now shown in a separate window.
    ... To continue, quit the pop-up window with 'q'.
    > To save the scene as *.png, press 's'.
    
    >>  Enter your choice: 1
    
    > Inversion of 'Model' structure at the origin of the coordinate system ...
    
    --------------------------------------------------------------------------------
    =================== Symmetry Adjustments & Sequence Matching ===================
    --------------------------------------------------------------------------------
    -6  Set number of deviations which are highlighted in the plot (current = 5)
    -5  Load the saved status (save point available: 'True')
    -4  Change plot settings
    -3  Manually swap atoms in Model structure
    -2  Change matching algorithm or solver
    -1  Match molecular sequences based on current alignment
    --------------------------------------------------------------------------------
        Current matching algorithm  : 'distance'
        Current matching solver     : 'hungarian'
        Structures were matched     : 'False'
    --------------------------------------------------------------------------------
    0   ... exit the menu (no return)
    1   ... inversion at the origin
    2   ... reflection at the xy plane
    3   ... reflection at the xz plane
    4   ... reflection at the yz plane
    5   ... rotation around the x axis
    6   ... rotation around the y axis
    7   ... rotation around the z axis
    8   ... show the molecules again
    --------------------------------------------------------------------------------
    10  ... save current changes (status was saved: 'True')
    20  ... export structures
    --------------------------------------------------------------------------------
    
    > Results are now shown in a separate window.
    ... To continue, quit the pop-up window with 'q'.
    > To save the scene as *.png, press 's'.
    
    >>  Enter your choice: 3
    
    > Reflection of 'Model' structure at the xz-plane ...
    
    --------------------------------------------------------------------------------
    =================== Symmetry Adjustments & Sequence Matching ===================
    --------------------------------------------------------------------------------
    -6  Set number of deviations which are highlighted in the plot (current = 5)
    -5  Load the saved status (save point available: 'True')
    -4  Change plot settings
    -3  Manually swap atoms in Model structure
    -2  Change matching algorithm or solver
    -1  Match molecular sequences based on current alignment
    --------------------------------------------------------------------------------
        Current matching algorithm  : 'distance'
        Current matching solver     : 'hungarian'
        Structures were matched     : 'False'
    --------------------------------------------------------------------------------
    0   ... exit the menu (no return)
    1   ... inversion at the origin
    2   ... reflection at the xy plane
    3   ... reflection at the xz plane
    4   ... reflection at the yz plane
    5   ... rotation around the x axis
    6   ... rotation around the y axis
    7   ... rotation around the z axis
    8   ... show the molecules again
    --------------------------------------------------------------------------------
    10  ... save current changes (status was saved: 'True')
    20  ... export structures
    --------------------------------------------------------------------------------
    
    > Results are now shown in a separate window.
    ... To continue, quit the pop-up window with 'q'.
    > To save the scene as *.png, press 's'.
    
    >>  Enter your choice: 10
    
    > The current status was saved successfully!
    
    --------------------------------------------------------------------------------
    =================== Symmetry Adjustments & Sequence Matching ===================
    --------------------------------------------------------------------------------
    -6  Set number of deviations which are highlighted in the plot (current = 5)
    -5  Load the saved status (save point available: 'True')
    -4  Change plot settings
    -3  Manually swap atoms in Model structure
    -2  Change matching algorithm or solver
    -1  Match molecular sequences based on current alignment
    --------------------------------------------------------------------------------
        Current matching algorithm  : 'distance'
        Current matching solver     : 'hungarian'
        Structures were matched     : 'False'
    --------------------------------------------------------------------------------
    0   ... exit the menu (no return)
    1   ... inversion at the origin
    2   ... reflection at the xy plane
    3   ... reflection at the xz plane
    4   ... reflection at the yz plane
    5   ... rotation around the x axis
    6   ... rotation around the y axis
    7   ... rotation around the z axis
    8   ... show the molecules again
    --------------------------------------------------------------------------------
    10  ... save current changes (status was saved: 'True')
    20  ... export structures
    --------------------------------------------------------------------------------
    
    >>  Enter your choice: -1
    
    --------------------------------------------------------------------------------
    
    	The geometric RMSD of the current alignment is:  0.214 A
    
    		 The 5 most disordered atom pairs are:
    		Entry		      Pair		  Distance / A 
    		  5		   H-3 -- H-3   	    0.510
    		  4		   H-5 -- H-5   	    0.539
    		  3		   H-6 -- H-6   	    0.571
    		  2		  O-20 -- O-20  	    0.598
    		  1		  O-17 -- O-17  	    0.722
    
    --------------------------------------------------------------------------------
    =================== Symmetry Adjustments & Sequence Matching ===================
    --------------------------------------------------------------------------------
    -6  Set number of deviations which are highlighted in the plot (current = 5)
    -5  Load the saved status (save point available: 'True')
    -4  Change plot settings
    -3  Manually swap atoms in Model structure
    -2  Change matching algorithm or solver
    -1  Match molecular sequences based on current alignment
    --------------------------------------------------------------------------------
        Current matching algorithm  : 'distance'
        Current matching solver     : 'hungarian'
        Structures were matched     : 'True'
    --------------------------------------------------------------------------------
    0   ... exit the menu (no return)
    1   ... inversion at the origin
    2   ... reflection at the xy plane
    3   ... reflection at the xz plane
    4   ... reflection at the yz plane
    5   ... rotation around the x axis
    6   ... rotation around the y axis
    7   ... rotation around the z axis
    8   ... show the molecules again
    --------------------------------------------------------------------------------
    10  ... save current changes (status was saved: 'True')
    20  ... export structures
    --------------------------------------------------------------------------------
    
    > Results are now shown in a separate window.
    ... To continue, quit the pop-up window with 'q'.
    > To save the scene as *.png, press 's'.
    
    >>  Enter your choice: 10
    
    > The current status was saved successfully!
    
    --------------------------------------------------------------------------------
    =================== Symmetry Adjustments & Sequence Matching ===================
    --------------------------------------------------------------------------------
    -6  Set number of deviations which are highlighted in the plot (current = 5)
    -5  Load the saved status (save point available: 'True')
    -4  Change plot settings
    -3  Manually swap atoms in Model structure
    -2  Change matching algorithm or solver
    -1  Match molecular sequences based on current alignment
    --------------------------------------------------------------------------------
        Current matching algorithm  : 'distance'
        Current matching solver     : 'hungarian'
        Structures were matched     : 'True'
    --------------------------------------------------------------------------------
    0   ... exit the menu (no return)
    1   ... inversion at the origin
    2   ... reflection at the xy plane
    3   ... reflection at the xz plane
    4   ... reflection at the yz plane
    5   ... rotation around the x axis
    6   ... rotation around the y axis
    7   ... rotation around the z axis
    8   ... show the molecules again
    --------------------------------------------------------------------------------
    10  ... save current changes (status was saved: 'True')
    20  ... export structures
    --------------------------------------------------------------------------------
    
    >>  Enter your choice: 0
    
    > Exiting symmetry transformation menu ...
    
    --------------------------------------------------------------------------------
    <built-in method center of str object at 0x7feaeab0aad8> =
    --------------------------------------------------------------------------------
    -10 Exit aRMSD
    -8  Plot aRMSD color map
    -7  Change general RMSD settings
    -6  Add/remove bond
    -4  Change plot settings
    -3  Define two substructures (structures are defined: 'False')
    -2  Change weighting function
    -1  Perform Kabsch alignment (required for all functions)
    --------------------------------------------------------------------------------
        Current weighting function  : 'none'
        Calculate mcc contribution  : 'False'
        Kabsch alignment performed  : 'False'
    --------------------------------------------------------------------------------
    0   ... visualize results in aRMSD representation
    1   ... visualize structural superposition
    2   ... perform statistic investigation of bond lengths and angles
    3   ... show RMSD results
    4   ... interpolate between the structures (cart., 10 steps)
    5   ... generate outfile
    20  ... export structural data
    --------------------------------------------------------------------------------
    
    >>  Enter your choice: -1
    
    --------------------------------------------------------------------------------
    ========================= Quality of the Superposition =========================
    --------------------------------------------------------------------------------
    
    > The type of weighting function is: 'none'
    
    
    ---------------------------- Similarity Descriptors ----------------------------
       >>>   Superposition R^2 :  0.99498
       >>>   Cosine similarity :  0.99732
       >>>   GARD score        :  0.80827
    
    
    -------------------------- Root-Mean-Square-Deviation --------------------------
       >>>   RMSD              :  0.20276 Angstrom
    
       >>>   - Decomposition   :  Individual atom types  (total percentage)
    	   C    (#  9)     :  0.11501 Angstrom  (08.47 %)
    	   H    (#  7)     :  0.20954 Angstrom  (28.13 %)
    	   O    (#  4)     :  0.31458 Angstrom  (63.40 %)
    
    
    ----------------------------- Z-matrix properties ------------------------------
       >>>   RMSD              :  0.38110
    
       >>>   - Decomposition   :  total percentage
    	     distances     :  22.92 %
    	     angles        :  43.59 %
    	     dihedrals     :  33.49 %
    
    --------------------------------------------------------------------------------
    <built-in method center of str object at 0x7feaeab0aad8> =
    --------------------------------------------------------------------------------
    -10 Exit aRMSD
    -8  Plot aRMSD color map
    -7  Change general RMSD settings
    -6  Add/remove bond
    -4  Change plot settings
    -3  Define two substructures (structures are defined: 'False')
    -2  Change weighting function
    -1  Perform Kabsch alignment (required for all functions)
    --------------------------------------------------------------------------------
        Current weighting function  : 'none'
        Calculate mcc contribution  : 'False'
        Kabsch alignment performed  : 'True'
    --------------------------------------------------------------------------------
    0   ... visualize results in aRMSD representation
    1   ... visualize structural superposition
    2   ... perform statistic investigation of bond lengths and angles
    3   ... show RMSD results
    4   ... interpolate between the structures (cart., 10 steps)
    5   ... generate outfile
    20  ... export structural data
    --------------------------------------------------------------------------------
    
    >>  Enter your choice: 0
    
    > Results are now shown in a separate window.
    ... To continue, quit the pop-up window with 'q'.
    > To save the scene as *.png, press 's'.
    
    --------------------------------------------------------------------------------
    <built-in method center of str object at 0x7feaeab0aad8> =
    --------------------------------------------------------------------------------
    -10 Exit aRMSD
    -8  Plot aRMSD color map
    -7  Change general RMSD settings
    -6  Add/remove bond
    -4  Change plot settings
    -3  Define two substructures (structures are defined: 'False')
    -2  Change weighting function
    -1  Perform Kabsch alignment (required for all functions)
    --------------------------------------------------------------------------------
        Current weighting function  : 'none'
        Calculate mcc contribution  : 'False'
        Kabsch alignment performed  : 'True'
    --------------------------------------------------------------------------------
    0   ... visualize results in aRMSD representation
    1   ... visualize structural superposition
    2   ... perform statistic investigation of bond lengths and angles
    3   ... show RMSD results
    4   ... interpolate between the structures (cart., 10 steps)
    5   ... generate outfile
    20  ... export structural data
    --------------------------------------------------------------------------------
    
    >>  Enter your choice: 1
    
    > Results are now shown in a separate window.
    ... To continue, quit the pop-up window with 'q'.
    > To save the scene as *.png, press 's'.
    
    --------------------------------------------------------------------------------
    <built-in method center of str object at 0x7feaeab0aad8> =
    --------------------------------------------------------------------------------
    -10 Exit aRMSD
    -8  Plot aRMSD color map
    -7  Change general RMSD settings
    -6  Add/remove bond
    -4  Change plot settings
    -3  Define two substructures (structures are defined: 'False')
    -2  Change weighting function
    -1  Perform Kabsch alignment (required for all functions)
    --------------------------------------------------------------------------------
        Current weighting function  : 'none'
        Calculate mcc contribution  : 'False'
        Kabsch alignment performed  : 'True'
    --------------------------------------------------------------------------------
    0   ... visualize results in aRMSD representation
    1   ... visualize structural superposition
    2   ... perform statistic investigation of bond lengths and angles
    3   ... show RMSD results
    4   ... interpolate between the structures (cart., 10 steps)
    5   ... generate outfile
    20  ... export structural data
    --------------------------------------------------------------------------------
    
    >>  Enter your choice: 2
    
    > Results are now shown in a separate window.
    ... To continue, quit the pop-up window with 'q'.
    
    
    ---------------- The Highest Deviations in Internal Coordinates ----------------
    The 3 highest deviations are printed below
    Entries are: Atoms, values in the Model and Reference, difference
    --------------------------------------------------------------------------------
     >> Bonds (in Angstrom):
        1.  [C-15, C-16] 1.455 1.598	Diff. 0.143
        2.  [C-8, O-17] 1.252 1.144	Diff. -0.108
        3.  [C-8, C-9] 1.49 1.549	Diff. 0.059
    --------------------------------------------------------------------------------
     >> Bond angles (in deg.):
        1.  [O-18, C-8, O-17] 119.78 128.521	Diff. 8.741
        2.  [O-17, C-8, O-18] 119.78 128.521	Diff. 8.741
        3.  [C-9, C-8, O-18] 117.731 112.838	Diff. -4.893
    --------------------------------------------------------------------------------
     >> Dihedral angles (in deg.):
        1.  [C-14, C-9, C-8, O-18] 35.01 50.069	Diff. 15.059
        2.  [O-18, C-8, C-9, C-14] 35.01 50.069	Diff. 15.059
        3.  [O-17, C-8, C-9, C-14] 144.42 130.333	Diff. -14.087
    --------------------------------------------------------------------------------
    
    --------------------------------------------------------------------------------
    <built-in method center of str object at 0x7feaeab0aad8> =
    --------------------------------------------------------------------------------
    -10 Exit aRMSD
    -8  Plot aRMSD color map
    -7  Change general RMSD settings
    -6  Add/remove bond
    -4  Change plot settings
    -3  Define two substructures (structures are defined: 'False')
    -2  Change weighting function
    -1  Perform Kabsch alignment (required for all functions)
    --------------------------------------------------------------------------------
        Current weighting function  : 'none'
        Calculate mcc contribution  : 'False'
        Kabsch alignment performed  : 'True'
    --------------------------------------------------------------------------------
    0   ... visualize results in aRMSD representation
    1   ... visualize structural superposition
    2   ... perform statistic investigation of bond lengths and angles
    3   ... show RMSD results
    4   ... interpolate between the structures (cart., 10 steps)
    5   ... generate outfile
    20  ... export structural data
    --------------------------------------------------------------------------------
    
    >>  Enter your choice: 3
    
    --------------------------------------------------------------------------------
    ========================= Quality of the Superposition =========================
    --------------------------------------------------------------------------------
    
    > The type of weighting function is: 'none'
    
    
    ---------------------------- Similarity Descriptors ----------------------------
       >>>   Superposition R^2 :  0.99498
       >>>   Cosine similarity :  0.99732
       >>>   GARD score        :  0.80827
    
    
    -------------------------- Root-Mean-Square-Deviation --------------------------
       >>>   RMSD              :  0.20276 Angstrom
    
       >>>   - Decomposition   :  Individual atom types  (total percentage)
    	   C    (#  9)     :  0.11501 Angstrom  (08.47 %)
    	   H    (#  7)     :  0.20954 Angstrom  (28.13 %)
    	   O    (#  4)     :  0.31458 Angstrom  (63.40 %)
    
    
    ----------------------------- Z-matrix properties ------------------------------
       >>>   RMSD              :  0.38110
    
       >>>   - Decomposition   :  total percentage
    	     distances     :  22.92 %
    	     angles        :  43.59 %
    	     dihedrals     :  33.49 %
    
    --------------------------------------------------------------------------------
    <built-in method center of str object at 0x7feaeab0aad8> =
    --------------------------------------------------------------------------------
    -10 Exit aRMSD
    -8  Plot aRMSD color map
    -7  Change general RMSD settings
    -6  Add/remove bond
    -4  Change plot settings
    -3  Define two substructures (structures are defined: 'False')
    -2  Change weighting function
    -1  Perform Kabsch alignment (required for all functions)
    --------------------------------------------------------------------------------
        Current weighting function  : 'none'
        Calculate mcc contribution  : 'False'
        Kabsch alignment performed  : 'True'
    --------------------------------------------------------------------------------
    0   ... visualize results in aRMSD representation
    1   ... visualize structural superposition
    2   ... perform statistic investigation of bond lengths and angles
    3   ... show RMSD results
    4   ... interpolate between the structures (cart., 10 steps)
    5   ... generate outfile
    20  ... export structural data
    --------------------------------------------------------------------------------
    
    >>  Enter your choice: 5
    
    > A logfile (aRMSD_logfile.out) has been written successfully!
    
    --------------------------------------------------------------------------------
    <built-in method center of str object at 0x7feaeab0aad8> =
    --------------------------------------------------------------------------------
    -10 Exit aRMSD
    -8  Plot aRMSD color map
    -7  Change general RMSD settings
    -6  Add/remove bond
    -4  Change plot settings
    -3  Define two substructures (structures are defined: 'False')
    -2  Change weighting function
    -1  Perform Kabsch alignment (required for all functions)
    --------------------------------------------------------------------------------
        Current weighting function  : 'none'
        Calculate mcc contribution  : 'False'
        Kabsch alignment performed  : 'True'
    --------------------------------------------------------------------------------
    0   ... visualize results in aRMSD representation
    1   ... visualize structural superposition
    2   ... perform statistic investigation of bond lengths and angles
    3   ... show RMSD results
    4   ... interpolate between the structures (cart., 10 steps)
    5   ... generate outfile
    20  ... export structural data
    --------------------------------------------------------------------------------
    
    >>  Enter your choice: -10
    
    --------------------------------------------------------------------------------
    ========================== Normal program termination ==========================
    --------------------------------------------------------------------------------


## complete *terminal log* by aRMSD for the successful comparison of pdb-data

The following is the *complete* output `aRMSD` generates on the
terminal while comparing model `M1.pdb` with model `M2.pdb`
*successfully*.  Operating system was Debian 10 (testing / Buster).

    ================================================================================
    			  aRMSD (version 0.9.8, 2018)                           
    ================================================================================
    	       A. Wagner, University of Heidelberg (2015, 2017),                
    			   forked by N. Behrnd (2018)                           
    
    --------------------------------- Description ----------------------------------
    Key features:
    * Parses data from various file formats
    * Establishes consistency and matches coordinate sequences of two molecules
    * Aligns two molecular structures based on the Kabsch algorithm
    * Supports different weighting functions for the superposition
    * Supports error propagation for experimental structures
    * Generates different visualization types of the superposition results
    * Writes outfiles that can be passed to other programs
    * The original version was created by A. Wagner under Windows.  You find it
          hosted on GitHub: https://github.com/armsd/aRMSD.
    * You are using a derivative fork based on the former, developed under Linux
          by N. Behrnd, hosted on GitHub: https://github.com/nbehrnd/aRMSD.
    
    *** Cite this program as:
        A. Wagner, H.-J. Himmel, J. Chem. Inf. Model, 2017, 57, 428-438
        (doi: 10.1021/acs.jcim.6b00516); with address and version of aRMSD used.
    
    Release dates of the individual modules:
    - core module:    	'2018-10-24'
    - plot module:    	'2016-11-03'
    - log  module:    	'2018-11-28'
    
    Module check:
    - numpy         	'1.14.5'
    - VTK           	'6.3.0'
    - matplotlib    	'2.2.2'
    - uncertainties 	'3.0.2'
    - openbabel     	'2.4.1'
    --------------------------------------------------------------------------------
    
    Enter the file name with extension for the first file (comp./model)
    >> M1.cif
    
    > ERROR: File type is not supported by openbabel!
    
    Enter the file name with extension for the first file (comp./model)
    >> M1.pdb
    
    > 'M1.pdb' has been loaded successfully! (#Atoms: 20)
    
    Enter the file name with extension for the second file (exp./reference)
    >> M2.pdb
    
    > 'M2.pdb' has been loaded successfully! (#Atoms: 20)
    --------------------------------------------------------------------------------
    ... Files have been loaded!
    
    --------------------------------------------------------------------------------
    > Checking for coordinate standard deviations...
    ... No standard deviations were found!
    --------------------------------------------------------------------------------
    
      Checking length unit of xyz coordinates ...
      The coordinate unit is [Angstrom]
    
      Checking length unit of xyz coordinates ...
      The coordinate unit is [Angstrom]
    
    > The current status was saved successfully!
    
    
    --------------------------------------------------------------------------------
    ================ Consistency Checks and Structural Modification ================
    --------------------------------------------------------------------------------
    
    > Performing consistency checks ... (Number of atoms: 20, 20)
      There are (7 & 7) H atoms in the molecules
    
    > The structures of both molecules are consistent.
    
    --------------------------------------------------------------------------------
        What should happen to the remaining 7 H-atoms?
    --------------------------------------------------------------------------------
        Info: The exclusion of H-atoms in RMSD calculations is recommended if
    	  they were not located and refined in the X-ray experiment
    --------------------------------------------------------------------------------
    0   ... remove all hydrogen atoms (7)
    3   ... keep all hydrogen atoms
    --------------------------------------------------------------------------------
    
    >>  Enter your choice: 3
    
    > The molecules were rotated into 'Standard Orientation' ...
    
    > The current status was saved successfully!
    
    --------------------------------------------------------------------------------
    =================== Symmetry Adjustments & Sequence Matching ===================
    --------------------------------------------------------------------------------
    -6  Set number of deviations which are highlighted in the plot (current = 5)
    -5  Load the saved status (save point available: 'True')
    -4  Change plot settings
    -3  Manually swap atoms in Model structure
    -2  Change matching algorithm or solver
    -1  Match molecular sequences based on current alignment
    --------------------------------------------------------------------------------
        Current matching algorithm  : 'distance'
        Current matching solver     : 'hungarian'
        Structures were matched     : 'False'
    --------------------------------------------------------------------------------
    0   ... exit the menu (no return)
    1   ... inversion at the origin
    2   ... reflection at the xy plane
    3   ... reflection at the xz plane
    4   ... reflection at the yz plane
    5   ... rotation around the x axis
    6   ... rotation around the y axis
    7   ... rotation around the z axis
    8   ... show the molecules again
    --------------------------------------------------------------------------------
    10  ... save current changes (status was saved: 'True')
    20  ... export structures
    --------------------------------------------------------------------------------
    
    > Results are now shown in a separate window.
    ... To continue, quit the pop-up window with 'q'.
    > To save the scene as *.png, press 's'.
    
    >>  Enter your choice: 1
    
    > Inversion of 'Model' structure at the origin of the coordinate system ...
    
    --------------------------------------------------------------------------------
    =================== Symmetry Adjustments & Sequence Matching ===================
    --------------------------------------------------------------------------------
    -6  Set number of deviations which are highlighted in the plot (current = 5)
    -5  Load the saved status (save point available: 'True')
    -4  Change plot settings
    -3  Manually swap atoms in Model structure
    -2  Change matching algorithm or solver
    -1  Match molecular sequences based on current alignment
    --------------------------------------------------------------------------------
        Current matching algorithm  : 'distance'
        Current matching solver     : 'hungarian'
        Structures were matched     : 'False'
    --------------------------------------------------------------------------------
    0   ... exit the menu (no return)
    1   ... inversion at the origin
    2   ... reflection at the xy plane
    3   ... reflection at the xz plane
    4   ... reflection at the yz plane
    5   ... rotation around the x axis
    6   ... rotation around the y axis
    7   ... rotation around the z axis
    8   ... show the molecules again
    --------------------------------------------------------------------------------
    10  ... save current changes (status was saved: 'True')
    20  ... export structures
    --------------------------------------------------------------------------------
    
    > Results are now shown in a separate window.
    ... To continue, quit the pop-up window with 'q'.
    > To save the scene as *.png, press 's'.
    
    >>  Enter your choice: 2
    
    > Reflection of 'Model' structure at the xy-plane ...
    
    --------------------------------------------------------------------------------
    =================== Symmetry Adjustments & Sequence Matching ===================
    --------------------------------------------------------------------------------
    -6  Set number of deviations which are highlighted in the plot (current = 5)
    -5  Load the saved status (save point available: 'True')
    -4  Change plot settings
    -3  Manually swap atoms in Model structure
    -2  Change matching algorithm or solver
    -1  Match molecular sequences based on current alignment
    --------------------------------------------------------------------------------
        Current matching algorithm  : 'distance'
        Current matching solver     : 'hungarian'
        Structures were matched     : 'False'
    --------------------------------------------------------------------------------
    0   ... exit the menu (no return)
    1   ... inversion at the origin
    2   ... reflection at the xy plane
    3   ... reflection at the xz plane
    4   ... reflection at the yz plane
    5   ... rotation around the x axis
    6   ... rotation around the y axis
    7   ... rotation around the z axis
    8   ... show the molecules again
    --------------------------------------------------------------------------------
    10  ... save current changes (status was saved: 'True')
    20  ... export structures
    --------------------------------------------------------------------------------
    
    > Results are now shown in a separate window.
    ... To continue, quit the pop-up window with 'q'.
    > To save the scene as *.png, press 's'.
    
    >>  Enter your choice: 10
    
    > The current status was saved successfully!
    
    --------------------------------------------------------------------------------
    =================== Symmetry Adjustments & Sequence Matching ===================
    --------------------------------------------------------------------------------
    -6  Set number of deviations which are highlighted in the plot (current = 5)
    -5  Load the saved status (save point available: 'True')
    -4  Change plot settings
    -3  Manually swap atoms in Model structure
    -2  Change matching algorithm or solver
    -1  Match molecular sequences based on current alignment
    --------------------------------------------------------------------------------
        Current matching algorithm  : 'distance'
        Current matching solver     : 'hungarian'
        Structures were matched     : 'False'
    --------------------------------------------------------------------------------
    0   ... exit the menu (no return)
    1   ... inversion at the origin
    2   ... reflection at the xy plane
    3   ... reflection at the xz plane
    4   ... reflection at the yz plane
    5   ... rotation around the x axis
    6   ... rotation around the y axis
    7   ... rotation around the z axis
    8   ... show the molecules again
    --------------------------------------------------------------------------------
    10  ... save current changes (status was saved: 'True')
    20  ... export structures
    --------------------------------------------------------------------------------
    
    >>  Enter your choice: -1
    
    --------------------------------------------------------------------------------
    
    	The geometric RMSD of the current alignment is:  0.214 A
    
    		 The 5 most disordered atom pairs are:
    		Entry		      Pair		  Distance / A 
    		  5		   H-3 -- H-3   	    0.511
    		  4		   H-5 -- H-5   	    0.539
    		  3		   H-6 -- H-6   	    0.571
    		  2		  O-20 -- O-20  	    0.598
    		  1		  O-17 -- O-17  	    0.722
    
    --------------------------------------------------------------------------------
    =================== Symmetry Adjustments & Sequence Matching ===================
    --------------------------------------------------------------------------------
    -6  Set number of deviations which are highlighted in the plot (current = 5)
    -5  Load the saved status (save point available: 'True')
    -4  Change plot settings
    -3  Manually swap atoms in Model structure
    -2  Change matching algorithm or solver
    -1  Match molecular sequences based on current alignment
    --------------------------------------------------------------------------------
        Current matching algorithm  : 'distance'
        Current matching solver     : 'hungarian'
        Structures were matched     : 'True'
    --------------------------------------------------------------------------------
    0   ... exit the menu (no return)
    1   ... inversion at the origin
    2   ... reflection at the xy plane
    3   ... reflection at the xz plane
    4   ... reflection at the yz plane
    5   ... rotation around the x axis
    6   ... rotation around the y axis
    7   ... rotation around the z axis
    8   ... show the molecules again
    --------------------------------------------------------------------------------
    10  ... save current changes (status was saved: 'True')
    20  ... export structures
    --------------------------------------------------------------------------------
    
    > Results are now shown in a separate window.
    ... To continue, quit the pop-up window with 'q'.
    > To save the scene as *.png, press 's'.
    
    >>  Enter your choice: 10
    
    > The current status was saved successfully!
    
    --------------------------------------------------------------------------------
    =================== Symmetry Adjustments & Sequence Matching ===================
    --------------------------------------------------------------------------------
    -6  Set number of deviations which are highlighted in the plot (current = 5)
    -5  Load the saved status (save point available: 'True')
    -4  Change plot settings
    -3  Manually swap atoms in Model structure
    -2  Change matching algorithm or solver
    -1  Match molecular sequences based on current alignment
    --------------------------------------------------------------------------------
        Current matching algorithm  : 'distance'
        Current matching solver     : 'hungarian'
        Structures were matched     : 'True'
    --------------------------------------------------------------------------------
    0   ... exit the menu (no return)
    1   ... inversion at the origin
    2   ... reflection at the xy plane
    3   ... reflection at the xz plane
    4   ... reflection at the yz plane
    5   ... rotation around the x axis
    6   ... rotation around the y axis
    7   ... rotation around the z axis
    8   ... show the molecules again
    --------------------------------------------------------------------------------
    10  ... save current changes (status was saved: 'True')
    20  ... export structures
    --------------------------------------------------------------------------------
    
    >>  Enter your choice: 0
    
    > Exiting symmetry transformation menu ...
    
    --------------------------------------------------------------------------------
    <built-in method center of str object at 0x7f7ba4445240> =
    --------------------------------------------------------------------------------
    -10 Exit aRMSD
    -8  Plot aRMSD color map
    -7  Change general RMSD settings
    -6  Add/remove bond
    -4  Change plot settings
    -3  Define two substructures (structures are defined: 'False')
    -2  Change weighting function
    -1  Perform Kabsch alignment (required for all functions)
    --------------------------------------------------------------------------------
        Current weighting function  : 'none'
        Calculate mcc contribution  : 'False'
        Kabsch alignment performed  : 'False'
    --------------------------------------------------------------------------------
    0   ... visualize results in aRMSD representation
    1   ... visualize structural superposition
    2   ... perform statistic investigation of bond lengths and angles
    3   ... show RMSD results
    4   ... interpolate between the structures (cart., 10 steps)
    5   ... generate outfile
    20  ... export structural data
    --------------------------------------------------------------------------------
    
    >>  Enter your choice: -1
    
    --------------------------------------------------------------------------------
    ========================= Quality of the Superposition =========================
    --------------------------------------------------------------------------------
    
    > The type of weighting function is: 'none'
    
    
    ---------------------------- Similarity Descriptors ----------------------------
       >>>   Superposition R^2 :  0.99498
       >>>   Cosine similarity :  0.99731
       >>>   GARD score        :  0.80826
    
    
    -------------------------- Root-Mean-Square-Deviation --------------------------
       >>>   RMSD              :  0.20276 Angstrom
    
       >>>   - Decomposition   :  Individual atom types  (total percentage)
    	   C    (#  9)     :  0.11507 Angstrom  (08.48 %)
    	   H    (#  7)     :  0.20956 Angstrom  (28.14 %)
    	   O    (#  4)     :  0.31451 Angstrom  (63.38 %)
    
    
    ----------------------------- Z-matrix properties ------------------------------
       >>>   RMSD              :  0.38077
    
       >>>   - Decomposition   :  total percentage
    	     distances     :  22.96 %
    	     angles        :  43.37 %
    	     dihedrals     :  33.67 %
    
    --------------------------------------------------------------------------------
    <built-in method center of str object at 0x7f7ba4445240> =
    --------------------------------------------------------------------------------
    -10 Exit aRMSD
    -8  Plot aRMSD color map
    -7  Change general RMSD settings
    -6  Add/remove bond
    -4  Change plot settings
    -3  Define two substructures (structures are defined: 'False')
    -2  Change weighting function
    -1  Perform Kabsch alignment (required for all functions)
    --------------------------------------------------------------------------------
        Current weighting function  : 'none'
        Calculate mcc contribution  : 'False'
        Kabsch alignment performed  : 'True'
    --------------------------------------------------------------------------------
    0   ... visualize results in aRMSD representation
    1   ... visualize structural superposition
    2   ... perform statistic investigation of bond lengths and angles
    3   ... show RMSD results
    4   ... interpolate between the structures (cart., 10 steps)
    5   ... generate outfile
    20  ... export structural data
    --------------------------------------------------------------------------------
    
    >>  Enter your choice: 0
    
    > Results are now shown in a separate window.
    ... To continue, quit the pop-up window with 'q'.
    > To save the scene as *.png, press 's'.
    
    --------------------------------------------------------------------------------
    <built-in method center of str object at 0x7f7ba4445240> =
    --------------------------------------------------------------------------------
    -10 Exit aRMSD
    -8  Plot aRMSD color map
    -7  Change general RMSD settings
    -6  Add/remove bond
    -4  Change plot settings
    -3  Define two substructures (structures are defined: 'False')
    -2  Change weighting function
    -1  Perform Kabsch alignment (required for all functions)
    --------------------------------------------------------------------------------
        Current weighting function  : 'none'
        Calculate mcc contribution  : 'False'
        Kabsch alignment performed  : 'True'
    --------------------------------------------------------------------------------
    0   ... visualize results in aRMSD representation
    1   ... visualize structural superposition
    2   ... perform statistic investigation of bond lengths and angles
    3   ... show RMSD results
    4   ... interpolate between the structures (cart., 10 steps)
    5   ... generate outfile
    20  ... export structural data
    --------------------------------------------------------------------------------
    
    >>  Enter your choice: 1
    
    > Results are now shown in a separate window.
    ... To continue, quit the pop-up window with 'q'.
    > To save the scene as *.png, press 's'.
    
    --------------------------------------------------------------------------------
    <built-in method center of str object at 0x7f7ba4445240> =
    --------------------------------------------------------------------------------
    -10 Exit aRMSD
    -8  Plot aRMSD color map
    -7  Change general RMSD settings
    -6  Add/remove bond
    -4  Change plot settings
    -3  Define two substructures (structures are defined: 'False')
    -2  Change weighting function
    -1  Perform Kabsch alignment (required for all functions)
    --------------------------------------------------------------------------------
        Current weighting function  : 'none'
        Calculate mcc contribution  : 'False'
        Kabsch alignment performed  : 'True'
    --------------------------------------------------------------------------------
    0   ... visualize results in aRMSD representation
    1   ... visualize structural superposition
    2   ... perform statistic investigation of bond lengths and angles
    3   ... show RMSD results
    4   ... interpolate between the structures (cart., 10 steps)
    5   ... generate outfile
    20  ... export structural data
    --------------------------------------------------------------------------------
    
    >>  Enter your choice: 2
    
    > Results are now shown in a separate window.
    ... To continue, quit the pop-up window with 'q'.
    
    
    ---------------- The Highest Deviations in Internal Coordinates ----------------
    The 3 highest deviations are printed below
    Entries are: Atoms, values in the Model and Reference, difference
    --------------------------------------------------------------------------------
     >> Bonds (in Angstrom):
        1.  [C-15, C-16] 1.454 1.598	Diff. 0.14400000000000013
        2.  [C-8, O-17] 1.253 1.143	Diff. -0.10999999999999988
        3.  [C-8, C-9] 1.491 1.55	Diff. 0.05899999999999994
    --------------------------------------------------------------------------------
     >> Bond angles (in deg.):
        1.  [O-18, C-8, O-17] 119.817 128.56	Diff. 8.74300000000001
        2.  [O-17, C-8, O-18] 119.817 128.56	Diff. 8.74300000000001
        3.  [C-9, C-8, O-18] 117.728 112.809	Diff. -4.918999999999997
    --------------------------------------------------------------------------------
     >> Dihedral angles (in deg.):
        1.  [C-14, C-9, C-8, O-18] 35.066 50.081	Diff. 15.015
        2.  [O-18, C-8, C-9, C-14] 35.066 50.081	Diff. 15.015
        3.  [C-14, C-9, C-8, O-17] 144.442 130.267	Diff. -14.175000000000011
    --------------------------------------------------------------------------------
    
    --------------------------------------------------------------------------------
    <built-in method center of str object at 0x7f7ba4445240> =
    --------------------------------------------------------------------------------
    -10 Exit aRMSD
    -8  Plot aRMSD color map
    -7  Change general RMSD settings
    -6  Add/remove bond
    -4  Change plot settings
    -3  Define two substructures (structures are defined: 'False')
    -2  Change weighting function
    -1  Perform Kabsch alignment (required for all functions)
    --------------------------------------------------------------------------------
        Current weighting function  : 'none'
        Calculate mcc contribution  : 'False'
        Kabsch alignment performed  : 'True'
    --------------------------------------------------------------------------------
    0   ... visualize results in aRMSD representation
    1   ... visualize structural superposition
    2   ... perform statistic investigation of bond lengths and angles
    3   ... show RMSD results
    4   ... interpolate between the structures (cart., 10 steps)
    5   ... generate outfile
    20  ... export structural data
    --------------------------------------------------------------------------------
    
    >>  Enter your choice: 3
    
    --------------------------------------------------------------------------------
    ========================= Quality of the Superposition =========================
    --------------------------------------------------------------------------------
    
    > The type of weighting function is: 'none'
    
    
    ---------------------------- Similarity Descriptors ----------------------------
       >>>   Superposition R^2 :  0.99498
       >>>   Cosine similarity :  0.99731
       >>>   GARD score        :  0.80826
    
    
    -------------------------- Root-Mean-Square-Deviation --------------------------
       >>>   RMSD              :  0.20276 Angstrom
    
       >>>   - Decomposition   :  Individual atom types  (total percentage)
    	   C    (#  9)     :  0.11507 Angstrom  (08.48 %)
    	   H    (#  7)     :  0.20956 Angstrom  (28.14 %)
    	   O    (#  4)     :  0.31451 Angstrom  (63.38 %)
    
    
    ----------------------------- Z-matrix properties ------------------------------
       >>>   RMSD              :  0.38077
    
       >>>   - Decomposition   :  total percentage
    	     distances     :  22.96 %
    	     angles        :  43.37 %
    	     dihedrals     :  33.67 %
    
    --------------------------------------------------------------------------------
    <built-in method center of str object at 0x7f7ba4445240> =
    --------------------------------------------------------------------------------
    -10 Exit aRMSD
    -8  Plot aRMSD color map
    -7  Change general RMSD settings
    -6  Add/remove bond
    -4  Change plot settings
    -3  Define two substructures (structures are defined: 'False')
    -2  Change weighting function
    -1  Perform Kabsch alignment (required for all functions)
    --------------------------------------------------------------------------------
        Current weighting function  : 'none'
        Calculate mcc contribution  : 'False'
        Kabsch alignment performed  : 'True'
    --------------------------------------------------------------------------------
    0   ... visualize results in aRMSD representation
    1   ... visualize structural superposition
    2   ... perform statistic investigation of bond lengths and angles
    3   ... show RMSD results
    4   ... interpolate between the structures (cart., 10 steps)
    5   ... generate outfile
    20  ... export structural data
    --------------------------------------------------------------------------------
    
    >>  Enter your choice: 5
    
    > A logfile (aRMSD_logfile.out) has been written successfully!
    
    --------------------------------------------------------------------------------
    <built-in method center of str object at 0x7f7ba4445240> =
    --------------------------------------------------------------------------------
    -10 Exit aRMSD
    -8  Plot aRMSD color map
    -7  Change general RMSD settings
    -6  Add/remove bond
    -4  Change plot settings
    -3  Define two substructures (structures are defined: 'False')
    -2  Change weighting function
    -1  Perform Kabsch alignment (required for all functions)
    --------------------------------------------------------------------------------
        Current weighting function  : 'none'
        Calculate mcc contribution  : 'False'
        Kabsch alignment performed  : 'True'
    --------------------------------------------------------------------------------
    0   ... visualize results in aRMSD representation
    1   ... visualize structural superposition
    2   ... perform statistic investigation of bond lengths and angles
    3   ... show RMSD results
    4   ... interpolate between the structures (cart., 10 steps)
    5   ... generate outfile
    20  ... export structural data
    --------------------------------------------------------------------------------
    
    >>  Enter your choice: -10
    
    --------------------------------------------------------------------------------
    ========================== Normal program termination ==========================
    --------------------------------------------------------------------------------


# Footnotes

<sup><a id="fn.1" href="#fnr.1">1</a></sup> Model `M1.xyz` and `M1.pdb` are derivated from entry
`FEHGAB`, while `M2.xyz` and `M2.pdb` are derivated from entry
`IVUYEE` of the Cambridge Crystallographic Data Base.  The *primary*
references for the model data are: `FEHGAB` / basis for model
`M1.xyz`: "Five-coordinate nickel(II) complexes with carboxylate
anions and derivatives of 1,5,9-triazacyclododec-1-ene: structural and
1H NMR spectroscopic studies" by M. D. Santana, A. A. Lozano,
G. Garcia, G. Lopez, J. Perez, *Dalton Transactions*, 2005, 104&#x2013;109
(doi: 10.1039/B413547D).  And for `IVUYEE`, basis for model `M2.xyz`:
"Synthesis, structural characterization and biological studies of
novel mixed ligand Ag(I) complexes with triphenylphosphine and aspirin
or salicylic acid" by M. Poyraz, C. N. Banti, N. Kourkoumelis,
V. Dokorou, M. J. Manos, M. Simčič, S. Golič-Grdadolnik,
T. Mavromoustakos, A. D. Giannoulis, I. I. Verginadis,
K. Charalabopoulos, S. K. Hadjikakou, *Inorganica Chimica Acta*, 2011,
*375*, 114&#x2013;121 (doi: 10.5517/ccv2f3f).

<sup><a id="fn.2" href="#fnr.2">2</a></sup> Dolomanov, O. V.; Bourhis, L. J.; Gildea, R. J.; Howard,
J. A. K.; Puschmann, H., OLEX2: A complete structure solution,
refinement and analysis program (2009). *J. Appl. Cryst.*, 42, 339&#x2013;341.
Olex2, version 1.2.10.

<sup><a id="fn.3" href="#fnr.3">3</a></sup> To account for the different data quality is right one
motivation of `aRMSD` to load module `incertainties`, on one hand, and
to access the standard derivations of the atom coordinates provided in
the structure data (e.g., `*.cif`), on the other.

<sup><a id="fn.4" href="#fnr.4">4</a></sup> Open Babel, <http://openbabel.org/wiki/Main_Page>.  For
further details, see by O'Boyle, N. M.; Banck, M.; James, C. A.;
Morley, C.; Vandermeersch, T.; Hutchison, G. R.  Open Babel: An open
chemical toolbox. *J. Cheminf.* 2011, 3:33 (doi: 10.1186/1758-2946-3-33).
