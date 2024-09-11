from setuptools import setup

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="jc-image-processing",
    version="0.0.1",
    author="Jorge Ferreira da Costa",
    author_email="jfcosta@tjma.jus.br"
    description="Package only for learning how create packages",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url=myurl.com,
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8"
    )  