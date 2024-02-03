# This file create a simple file
import os # Operative System module

def createFile(path, extension,content):
    fileName = f"index{extension}"
    file_path = os.path.join(path,fileName)

    with open(file_path,'w') as newFile :
        newFile.write(content)
        newFile.close()

    print(f"File {fileName} created in {path}")