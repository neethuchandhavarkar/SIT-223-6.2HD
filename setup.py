from setuptools import setup, find_packages

setup(
    name='my-python-app',
    version='1.0',
    packages=find_packages(),  # Automatically find packages
    install_requires=['flask'],
    author='Neethu',
    author_email='neethuchandhavarkar2003@gmail.com',
    description='A simple Flask application'
)
