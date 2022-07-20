import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="housingpricera",
    version="0.2.2",
    author="Radhika Agarwal",
    author_email="radhika.agarwal@tigeranalytics.com",
    description="Package for assignment 2.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/agarwalradhika20/mle-training",
    project_urls={
        "Bug Tracker": "https://github.com/agarwalradhika20/mle-training/issues",
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