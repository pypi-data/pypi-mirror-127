import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="threeza",
    version="1.0.2",
    description="Lottery like mechanisms for crowd-sourcing",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/microprediction/threeza",
    author="microprediction",
    author_email="peter.cotton@microprediction.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["threeza","threeza.inclusion"],
    test_suite='pytest',
    tests_require=['pytest'],
    include_package_data=True,
    install_requires=["wheel","pathlib"],
    entry_points={
        "console_scripts": [
            "threeza=threeza.__main__:main",
        ]
    },
)
