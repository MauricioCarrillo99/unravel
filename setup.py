from setuptools import setup

setup(
    name="unravel",
    url="https://github.com/maxelOA/unravel.git",
    author="Mauricio Carrillo",
    author_email="mauricio.carrillo99@outlook.com",
    packages=['unravel'],
    install_requires=["numpy >=1.21.6","pandas >= 1.3.5","requests >=2.25.1"],
    version="1.0",
    license="MIT",
    description="Python's Package for Unstructured Data",
    long_description=open('README.md').read()
)
