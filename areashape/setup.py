from setuptools import setup, find_packages

setup(
    name='areashape',
    version='0.1',
    packages=find_packages(),
    author='Boris Shakun',
    author_email='shakun.boris@gmail.com',
    description='Library for calculating areas of geometric shapes such as triangle and circle.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ShakunBoris/areashape',
    install_requires=[
        # List of dependencies
        'numpy',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: Commercial',
        'Operating System :: OS Independent',
    ],
)