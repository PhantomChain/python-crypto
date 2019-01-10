import sys

import setuptools


requires = [
    'base58',
    'binary-helpers',
    'coincurve'
]

tests_require = [
    'flake8>=3.5.0',
    'flake8-import-order>=0.17.1',
    'flake8-print>=3.1.0',
    'flake8-quotes>=1.0.0',
    'pytest>=3.6.1',
    'pytest-cov>=2.5.1'
]

extras_require = {
    'test': tests_require,
    'dev': requires + tests_require
}

setup_requires = ['pytest-runner'] if {'pytest', 'test', 'ptr'}.intersection(sys.argv) else []

setuptools.setup(
    name='phantomchain-crypto',
    description='A simple Cryptography Implementation in Python for the PHANTOM Blockchain.',
    version='0.1.1',
    author='PhantomChain',
    author_email='info@phantom.org',
    url='https://github.com/PhantomChain/python-crypto',
    packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
    install_requires=requires,
    extras_require=extras_require,
    tests_require=tests_require,
    setup_requires=setup_requires,
)
