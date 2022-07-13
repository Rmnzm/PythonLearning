1) Create the description file
README FILE

2) Create setup file
 - install setuptools
 - code {
        from setuptools import setup

        setup(
            name='vsearch',
            version='1.0',
            description='The Head First Python Search Tools',
            author='HF Python 2e',
            author_email='hfpy2e@gmail.com',
            url='headfirstlabs.com',
            py_modules=['vsearch'],
            )
 }

3) Create setup archive
From module folder command:
py -3 setup.py sdist

4) Setup package with PIP (Package Installer for Python)
From new dist folder command:
py -3 -m pip install {module name}.tar.gz


TO USE
import {your package name}