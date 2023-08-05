import setuptools

with open( "README.md", "r" ) as fh:
    long_description = fh.read()

setuptools.setup(
    name = "bigmcl",
    version = "0.1b10",
    author = "xonq",
    author_email = "konkelzach@protonmail.com",
    description = "High throughput large scale Markov clustering (MCL) via subgraph extraction",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://gitlab.com/xonq/bigmcl",
    package_dir={"": "bigmcl"},
    packages = setuptools.find_packages( where="bigmcl" ),
    scripts = ["bigmcl/bigmcl.py"],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires = '>=3.0,<4'
)
