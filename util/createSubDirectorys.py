# This file generate a list of the subdirectorys in the project structure

import os # Module Operative System

# Function to create a list of the subdirectorys
def createSubDirectorys(project_path, subdirectories):        
     # Create the subdirectories
    for subdir in subdirectories :
        # Comdine the path project and the subdirectory
        subdir_path = os.path.join(project_path, subdir)

        # Create the subdirectory
        os.makedirs(subdir_path, exist_ok=True)

        print(f"Subdirectory '{subdir}' is created in {project_path}")