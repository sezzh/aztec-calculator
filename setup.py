"""."""
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

import aztec_calculator

setup(
    name='aztec_calculator',
    version=aztec_calculator.__version__,
    description='aztec calculator for hedwig proposal system.',
    url='https://github.com/sezzh/aztec-calculator',
    author='Jesus Cruz',
    author_email='hello@seribits.com',
    license='GPLv3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5'
    ],
    keywords='calculator aztec hedwig',
    packages=find_packages(exclude=['tests*'])

)
