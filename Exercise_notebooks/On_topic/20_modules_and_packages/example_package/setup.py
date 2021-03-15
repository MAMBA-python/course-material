from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.rst')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()

version = {}
with open(os.path.join(_here, 'somepackage', 'version.py')) as f:
    exec(f.read(), version)

setup(
    name='somepackage',
    version=version['__version__'],
    description=('Show how to structure a Python project.'),
    long_description=long_description,
    author='Onno Ebbens',
    author_email='onno.ebbens@mamba-python.nl',
    license='MPL-2.0',
    packages=['somepackage'],
    install_requires=['matplotlib>=3.0','wordcloud>=1.8.1'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'],
    )
