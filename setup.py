from setuptools import find_packages,setup
from typing import List

HIPHEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return list of requirements

    '''
    requirements = []
    with open (file_path) as file_obj:
        requirements = file_obj
        requirements =[req.replace("/n","") for req in requirements]
        if HIPHEN_E_DOT in requirements:
            requirements.remove(HIPHEN_E_DOT)

    return requirements

setup(
    name="mlproject", 
    version='0.0.1',
    author='fathima',
    author_email='fathimak90@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
      )