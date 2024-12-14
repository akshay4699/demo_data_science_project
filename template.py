import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
project_name = "datascience"

list_of_files = {
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html"
}

for filepath in list_of_files:
    # Initialize the Path object
    filepath = Path(filepath)
    
    # Get the directory and filename
    filedir, filename = os.path.split(filepath)

    # Create directory if it does not exist
    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file: {filename}")

    # Check if file exists or is empty
    if not filepath.exists() or (filepath.exists() and filepath.stat().st_size == 0):
        with open(filepath, "w") as f:
            pass  # Create an empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists.")
