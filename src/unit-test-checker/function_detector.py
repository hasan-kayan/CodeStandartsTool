# Find fucntions in a file

# Path: unit-test-checker/function_detector.py

import os
import sys
import re

def find_functions(file_path):
    """
    Find all the functions in a file.

    Args:
        file_path (str): The path of the file in which the functions need to be found.

    Returns:
        List[str]: A list of function names found in the file.

    """
    functions = []
    with open(file_path, 'r') as f:
        content = f.read()
        # Find all the functions in the file
        function_names = re.findall(r'def ([a-zA-Z0-9_]+)\(', content)
        functions.extend(function_names)
    return functions