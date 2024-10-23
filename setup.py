from setuptools import setup, find_packages

setup(
    name="Product Category Tree",
    version="0.1.0",
    author="Constantin Dalinghaus",
    author_email="dalinghaus.constantin@gmail.com",
    description="Category classification tree for products :)",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/shopwithai/category_tree",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # List your package dependencies here
        # "somepackage>=1.0",
    ],
)
