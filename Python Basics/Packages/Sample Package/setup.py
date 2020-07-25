import setuptools

setuptools.setup(
    name="PythonBasicsPackage",
    version="1.0.0",
    author="Me",
    author_email="jamesheathradford@gmail.com",
    description="Python Basics Package",
    long_description="A sample package to demonstrate how pip installs user packages",
    long_description_content_type="text/markdown",
    url="https://github.com/JamesFHeath/jamesfheathblog_code/tree/master/Python%20Basics",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)