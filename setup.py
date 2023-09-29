"""Python client for an easy interaction with the WikiJS graphql API"""

import sys
import setuptools


__py_version__: tuple[int, ...] = (3, 10)
__py_version_str__: str = '.'.join(map(str, __py_version__))

# Python version check
if sys.version_info < __py_version__:
    raise ValueError(f"This package requires Python {__py_version_str__} or newer")


# Package metadata
__project__ = "wikijs-pyclient"
__version__ = "1.0.0"
__license__ = "MIT License"
__name__ = "Lovesh Kumrawat"
__email__ = "kumrawat.lovesh@gmail.com"
__url__ = "https://github.com/lovesh-kumrawat/wikijs-pyclient"
__download_url__ = "https://pypi.org/project/wikijs-pyclient"
__platforms__ = "ALL"

__classifiers__ = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    f'License :: OSI Approved :: {__license__}',
    'Operating System :: OS Independent',
    f"Programming Language :: Python :: {__py_version_str__}",
    'Topic :: Software Development'
]

__keywords__ = [
    "wikijs-client",
    "wikijs-python-client",
    "wikijs-api-wrapper",
    "wikijs-graphql-api",
    "wikijs-graphql-api-automation",
]

with open("README.md", "r") as fh:
    __long_description__ = fh.read()
    __long_description_content_type__ = "text/markdown"


setuptools.setup(
    name                          = __project__,
    version                       = __version__,
    description                   = __doc__,
    long_description              = __long_description__,
    long_description_content_type = __long_description_content_type__,
    author                        = __name__,
    author_email                  = __email__,
    maintainer                    = __name__,
    maintainer_email              = __email__,
    license                       = __license__,
    platforms                     = __platforms__,
    url                           = __url__,
    download_url                  = __download_url__,
    classifiers                   = __classifiers__,
    keywords                      = __keywords__,
    packages                      = setuptools.find_packages(),
    python_requires               = f">={__py_version_str__}",
)
