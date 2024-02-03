# Imports
import argparse
import os # import operative system functions
from util.createFile import createFile 

# My utils
from util.isValidDirectory import isValidDirectory 
from util.createSubDirectorys import createSubDirectorys

# Templates files
from util.template import CSS_TEMPLATE, HTML_TEMPLATE, JS_TEMPLATE 

# Options Program
parser = argparse.ArgumentParser(
    prog= "GW",
    description="Structure Builder for Web Projects",
    epilog="For more information, visit the Github"
)

# Add arguments
parser.add_argument('-sw','--simpleWeb', help="Generate the structure of a simple web project",action='store_true')
parser.add_argument('-p', '--path', help="Specify the path to create the project structure")
parser.add_argument('-n', '--name', help="Specify the name of the project")

# Function
def createASimpleProjectStructre(path, name):   
    # Verify if the path exist
    if isValidDirectory(path):
        # Combine path and name to get the full project path
        project_path = os.path.join(path, name)

        # Create the main directory of the project
        os.makedirs(project_path, exist_ok=True)

        # TODO: Create a index file with file in util

        # List of the sundirectories
        subdirectories = ['assets','assets/img','assets/video', 'assets/icons','assets/fonts','css', 'js']

        createSubDirectorys(project_path, subdirectories)

        createFile(project_path, ".html", HTML_TEMPLATE)
        createFile(os.path.join(project_path,subdirectories[5]),".css",CSS_TEMPLATE)
        createFile(os.path.join(project_path,subdirectories[6]),".js",JS_TEMPLATE)
    
        print(f"The project structure is generate in {project_path}")
    else :
        print(f"Error: {path} is not a valid directory")
    

# Run the mini CLI
if __name__ == '__main__':
    # Parser args
    args = parser.parse_args()

    # Cases
    if args.simpleWeb:
        # Check if both path and name are provided
        if args.path and args.name : 
            createASimpleProjectStructre(args.path, args.name)
        else :
            print("Both path and name are required for creating a project.")
    else :
        print("Wrong way!")