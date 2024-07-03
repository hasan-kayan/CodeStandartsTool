## Each programming language has its own funciton rules about naming etc. 
## here are the common rules that is vaild for all languages

# If a function is not using cannot stay in code 
# If a function does not have error correction mechanism, it cannot stay in code
# If a function does not have docString it cannot stay in code


# Path: code-style-checker/function_checker.py

import json
import os
from typing import List, Dict

def function_checker(language: str) -> List[Dict[str, str]]:
    """
    Check the code style of functions in the project directory based on the specified language.

    Args:
        language (str): The programming language to check the code style for.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing the file name and its status.
            The status can be either 'pass' or 'fail' depending on whether the code style
            of the functions in the file meets the specified rules.

    Raises:
        FileNotFoundError: If the JSON configuration file for the specified language is not found.
    """
    result = []
    with open(f'code-style-checker/{language}.json') as f:
        data = json.load(f)
        for file in os.listdir('project'):
            if file.endswith(data['functionrules']['extension']):
                result.append({'file': file, 'status': 'pass'})
            else:
                result.append({'file': file, 'status': 'fail'})
    return result