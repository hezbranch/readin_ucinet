import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="readin_ucinet",
    version="1.3.4",
    author="Hezekiah Branch",
    author_email="hezekiah.branch.tufts@gmail.com",
    description="Read in UCINET file as pandas DF",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hezbranch/readin_ucinet",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)
