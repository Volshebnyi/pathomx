#!/usr/bin/env python
# coding=utf-8
"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""
import sys
from copy import copy
import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup, find_packages

version_string = '0.9.0'

sys.path.append('metapath')

# Defaults for py2app / cx_Freeze
default_build_options=dict(
    packages=[
#        'PyQt5', #.QtGui',
#        'PyQt5.QtCore',
#        'PyQt5.QtWebKit',
#        'PyQt5.QtNetwork',
#        'PyQt5.QtWidgets',
#        'PyQt5.QtWebKitWidgets',
#        'PyQt5.QtPrintSupport',
        'PyQt5',
#        'PySide',
        'numpy',
        'scipy',
        'nmrglue',
        'gpml2svg',
        'pydot',
        'poster.encode',
        'sklearn',
#        'fileiobase',
#        'sip',
        ],
    includes=[
        'sip',
        ],
    excludes=[
        '_xmlplus',
        'IPython',
        'test',
        'networkx',
        'wx',
        'matplotlib',
        ],
    )

build_mac = None
build_exe = None
build_py2app = None

executables = []

try:
    import py2app
except:
    pass
else:
    # py2app setup
    build_py2app = dict(
                    iconfile='metapath/static/icon.icns',
                    site_packages=True,
                    optimize=2,
                    resources=['metapath/static', 'examples', 'metapath/database', 'metapath/plugins', 'metapath/identities', 'metapath/html','metapath/icons'],
                    plist=dict(
                        CFBundleName = "MetaPath",
                        CFBundleShortVersionString = version_string, # must be in X.X.X format
                        CFBundleGetInfoString = "MetaPath %s" % version_string,
                        CFBundleExecutable = "MetaPath",
                        CFBundleIdentifier = "com.mfitzp.metapath",
                    ),
                    matplotlib_backends=['macosx'],
                )
    build_py2app.update( default_build_options )



try:
    from cx_Freeze import setup, Executable
except:
    build_exe = None
    build_mac = None
    excutables = None
else:
    # cx_Freeze setup
    base = None
    exceutables = None

    build_all = dict()

    build_all['include_files']=[
        ('metapath/static', 'static'),
        ('metapath/database', 'database'),
        ('metapath/plugins', 'plugins'),
        ('metapath/identities', 'identities'),
        ('metapath/html', 'html'),
        ('metapath/icons', 'icons'),
        ]

    build_exe = copy(build_all)
    build_mac = copy(build_all)
    
    build_mac['iconfile'] = 'metapath/static/icon.icns'
    
    base = None
    if sys.platform == "win32":
        base = "Win32GUI"
    # cx_freeze GUI applications require a different base on Windows (the default is for a
    # console application).
    executables=[Executable("metapath/metapath.py", base=base)]

    # Apply default build options to cx/py2app build targets
    build_exe.update( default_build_options )
    build_mac.update( default_build_options )
    

setup(

    name='MetaPath',
    version=version_string,
    author='Martin Fitzpatrick',
    author_email='martin.fitzpatrick@gmail.com',
    url='https://github.com/mfitzp/metapath',
    download_url='https://github.com/mfitzp/metapath/zipball/master',
    description='Metabolic pathway visualisation and analysis.',
    long_description='MetaPath is a tool for the analysis of metabolic pathway and \
        associated visualisation of experimental data. Built on the MetaCyc database it \
        provides an interactive map in which multiple pathways can be simultaneously \
        visualised. Multiple annotations from the MetaCyc database are available including \
        synonyms, associated reactions and pathways and database unification links.',

    packages = find_packages(),
    include_package_data = True,
    package_data = {
        '': ['*.txt', '*.rst', '*.md'],
    },
    exclude_package_data = { '': ['README.txt'] },

    executables = executables,

    entry_points = {
        'gui_scripts': [
            'metapath = metapath.metapath:main',
        ]
    },

    install_requires = [
#            'PySide>=1.1.1',
            'numpy>=1.5.0',
            'wheezy.template>=0.1.135',
            'gpml2svg>=0.1.0',
#            'sip',
#            'matplotlib>=1.2.1'
            ],

    keywords='bioinformatics metabolomics research analysis science',
    license='GPL',
    classifiers=['Development Status :: 4 - Beta',
               'Natural Language :: English',
               'Operating System :: OS Independent',
               'Programming Language :: Python :: 2',
               'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
               'Topic :: Scientific/Engineering :: Bio-Informatics',
               'Topic :: Education',
               'Intended Audience :: Science/Research',
               'Intended Audience :: Education',
              ],

    # cx_freeze/py2app settings for building the .app file
    options={
        "build_exe": build_exe,
        "build_mac": build_mac,
        "py2app": build_py2app
    },
    app=[ 'metapath/metapath.py' ],
    setup_requires=["py2app"],

    )