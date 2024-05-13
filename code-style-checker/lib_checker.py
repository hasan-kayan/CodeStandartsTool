# Let this part check the import if the imported library is not used in the code, remove it.

# Path: code-style-checker/lib_checker.py
# Compare this snippet from code-style-checker/file_name_checker.py:
# ## each language has its own configuration json file, and each json contains filenamerules field

def lib_checker(language: str) -> List[Dict[str, str]]:
    """
    Check the code style of files in the 'project' directory based on the rules specified in the language-specific JSON file.

    Args:
        language (str): The programming language for which the code style needs to be checked.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing the file name and its status ('pass' or 'fail') based on the code style rules.

    Raises:
        FileNotFoundError: If the language-specific JSON file is not found.

    """
    result = []
    with open(f'code-style-checker/{language}.json') as f:
        data = json.load(f)
        for file in os.listdir('project'):
            if file.endswith(data['librules']['extension']):
                result.append({'file': file, 'status': 'pass'})
            else:
                result.append({'file': file, 'status': 'fail'})
    return result