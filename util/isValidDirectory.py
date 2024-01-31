# This file check if the directory is valid
import os # Module Operative System

def isValidDirectory(path):
    # Check if exist the path and is valid
    return os.path.exists(path=path) and os.path.isdir(path)