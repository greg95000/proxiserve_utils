import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="proxiserve_utils", # Replace with your own username
    version="0.0.1",
    author="greg95000",
    author_email="greg95000@gmail.com",
    description="The proxiserve access data utils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/greg95000/proxiserve_utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.6',
    install_requires= [
        "sqlalchemy",
        "sqlalchemy-utils"
    ]
)