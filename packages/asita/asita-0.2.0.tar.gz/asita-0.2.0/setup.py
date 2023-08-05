from setuptools import setup

setup(
    name = "asita",
    version = "0.2.0",
    author = "Mattéo Gaillard",
    description = "A web application framework",
    long_description = open("README.md", "r").read(),
    long_description_content_type = "text/markdown",
    url = "https://github.com/Matteo0810/Asia",
    packages = [
        "asita",
        "asita.handlers",
        "asita.utils"
    ],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.9',
)