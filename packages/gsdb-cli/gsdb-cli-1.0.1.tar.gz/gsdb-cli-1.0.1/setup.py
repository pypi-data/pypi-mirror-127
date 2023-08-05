# Copyright (c) 2014-2021 GeoSpock Ltd.

from os import path
from setuptools import setup, find_packages

here = path.dirname(__file__)

with open(path.join(here, "VERSION"), "r") as fh:
    version_number = fh.read().strip()

with open(path.join(here, "README.md"), "r") as fh:
    long_description = fh.read().strip()

setup(
    name="gsdb-cli",
    version=version_number,
    description="GeoSpock DB CLI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="GeoSpock Ltd",
    author_email="cli-development@geospock.com",
    url="http://geospock.com/",

    license="MIT",

    packages=find_packages(),
    include_package_data=True,

    # More info at https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        "Click",
        "boto3",
        "keyring",
        "requests",
        "tenacity",
        "urllib3",
        "keyrings.cryptfile"
    ],

    tests_require=[
        "requests_mock"
    ],

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.5",

    entry_points={
        "console_scripts": [
            "gsdb = geospock_cli.geospockcli:wrapped_cli",
        ],
    }
)
