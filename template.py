import os
from pathlib import Path 
import logging

# configuring log file
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s: %(levelname)s]: %(message)s'
)

while True:
    project_name = input("Enter the Project Name : ")
    if project_name != " ":
        break
logging.info(f"Creating Project by name : {project_name}")

# list of files :
list_of_files =[
    ".github/workflows/.gitkeep", #gitkeep because repository does not take empty repo
    f"src/{project_name}/__init__.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    "init_setup.sh",#help setup envt
    "requirements.txt",
    "requirements_dev.txt", #required for testing 
    "setup.py", #help do basic setup
    "pyproject.toml",
    "setup.cfg",
    "tox.ini"# to test package in different python environment 
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating file directory {filedir} for filename : {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating a new file : {filename} at path: {filepath}")
    else:
        logging.info(f"file is already present in at : {filepath}")# to protect the file from overwriting
