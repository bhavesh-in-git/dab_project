from setuptools import setup, find_packages

setup(
    name="dab_project",
    version="0.0.3",
    description="This contains the code in the ./src directory of the project",
    packages=find_packages(where="./src"),
    package_dir={"": "./src"},
    install_requires=["setuptools"],
    entry_points={
        "console_scripts": [
            "main=dab_project.main:main"
        ]
    }
)