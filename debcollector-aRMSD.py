#!/usr/bin/ python

# File name: debcollector-aRMSD.py
# Last edit: 2018-11-28

"""
Motivation:  Collection and installation of the *.deb needed to start
aRMSD may be put into a list Python works on.

Intended use on the CLI with

python debcollector-aRMSD.python

in the supervised shell of Debian 9 (Sid/buster) with administrator privileges.
It equally was tested to proceed successfully on Xubuntu 18.04 LTS.  Reference
installation for Xubuntu was the default (64 bit) point release 18.04.1,
accessed in November 2018.
"""

# module calling
import subprocess as sub
import sys

platform = ""    # to account for either *.deb, or *.rpm based systems

# initial user contact
print("'debcollector-aRMSD.py' installs packages to use aRMSD.")

# what is the platform?
print("\nYou choose either")
print(" [0]    Quit the script altogether, no installation.")
print(" [1]    Debian based platform requiering packages as *.deb.")
print(" [2]    Fedora based platform requiring *.rpm.")
print("           This option is foreseen, but currently not implemented.")

# selection
platform = str(input())
if platform == str("0"):
    print("\n The script closes now.  No installation was performed.")
    sys.exit()

if platform == str("1"):
    print("\n It is assumed you either work on Debian 9 (Sid/buster),)")
    print(" or on Xubuntu 18.04 LTS (successfully tested on point release 18.04.1).")

if platform == str("2"):
    print("\n It is assumed you work on Fedora.")
    print(" Currently, Fedora's *.rpm packages were not checked for suitability for aRMSD.")
    print(" Hence, for the moment, this will install nothing on Fedora.")
    print(" The script will close now.")
    sys.exit()


# Programs to install under Debian (ref.: Debian 9 sid/buster,
# October 2018).  This list is used as reference for later definitions
# (e.g., Fedora in the next list), too.

collect_Debian = ["cython",
                  "cython3",
                  "openbabel",
                  "libopenbabel5"
                  "python-openbabel",
                  "python-matplotlib",
                  "python-matplotlib-data",
                  "python3-matplotlib",
                  "python-uncertainties",
                  "python3-uncertainties",
                  "libvtk6.3",
                  "libvtk6.3-qt",
                  "python-vtk6",
                  "libvtk7.1",
                  "libvtk7.1-qt",
                  "python3-vtk7",
                  "vtk7"]


# Programs to install under Fedora (reference: the online repository,
# https://apps.fedoraproject.org/packages).
collect_Fedora = []

# installation on Debian
if platform == str("1"):
    for item in collect_Debian:
        # CLI pattern would be:
        # sudo apt-get install pinta
        output = "sudo apt-get install " + item

        sub.call(output, shell=True)

# installation on Fedora
if platform == str("2"):
    for item in collect_Fedora:
        # CLI pattern would be
        # sudo yum install wxapt
        # (https://docs.fedoraproject.org/en-US/Fedora/14/html/Amateur_Radio_Guide/apas02.html)
        output = "sudo yum install " + item

        sub.call(output, shell=True)


# closing
print("\nScript 'debcollector-aRMSD.py' completed its tasks. Bye.")
sys.exit()
