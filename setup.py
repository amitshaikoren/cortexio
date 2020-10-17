from setuptools import setup, find_packages

setup(
    name='cortexio',
    version='0.1.0',
    author='Amit-Shai Koren',
    description='Your thoughts, your feelings, your essence: now available for everyone to see.',
    packages=find_packages(),
    install_requires=['click', 'flask'],
    tests_require=['pytest', 'pytest-cov'],
)
