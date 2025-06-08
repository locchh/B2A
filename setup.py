from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="b2a",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python-based tool that translates between Braille and the alphabet",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/b2a",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'b2a = b2a.cli:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
