import setuptools

from src.testproject import definitions

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="testproject-python-sdk",
    version="1.2.3",
    author="Denis Juma",
    author_email="deniskwanusu@gmail.com",
    description="Selenium and Appium powered SDK for TestProject.io",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/testproject-io/python-opensdk",
    packages=setuptools.find_packages(exclude=["tests", "tests.*", "proxy_examples", "proxy_examples.*"]),
    classifiers=[
        "Programming Language :: Python > 2.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=2.7",
    install_requires=[
        "selenium==3.141.0",
        "Appium-Python-Client==0.52",
        "decorator>=4.4.2",
        "requests>=2.24.0",
        "importlib-metadata>=1.7.0",
        "packaging>=20.4",
    ],
)
