#!/usr/bin/env python

from os.path import abspath, dirname, join

from setuptools import find_packages, setup


def requires(filename):
    with open(join(dirname(abspath(__file__)), filename), "r") as f:
        return [line for line in f.read().splitlines() if not line.startswith("--")]

base_requires = requires("requirements.txt")

setup(
    name="ikva_utils",
    version="0.1",
    description="TODO",
    author="TODO",
    author_email="TODO",
    packages=find_packages(),
    platforms=["Linux"],
    install_requires=base_requires,
)
