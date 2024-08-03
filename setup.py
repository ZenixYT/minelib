from setuptools import setup, find_packages

classifiers = [
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "Operating System :: Microsoft",
    "Operating System :: MacOS",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python :: 3"
]

setup(
    name = "minelib",
    version = "a1.0.0",
    description = "A Python library to assist with creating Minecraft: Java Edition datapacks.",
    long_description=open("README.md").read(),
    url='',
    author="Anthony Schofield",
    author_email="carvekidsak@gmail.com",
    license="GPL",
    classifiers=classifiers,
    keywords='minecraft',
    packages=find_packages(),
)