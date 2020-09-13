import setuptools

with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

requirements = [
    'pickle'
]
    
setuptools.setup(
    name="germaNLG",
    version="0.0.1",
    author="Joe Breuer",
    author_email="joe.breuer@gmx.de",
    description="A python NLG realizer for German",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JBreuerPY/germaNLG",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: German",
        "Topic :: NLG Software",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
    include_package_data=True,
    package_data={'': ['data/*.zip']},
    python_requires='>=3.6',
)