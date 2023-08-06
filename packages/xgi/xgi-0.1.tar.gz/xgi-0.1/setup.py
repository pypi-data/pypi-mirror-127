from setuptools import setup
import sys
import xgi.metadata

__version__ = xgi.metadata.__version__

if sys.version_info < (3, 7):
    sys.exit("XGI requires Python 3.7 or later.")

name = "xgi"

packages = [
    "xgi",
    "xgi.algorithms",
    "xgi.classes",
    "xgi.generators",
    "xgi.linalg",
    "xgi.readwrite",
    "xgi.utils",
]

version = __version__

authors = xgi.metadata.__author__# "Nicholas Landry and Leo Torres"

author_email = xgi.metadata.__email__ #"nicholas.landry@colorado.edu"

url = "https://github.com/ComplexGroupInteractions/xgi"

description = "XGI is a Python library for the representation and analysis of hypergraphs."

install_requires = [
    "networkx>=2.2,<3.0",
    "numpy>=1.15.0,<2.0",
    "scipy>=1.1.0,<2.0",
    "pandas>=0.23",
]

license = xgi.metadata.__license__ #"3-Clause BSD license"

extras_require = {
    "testing": ["pytest>=4.0"],
    "tutorials": ["jupyter>=1.0"],
    "documentation": ["sphinx>=1.8.2", "sphinx-rtd-theme>=0.4.2"],
    "all": [
        "sphinx>=1.8.2",
        "sphinx-rtd-theme>=0.4.2",
        "pytest>=4.0",
        "jupyter>=1.0",
    ],
}

setup(
    name=name,
    packages=packages,
    version=version,
    author=authors,
    author_email=author_email,
    url=url,
    description=description,
    install_requires=install_requires,
    extras_require=extras_require,
)
