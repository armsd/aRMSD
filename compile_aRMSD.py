"""
Script for an easy installation/compilation of aRMSD from command line
(c) 2016 by Arne Wagner
"""

# Authors: Arne Wagner
# License: MIT

from __future__ import print_function
from distutils.sysconfig import get_python_lib
import os
import sys
import shutil
import subprocess
import shlex
from codecs import open
import time

inst_version = '1.1'  # Version of the installer

# This is the command which calls PyInstaller (should work on every system)
pyinstaller_cmd = 'pyinstaller --onefile aRMSD.spec'


def analyze_arguments(arguments):
    """ Checks given arguments and passes correct ones to the compilation script """

    accepted_arg_prefix = ['--use_cython', '--cython_compiler']

    def _split(arg):

        pos = arg.find('=')
        prefix = arg[:pos]
        suffix = arg[pos+1:]

        return (None, None) if prefix not in accepted_arg_prefix else (prefix, suffix)

    # Default compiler arguments
    use_cython = False
    cython_compiler = 'msvc'

    if len(arguments) != 0:  # Arguments given

        for entry in arguments:

            data = _split(entry)

            if data[0] == '--use_cython':

                use_cython = data[1]

            elif data[0] == '--cython_compiler':

                cython_compiler = data[1]

    return use_cython, cython_compiler


def check_for_ext(pyx_file_path, ext, default):
    """ Checks if a .pyx/.pyd file exists and returns the extension """

    return ext if os.path.isfile(pyx_file_path+ext) else default


def check_for_pyd_so(file_path):
    """ Checks if a file with .pyd or .so extension exists """

    return True if os.path.isfile(file_path+'.pyd') or os.path.isfile(file_path+'.so') else False


def get_current_version(armsd_dir):
    """ Returns the name of the executable (this part is copied from the spec file) """

    # Determine the version of aRMSD and append it to the file name
    contents = open(armsd_dir+'\\aRMSD.py').readlines()

    for index, line in enumerate(contents):

        if '__aRMSD_version__' in line and len(line.split()) == 3:

            version = eval(line.split()[-1])

    # Setup platform and program name
    platform, name = '', 'aRMSD'

    # Determine platform and architecture
    # First: Operating system
    if sys.platform == 'win32':

        platform = 'Win'

    elif sys.platform == 'darwin':

        platform = 'Mac'

    elif sys.platform == 'linux2':

        platform = 'Lin'

    else:

        platform = 'Os'

    # Second: 32 or 63 bit
    if sys.maxsize > 2 ** 32:

        platform += '64'

    else:
        
        platform += '32'

    name += '_{}_{}'.format(version, platform)

    return name


def has_pyinstaller():
    """ Checks if pyinstaller is available """

    site_packages_path = get_python_lib()
    return os.path.isdir(site_packages_path+'\\pyinstaller')


def package_cython_modules(build_dir, list_of_files, cython_compiler):
    """ Compiles .pyx/.py files to .pyd/.so files inplace """

    os.chdir(build_dir)  # Change to build directory and create a new file

    setup_file = 'cythonize_modules.py'
    
    # Write temporary setup file
    with open(setup_file, 'w') as outfile:
        
        outfile.write("""
from setuptools import setup
from setuptools import Extension
from Cython.Build import cythonize

setup(name = 'acore', ext_modules = cythonize('"""+list_of_files[0]+"""'),)
setup(name = 'aplot', ext_modules = cythonize('"""+list_of_files[1]+"""'),)
setup(name = 'alog', ext_modules = cythonize('"""+list_of_files[2]+"""'),)
""")

    t0 = time.clock()  # Start time

    # Cythonize modules and compile them to .pyd/.so libraries
    subprocess.call(r'python {setup} build_ext --inplace --compiler={cython_compiler}'.format(setup=setup_file,
                                                                                              cython_compiler=cython_compiler))
    t1 = time.clock()  # End time

    print('\n>> Modules were successfully compiled by Cython!')
    print('Compilation time: '+str(round((t1 - t0) / 60.0, 1))+' min')


def run_compilation(use_cython, cython_compiler):
    """ Runs the pyinstaller compilation with the given flags for cython and the c compiler """

    print('\n*** This the official installer for aRMSD (Installer version: '+inst_version+') ***')
    print('==============================================================================')
    print('It will create a standalone executable using PyInstaller.')
    print('\nNote: The compilation process will take some time (see below),')
    print('      open/close additional windows and create temporary files.')

    if not use_cython:  # Estimates the compilation time based on tests - but may be different on other machines

        print('\n\t -- Estimated total compilation time: 25 min --')

    else:

        print('\n\t --Estimated total compilation time: 28 min --')

    print('------------------------------------------------------------------------------')
    print('Info: You can customize the build by adjusting the')
    print('      aRMSD.spec and compile_aRMSD.py files')
    print('------------------------------------------------------------------------------')

    has_pyinst = has_pyinstaller()

    if has_pyinst:

        # Names of the build folder and the core modules (without extensions)
        build_folder_name = 'build'
        name_core, name_log, name_plot = 'acore', 'alog', 'aplot'

        basic_dir = os.getcwd()  # Determine the initial working directory
        armsd_dir = basic_dir+'\\armsd'  # aRMSD folder in the working directory
        build_dir = basic_dir+'\\'+build_folder_name  # Build folder directory

        # Check for pre-compiled .pyd files
        comp_core = check_for_pyd_so(armsd_dir + '\\' + name_core)
        comp_plot = check_for_pyd_so(armsd_dir + '\\' + name_plot)
        comp_log = check_for_pyd_so(armsd_dir + '\\' + name_log)

        if True in [comp_core, comp_plot, comp_log]:  # If a single pre-compiled module exists, don't compile

            print('\n>> Pre-compiled modules found...')
            use_cython = False

        # Check if .pyx files of the three modules exist
        ext_core = check_for_ext(armsd_dir+'\\'+name_core, '.pyx', '.py')
        ext_plot = check_for_ext(armsd_dir+'\\'+name_plot, '.pyx', '.py')
        ext_log = check_for_ext(armsd_dir+'\\'+name_log, '.pyx', '.py')

        print('\n>> Installer was called as...')
        print('\npython compile_aRMSD.py')

        print('\n>> Creating temporary directory... '+build_folder_name)

        os.makedirs(build_folder_name)  # Make temporary build directory

        os.chdir(build_folder_name)  # Change to build folder

        # Copy core files to build directory
        shutil.copyfile(armsd_dir+'\\'+name_core+ext_core, build_dir+'\\'+name_core+ext_core)
        shutil.copyfile(armsd_dir+'\\'+name_plot+ext_plot, build_dir+'\\'+name_plot+ext_plot)
        shutil.copyfile(armsd_dir+'\\'+name_log+ext_log, build_dir+'\\'+name_log+ext_log)

        print('\n>> Copying core modules...')
        print('\t... '+name_core+ext_core)
        print('\t... '+name_plot+ext_plot)
        print('\t... '+name_log+ext_log)

        if use_cython:  # Cythonize pyx files or py files

            print('\n>> Attempting to use Cython in the compilation')

            try:

                # Import required modules
                from setuptools import setup
                from setuptools import Extension
                from Cython.Build import cythonize

                print('\n>> Cython and setuptools found, starting compilation...')
                will_use_cython = True

            except ImportError:  # Something went wrong, most likely no Cython installation

                print('\n>> ERROR: Will continue without cythonization!')
                will_use_cython = False

            if will_use_cython:

                print('\npython cythonize_modules.py build_ext --inplace --compiler='+cython_compiler)

                # Combine modules in list and compile to libraries
                sourcefiles = [name_core+ext_core, name_plot+ext_plot, name_log+ext_log]
                package_cython_modules(build_dir, sourcefiles, cython_compiler)

                # Remove .pyx/.py and .c files - the program will be automatically compiled with the cythonized files
                os.remove(name_core+ext_core)
                os.remove(name_core+'.c')
                os.remove(name_plot+ext_plot)
                os.remove(name_plot+'.c')
                os.remove(name_log+ext_log)
                os.remove(name_log+'.c')

        else:

            print('\n>> INFO: Cython will not be used!')

        print('\n>> Copying main program files...')

        # Copy main file, icon and spec file to build directory
        shutil.copyfile(armsd_dir+'\\aRMSD.py', build_dir+'\\aRMSD.py')
        shutil.copyfile(basic_dir+'\\aRMSD_icon.ico', build_dir+'\\aRMSD_icon.ico')
        shutil.copyfile(basic_dir+'\\aRMSD.spec', build_dir+'\\aRMSD.spec')

        # Gets the file name of the created executable
        file_name_dir = get_current_version(armsd_dir)

        print('\n>> Calling PyInstaller...')
        print('\n'+build_dir+'> '+pyinstaller_cmd)

        t0 = time.clock()  # Start time

        # Compile files with PyInstaller
        pyinstaller_args = shlex.split(pyinstaller_cmd)
        subprocess.call(pyinstaller_args)

        t1 = time.clock()  # End time

        # Copy executable to 'armsd' folder and delete all temporary files
        os.chdir(basic_dir)
        shutil.rmtree(build_dir+'\\dist\\'+file_name_dir)
        prg_file_name = os.listdir(build_dir+'\\dist')[0]  # List file (only one should be there) in distribution directory
        shutil.copyfile(build_dir+'\\dist\\'+prg_file_name, armsd_dir+'\\'+prg_file_name)
        shutil.rmtree(build_dir)

        # Echo successful creation, print compilation time
        print('Executable -- '+prg_file_name+' -- was created successfully!')
        print('Compilation time: '+str(round((t1 - t0) / 60.0, 1))+' min')
        print('Cleaning up files and directories')

        print('\nClean up complete, executable has been moved to:\n'+armsd_dir)
        print('\n>> Compilation complete!')
        print('\n-----------------------------------------------------------------------------')
        print('In order to use the executable, copy...')
        print('settings.cfg, the xsf folder and '+prg_file_name)
        print('to any directory of your choice and start the program.')
        print('It is recommended to call aRMSD from command line')
        print('e.g. Path\\to\\exe> '+prg_file_name)
        print('to catch potential errors. The start of the program may take a few seconds!')

    else:

        print('\n>> ERROR: PyInstaller was not found, install the package and run again!')
        print('--> from command line: pip install pyinstaller')


if __name__ == '__main__':  # Run the program

    arguments = sys.argv[1:]  # Get arguments

    use_cython, cython_compiler = analyze_arguments(arguments)  # Check arguments and set variables

    run_compilation(use_cython, cython_compiler)
