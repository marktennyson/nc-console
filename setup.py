from nc_console import __version__ as version
from nc_console import __author__ as author

from setuptools import setup,find_packages


with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="nc-console",
    version=version,
    url="https://github.com/marktennyson/nc-console",
    license="GPL",
    author=author,
    author_email="aniketsarkar@yahoo.com",
    description="The programmatic consoler.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["console", "input", "logger", "click", "print", "log", "logging"],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms="any",
    install_requires=[ 
       "click==8.0.0" 
    ],
    extras_require={},
    python_requires=">=3.6,<4",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)