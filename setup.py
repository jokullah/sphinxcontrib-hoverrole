from setuptools import find_packages, setup

long_desc = """
This package contains a Sphinx extension to embed mouse-over translations of mathematical terms from
Icelandic to English (or vice versa). It defines a role :hover:
"""

requires = ["Sphinx>=0.6", "setuptools", "coloredlogs>=15.0"]


setup(
    name="sphinxcontrib-hoverrole",
    version="2.0.6",
    description="Sphinx mouse-over translation extension",
    author="Simon Bodvarsson",
    author_email="simonb92@gmail.com",
    maintainer="Benedikt Magnusson",
    maintainer_email="bsm@hi.is",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=["sphinxcontrib"],
)
