from setuptools import find_packages,setup
import os

with open('requirements.txt') as f:
    requrements = f.read().splitlines()


setup(
    name = "Helper RAG",
    author = "Yasiru",
    version = "0.0.1",
    packages = find_packages(),
    install_requires = requrements
)