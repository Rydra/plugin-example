#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='plugin-example',
      version='4.1.0',
      description='A plugin example',
      url='https://github.com/Rydra/plugin-example',
      author='David Jiménez (Rydra)',
      author_email='davigetto@gmail.com',
      license='MIT',
      keywords='example',
      packages=find_packages(),
      classifiers=[
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python'
      ],
      install_requires=[
        "straight.plugin"
      ],
      include_package_data=True,
      zip_safe=False)
