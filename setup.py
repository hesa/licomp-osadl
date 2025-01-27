# SPDX-FileCopyrightText: 2024 Henrik Sandklef
#
# SPDX-License-Identifier: GPL-3.0-or-later

import setuptools
from licomp_osadl.config import licomp_osadl_version
from licomp_osadl.config import description
from licomp_osadl.config import module_name


requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

requirements_dev = []
with open('requirements-dev.txt') as f:
    requirements_dev = f.read().splitlines()

with open("README.md") as f:
    _long_description = f.read()

setuptools.setup(
    name='licomp_osadl',
    version=licomp_osadl_version,
    author="Henrik Sanklef",
    author_email="hesa@sandklef.com",
    description=description.replace('\n', ' '),
    long_description=_long_description,
    long_description_content_type="text/markdown",
    license_files=('LICENSES/GPL-3.0-or-later.txt',),
    url="https://github.com/hesa/licomp-osadl",
    packages=['licomp_osadl'],
    entry_points={
        "console_scripts": [
            "licomp-osadl = licomp_osadl.__main__:main",
        ],
    },
    package_data={
        f'{module_name}': ['data/*.json'],
    },
    install_requires=requirements,
    extras_require={
        'dev': requirements_dev,
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Legal Industry",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Quality Assurance",
    ],
    python_requires='>=3.6',
)
