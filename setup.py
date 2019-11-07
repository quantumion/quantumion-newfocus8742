#!/usr/bin/env python3

from setuptools import setup
from setuptools import find_packages


setup(
    name="newfocus8742",
    version="0.2",
    description="Driver for New Focus/Newport 8742 four channel open loop "
                "piezo motor controller",
    long_description=open("README.rst").read(),
    author="Robert Jördens",
    author_email="rj@quartiq.de",
    url="https://github.com/quartiq/newfocus8742",
    download_url="https://github.com/quartiq/newfocus8742",
    packages=find_packages(),
    install_requires=["sipyco"],
    entry_points={
        "console_scripts": [
            "aqctl_newfocus8742 = newfocus8742.aqctl_newfocus8742:main",
        ],
    },
    test_suite="newfocus8742.test",
    license="LGPLv3+",
)
