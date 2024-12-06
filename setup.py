from setuptools import setup
import os

VERSION = "0.0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="tractorbeam",
    version=VERSION,
    author="Wade Fletcher",
    author_email="wade@tractorbeam.ai",
    description="Python bindings for Tractorbeam API",
    url="https://github.com/tractorbeamai/tractorbeam-python",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    project_urls={
        "Bug Tracker": "https://github.com/tractorbeamai/tractorbeam-python/issues",
        "Documentation": "https://docs.tractorbeam.ai",
        "Source Code": "https://github.com/tractorbeamai/tractorbeam-python",
    },
    python_requires=">=3.7",
    keywords="knowledge graph, llm, retrieval, information retrieval, graph database",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
