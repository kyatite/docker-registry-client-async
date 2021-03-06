#!/usr/bin/env python

import os
import re

from setuptools import setup, find_packages


def find_version(*segments):
    root = os.path.abspath(os.path.dirname(__file__))
    abspath = os.path.join(root, *segments)
    with open(abspath, "r") as file:
        content = file.read()
    match = re.search(r"^__version__ = ['\"]([^'\"]+)['\"]", content, re.MULTILINE)
    if match:
        return match.group(1)
    raise RuntimeError("Unable to find version string!")


setup(
    author="Richard Davis",
    author_email="crashvb@gmail.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    description="An AIOHTTP based Python REST client for the Docker Registry.",
    extras_require={
        "dev": [
            "black",
            "pylint",
            "pytest",
            "pytest-asyncio",
            "pytest-docker-registry-fixtures",
            "twine",
            "wheel",
        ],
        "test": ["pytest-xdist"],
    },
    include_package_data=True,
    install_requires=[
        "aiodns",
        "aiofiles",
        "aiohttp",
        "canonicaljson",
        "www_authenticate",
    ],
    keywords="docker docker-sign docker-verify integrity sign signatures verify",
    license="Apache License 2.0",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    name="docker_registry_client_async",
    packages=find_packages(),
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-asyncio", "pytest-docker-registry-fixtures"],
    test_suite="tests",
    url="https://pypi.org/project/docker-registry-client-async/",
    version=find_version("docker_registry_client_async", "__init__.py"),
)
