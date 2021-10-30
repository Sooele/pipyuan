import setuptools
import os
import sys

def read(rel_path: str) -> str:
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, rel_path)) as fp:
        return fp.read()


def get_version(rel_path: str) -> str:
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            # __version__ = "0.9"
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")

long_description = read("README.md")


setuptools.setup(
    name="pipyuan",
    version=get_version("src/pipyuan/__init__.py"),

    author="find456789",
    # author_email="author@example.com",
    description="pipyuan 内置了国内常用的 pip 源， 你可以快速设置想要的源",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/find456789/pipyuan",
    project_urls={
        "Bug Tracker": "https://github.com/find456789/pipyuan/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    # py_modules=["sys","textwrap","argparse","subprocess","gettext"],

    entry_points={
        'console_scripts': [
            'pipyuan=pipyuan.main:main',
        ],
    },
    python_requires=">=3.6",

)


