#!/usr/bin/env python
req =['nose','numpy','matplotlib','seaborn']
# %%    
from setuptools import setup #enables develop
from numpy.distutils.core import setup,Extension
#%% install
setup(name='tincanradar',
      version='0.1',
      packages=['tincanradar'],
	  description='Model and Build a $35 radar from coffee cans and MMICs',
	  author='Michael Hirsch, Ph.D.',
	  url='https://github.com/scivision/tincanradar',
      ext_modules=[Extension(name='pychirp',
                    sources=['comm.f90','fwdmodel.f90'],
                    f2py_options=['--quiet'])],
      install_requires=req, 
      python_requires='>=3.6',                   
	  )


