from setuptools import setup, find_packages
from os import path

with open(path.join('README.md'), encoding='utf-8') as f:
    long_description = f.read()

def parse_requirements(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines if line.strip() and not line.startswith('#')]

install_requirements = parse_requirements("requirements.txt")


setup(
    name = "pywalletscan",
    version = "0.0.8",
    url = "https://github.com/efssisbdyy/pywalletscan",
    description = "A Python Wrapper Implementation of Etherscan",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    license = "MIT",
    keywords = "ETH, Etherium, Bitcoin, wallet, Etherscan",
    packages = find_packages(exclude=["tests"]),
    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    install_requirements=install_requirements
)