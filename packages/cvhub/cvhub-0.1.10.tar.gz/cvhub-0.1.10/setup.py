import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cvhub",
    version="0.1.10",

    author="cvdnn",
    author_email="cvvdnn@gmail.com",

    keywords=("pip", "license"),
    description="A python util package",
    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/ThreeParty/U-2-Net.git",
    project_urls={
        "Bug Tracker": "https://github.com/ThreeParty/U-2-Net.git/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),

    python_requires=">=3.6",
)
