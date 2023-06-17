from setuptools import setup, find_packages

with open('requirements.txt') as f:
    dependencies = f.read().splitlines()

setup(
    name='pyoffice',
    version='0.0.1',
    author='Gabriele Losi',
    author_email='gabrielelosi.work@gmail.com',
    description='A Python package for office-related tasks.',
    packages=find_packages(),
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'pyoffice = main:main',
        ],
    } 
)
