import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-amazon-paapi5",
    version="0.1.1",
    author="Sergio Abad",
    author_email="sergio.abad@bytelix.com",
    description="Amazon Product Advertising API V5 wrapper for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sergioteula/python-amazon-paapi5",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)