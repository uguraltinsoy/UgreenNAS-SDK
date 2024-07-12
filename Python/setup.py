from setuptools import setup, find_packages

setup (
    name="UgreenNAS",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "pycryptodome"
    ],
    author="Ugur Altinsoy",
    description="UGREEN NAS Simple Python SDK",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown"
)