# Imports
import argparse
import os # import operative system functions

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
    # Combine path and name to get the full projevt path
    project_path = os.path.join(path, name)

    print(f"The project structure is generate in {project_path}")
    

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