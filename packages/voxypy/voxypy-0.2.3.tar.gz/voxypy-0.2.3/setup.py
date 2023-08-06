import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="voxypy",
    version="0.2.3",
    description="Data structures for Voxel operations.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/Claytone/voxypy",
    author="Claytone",
    author_email="clayton.wells.321@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("test",)),
    include_package_data=True,
    install_requires=["numpy", "Pillow", "imageio"],
    entry_points={},
)