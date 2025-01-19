from setuptools import find_packages,setup
from typing import List

HYPHON_SYMBOL="-e ."
def get_requirements_list(file_path:str)->List:
    requirement_list=[]
    with open(file_path) as f:
        requirement_list=f.readlines()
    
    requirement_list=[req.replace("\n","") for req in requirement_list]

    if HYPHON_SYMBOL in requirement_list:
        requirement_list.remove(HYPHON_SYMBOL)

    return requirement_list

setup(
    name="ML_Project",
    version="1.0.0",
    author="Ajay Reddy",
    author_email="ajay.mareddy04@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements_list("requirements.txt")
)