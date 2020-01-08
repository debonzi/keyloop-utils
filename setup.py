from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

requires = []

test_requires = [
    "pytest",
    "pytest-cov",
]
ci_requires = [
    "python-coveralls",
]
dev_requires = ["black", "pre-commit", "pylint"] + test_requires

extras_require = {
    "dev": dev_requires,
    "test": test_requires,
    "ci": ci_requires,
}

setup(
    name="keyloop-utils",
    version="0.0.1",
    description="Key Loop - Authorization Server Utils.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Daniel Debonzi",
    author_email="debonzi@gmail.com",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=requires,
    extras_require=extras_require,
    url="https://github.com/debonzi/keyloop-utils",
    packages=["keyloop_utils",],
)
