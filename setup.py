from io import open as io_open
from setuptools import setup, find_packages

# read module requirements from requirements.txt instead of repeating th edependencies here:
with open("requirements.txt") as f:
    requirements = f.read().splitlines()
    install_requires = [r for r in requirements if not r == ""]

setup(
        name="moviedb_analyzer",
        version="0.1",
        description="Pandas analyzer for moviedb files",
        long_description=io_open("README.md", encoding="utf-8").read(),
        package_dir={"": "src"},
        packages=find_packages("src"),
        install_requires=install_requires
)
