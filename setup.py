from setuptools import setup, find_packages

setup(
    name="otf2ttf",
    version='0.1',
    packages=find_packages("src/"),
    package_dir={
        '': 'src'
    },
    package_data={
    },
    include_package_data=True,
    entry_points={
        "console_scripts": [
            'otf2ttf=otf2ttf:main',
        ],
    },
    install_requires=[
        "fonttools",
        "cu2qu",
    ]
)
