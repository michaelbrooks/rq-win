import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="rq-win",
    version="0.3.13",
    author="Michael Brooks",
    author_email="mjbrooks@uw.edu",
    description=("RQ Worker class that works for development on Windows"),
    license="MIT",
    keywords="rq queue windows",
    url="https://github.com/michaelbrooks/rq-win",
    packages=['rq_win'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        ],
    install_requires=[
        "rq>1.2.0", "times"
    ]
)
