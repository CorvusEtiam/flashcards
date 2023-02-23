from setuptools import setup, find_packages

setup(
    name="fiszki",
    version="1.0.0",
    packages=find_packages("src"),
    package_dir={"":"src"}
)