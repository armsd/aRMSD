#!/usr/bin/ python

# File name: debcollector-aRMSD.py
# Last edit: 2018-10-23

"""
Motivation:  Collection and installation of the *.deb needed to start
aRMSD may be put into a list Python works on.

Intended use: python debcollector-aRMSD.python

for either Python2 or Python3 of Debian 9 (sid/buster).  Worked fine
on this platform.  Potentially working -- but not tested -- on
related Ubuntu 18.04 LTS, too.
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
print(" [1]    Debian based platform recquiering packages as *.deb.")
print(" [2]    Fedora based platform requiring *.rpm.\n")

# selection
platform = str(input())
if platform == str("0"):
    print("\n The script closes now.  No installation was performed.")
    sys.exit()

if platform == str("1"):
    print("\n Work now assumes you work on Debian.")
    print(" Not tested, yet possible to work for Ubuntu 18.04 LTS, too.\n")

if platform == str("2"):
    print("\n Work now assumes you work on Fedora.")
    print(" Currently, Fedora's *.rpm packages were not checked for suitability for aRMSD.")
    print(" Hence, for the moment, this will install nothing on Fedora.")
    print(" The script will close now.")
    sys.exit()


# Programs to install under Debian (ref.: Debian 9 sid/buster,
# October 2019).  This list is used as reference for later definitions
# (e.g., Fedora in the next list), too.
#
# Potentially working -- but not yet tested -- for derivates like Ubuntu 18.04 LTS.
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


# Programs to install under Fedora (reference: was the online repository,
# https://apps.fedoraproject.org/packages, visited October 2018).
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
