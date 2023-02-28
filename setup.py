__author__ = 'Zinc Zhao'

import setuptools

with open('README.md') as fh:
    long_description = fh.read()

setuptools.setup(
    name='eclair_transformer',
    version='1.0',
    scripts=[],
    author='Zinc Zhao',
    author_email='zinc.zhao@emory.edu',
    description='Resume Parser for CRCs',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/emorynlp/eclair-transformer',
    packages=setuptools.find_packages(exclude=['tests*']),
    install_requires=[
        'torch>=1.12.0',
        'transformers==4.25.1',
        'datasets>=2.3.2'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    include_package_data=True
 )