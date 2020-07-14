from setuptools import setup, find_packages

def parse_reqs(filename):
    with open("requirements.txt") as reqs:
        reqs = reqs.read().strip().split("\n")
    return reqs

setup(
    name="{{cookiecutter.project_name}}",
    version="0.0.1",
    description="{{cookiecutter.project_description}}",
    python_requires=">={{cookiecutter.python_version}}",
    packages=find_packages(),
    install_requires=parse_reqs("requirements.txt"),
    extras_require={
        "dev": parse_reqs("requirements.dev.txt")
    }
)