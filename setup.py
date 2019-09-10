from setuptools import setup, find_packages

# read the contents of your README file
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="otf2ttf",
    version="0.2",
    packages=find_packages("src/"),
    package_dir={"": "src"},
    package_data={},
    include_package_data=True,
    entry_points={"console_scripts": ["otf2ttf=otf2ttf:main"]},
    install_requires=["fonttools", "cu2qu"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Awesome Toolbox",
    author_email="info@awesometoolbox.com",
    description="command-line tool for converting OTF to TTF",
    license="MIT",
    keywords="font convert otf ttf",
    url="https://github.com/awesometoolbox/otf2ttf",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Text Processing :: Fonts",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
    ],
)
