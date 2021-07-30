from setuptools import find_packages, setup


def parse_reqs(filename):
    with open(filename) as f:
        lines = f.readlines()
        stripped_lines = [line.strip() for line in lines]
        reqs = [line for line in stripped_lines if line and not line.startswith("#")]
    return reqs


setup(
    name="{{cookiecutter.project_name}}",
    version="0.0.1",
    description="{{cookiecutter.project_description}}",
    python_requires=">={{cookiecutter.python_version}}",
    packages=find_packages(),
    install_requires=parse_reqs("requirements.txt"),
    extras_require={"dev": parse_reqs("requirements.dev.txt")},
)
