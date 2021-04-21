#!/usr/bin/env python3
"""duck-calc package setup
"""
from setuptools import setup

from duck_calc import __version__ as version


def get_requirements():
    return [
        "PyQt5==5.15.4",
        "PyQt5-Qt5==5.15.2",
        "PyQt5-sip==12.8.1",
        "PySide2==5.15.2",
    ]


setup(name='duck-calc',
      version=version,
      description='Easy calculator',
      license='GNU General Public Licence v3.0',
      packages=['duck_calc'],
      install_requires=get_requirements(),
      include_package_data=True,
      data_files=[
          ('share/icons', ['duck_calc/data/duck-calc.png']),
          ('share/applications', ['duck_calc/data/duck-calc.desktop'])
      ],
      entry_points={
          'console_scripts': [
              'duck-calc-easter-egg=duck_calc.main:foo_run',
              'duck-calc=duck_calc.main:run',
          ],
      },
      python_requires='>=3.6',
      )
