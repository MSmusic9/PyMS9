from setuptools import setup

lg = open("README.md", "r")
lf = lg.read()

setup(
name="MS9",
version="0.1.0",
description="Stupid but funny library",
long_description=lf,
long_description_content_type="text/markdown",
url="https://github.com/MSmusic9/PyMS9",
author="MS.music9",
author_email="gd.ms.kstash@gmail.com",
license="GNU General Public License v3 (GPLv3)",
packages=["MS9"],
classifiers=[
	"Programming language :: Python :: 3",
	"License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
],
zip_safe=True,
python_requires=">=3.0"
)