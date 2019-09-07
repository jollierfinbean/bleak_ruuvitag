"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='bleak_ruuvitag',
    version='0.0.1',
    description='Asyncio library for fetching data from BE sensors using bleak',
    author='Samuli Lager',
    author_email='samuli.lager@gmail.com',
    url='https://github.com/jollierfinbean/bleak_ruuvitag'
    classifiers=[
        'Development Status :: 1 - Planning'
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='asyncio bluetooth BE ruuvitag',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires='>=3.7',
    install_requires=[
        'bleak>=0.5.0'
    ]
)
