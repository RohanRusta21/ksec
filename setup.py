from setuptools import setup, find_packages

setup(
    name="ksec",
    version="0.1.0",
    description="A CLI tool to encrypt secrets for Kubernetes YAML files",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Rohan",
    author_email="rohanrustagi21@gmail.com",
    url="https://github.com/RohanRusta21/ksec",
    packages=find_packages(),
    install_requires=[
        "click>=8.0",
        "cryptography>=36.0",
    ],
    entry_points={
        "console_scripts": [
            "ksec=ksec.cli:cli",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
