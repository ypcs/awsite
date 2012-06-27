# -*- coding: utf-8 -*-

import os
from distutils.core import setup
#, find_packages
from version import get_git_version

def read(filename):
    f = os.path.join(os.path.dirname(__file__), filename)
    if os.path.exists(f):
        return open(f).read()

setup(name='awsite',
    version = get_git_version(),
#    version='1.0a',
    description='Tools to publish sites via Amazon Web Services, easily',
    long_description=read('README.txt'),
    author='Ville Korhonen',
    author_email='ville@xd.fi',
    url='http://ypcs.fi/code/awsite/',
    packages=['awsite'],
#    packages=find_packages(),
    package_dir={'awsite': 'src/awsite',},
    install_requires=[
        "boto >= 2.5.2",
    ],
    license='GPLv3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Utilities',    
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        ],
    entry_points={
        'console_scripts': [
            'awsite = awsite.core:main',
        ],
    },
    )
