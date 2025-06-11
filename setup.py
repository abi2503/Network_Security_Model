### This is a setup file for the project, it will install the necessary packages for the project and create a virtual environment.
### It will also create a .env file for the project, and a requirements.txt file for the project.


from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function will read the requirements.txt file and return a list of requirements.
    """
    try:
        requirements = []
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.replace("\n", "") for req in requirements]
            if "-e ." in requirements:
                requirements.remove("-e .")
        return requirements
    except FileNotFoundError:
        print("Requirements file not found")


setup(
    name="Network Security Project",
    version="0.0.1",
    author="Abhishek Suresh",
    author_email="as18757@nyu.edu",
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages(),
)