"""
@Description: 
@Usage: 
@Author: liuxianglong
@Date: 2021/8/21 下午6:44
"""
# !/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='fatgoose3',
    version='V1.4.5',
    description=(
        'A general web article parser inherit from goose3'
    ),
    long_description=open('README.rst').read(),
    author='xlomg',
    author_email='liu_xianglong@live.com',
    maintainer='xlomg',
    maintainer_email='liu_xianglong@live.com',
    license='BSD License',
    packages=['fatgoose3', 'fatgoose3.extractors', 'fatgoose3.utils', 'fatgoose3.resources'],
    package_data={
        'fatgoose3': ['resources/images/*.txt', 'resources/text/*.txt']
    },
    platforms=["all"],
    url='https://github.com/xlomg/fatgoose3.git',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
        'goose3'
    ]
)