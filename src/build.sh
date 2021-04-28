#!/bin/bash
# File: build.sh
# Script pro vytvoreni debian balicku

set -e
version="1.0.3"

# build dependency 
sudo apt-get install -y build-essential devscripts debhelper debmake dh-python python3-all python3-pip python3-pyqt5 qt5-default 

python3 setup.py sdist

cd dist && mv duck-calc-${version}.tar.gz ../ && cd ..
tar -xzmf duck-calc-${version}.tar.gz && cd duck-calc-${version}/

debmake -b":python3"

# Vytvori script, ktery se pousti po instalaci balicku
{
    echo "#!/bin/bash"
    echo "pip3 install --no-warn-script-location PyQt5==5.15.4 PyQt5-Qt5==5.15.2 PyQt5-sip==12.8.1 PySide2==5.15.2"
} >> debian/postinst


# Prepise control file 
rm debian/control

{
    echo "Source: duck-calc"
    echo "Section: python,"
    echo "Priority: optional"
    echo "Maintainer: whitelist team"
    echo "Build-Depends: debhelper (>=11~), dh-python, python3-all, python3-setuptools, qt5-default, python3-pip"
    echo "Standards-Version: 4.1.4"
    echo "Homepage: https://github.com/Honny1/ivs_calc"
    echo "X-Python3-Version: >= 3.2"
    echo ""
    echo "Package: duck-calc"
    echo "Architecture: any"
    echo "Multi-Arch: foreign"
    echo "Depends: \${misc:Depends}, \${shlibs:Depends}, qt5-default, python3-pip"
    echo "Description: auto-generated package by debmake"
    echo " This Debian binary package was auto-generated by the"
    echo " debmake(1) command provided by the debmake package."
} >> debian/control

debuild

echo "Done!"
