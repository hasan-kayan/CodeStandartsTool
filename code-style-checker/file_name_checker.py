## each language has its own configuration json file, and each json contains filenamerules field 
## write a function takes the language and according to its rules check each file in the project and return the result

import json
import os
from typing import List, Dict

def file_name_checker(language: str) -> List[Dict[str, str]]:
    result = []
    with open(f'code-style-checker/{language}.json') as f:
        data = json.load(f)
        for file in os.listdir('project'):
            if file.endswith(data['filenamerules']['extension']):
                result.append({'file': file, 'status': 'pass'})
            else:
                result.append({'file': file, 'status': 'fail'})
    return result

