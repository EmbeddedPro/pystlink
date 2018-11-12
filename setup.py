import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pystlink",
    version="0.0.1",
    author="pavelrevak",
    author_email="author@example.com",
    description="Python tool for manipulating with STM32 MCUs using ST-Link in-system programmer and debugger.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pavelrevak/pystlink",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)