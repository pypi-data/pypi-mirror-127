# coding=utf-8
""" Setup file for the entire project """
import os
import setuptools
from pathlib import Path

SRC_PATH = Path(os.path.dirname(os.path.realpath(__file__))).resolve()

with open(SRC_PATH / "README.md", "r", encoding='utf-8') as file:
    long_description = file.read()

with open(SRC_PATH / "requirements.txt", encoding='utf-8') as file:
    requirements = file.read()

setuptools.setup(
    name="parac_ext_cli",
    version="0.1.dev6",
    author="Luna Klatzer",
    author_email="luna.klatzer@gmail.com",
    maintainer="Luna Klatzer",
    maintainer_email="luna.klatzer@gmail.com",
    description="Command Line Interface Implementation for the Para-C "
                "programming language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GNU GENERAL PUBLIC LICENSE v3.0",
    url="https://github.com/Para-C/Para-C-CLI/",
    project_urls={
        "Issue-Page": "https://github.com/Luna-Klatzer/Para-C-CLI/issues/",
        "Changelog": "https://github.com/Luna-Klatzer/Para-C-CLI/releases"
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: C",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ],
    include_package_data=True,
    python_requires='>=3.8',
    install_requires=requirements
)
