import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smart_home_pkg_ngonimombeshora",  # Replace with your own username
    version="0.0.1",
    author="Ngoni Mombeshora",
    author_email="nmombeshora3@gmail.com",
    description="A smart home hub API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # chaange to github link after creating repo on github
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
