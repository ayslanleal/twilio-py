from setuptools import setup, find_packages


def read(filenames):
    return [
        req.strip()
        for req in open(filenames).readlines()
    ]


setup(
    name="pytwilio",
    version="0.1.0",
    description="Aplication using twillo requests",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read("requirements.txt")
)
