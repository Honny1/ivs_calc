"""duck-calc package setup
"""
from setuptools import find_packages, setup

import duck_calc

setup(name='duck-calc',
      version=duck_calc.__version__,
      description='Easy calculator',
      license='GNU General Public Licence v3.0',
      packages=find_packages(),
      install_requires=[],
      include_package_data=True,
      entry_points={
          'console_scripts': [
              'duck-calc=duck_calc.main:foo_run',
          ],
      },
      python_requires='>=3.6',
      )
