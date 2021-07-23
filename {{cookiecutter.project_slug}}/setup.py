from setuptools import setup, find_packages

def parse_reqs(filename):
    with open(filename) as f:
        lines = f.readlines()
        no_space = [l.strip() for l in lines]
        reqs = [r for r in no_space if r and not r.startswith("#")]
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