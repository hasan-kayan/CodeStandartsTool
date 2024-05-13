# check each file and each variable if its not used remove it
#
# Path: code-style-checker/variable_cehcker.py
 def variable_checker(language: str) -> List[Dict[str, str]]:
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
             if file.endswith(data['variablerules']['extension']):
                 result.append({'file': file, 'status': 'pass'})
             else:
                 result.append({'file': file, 'status': 'fail'})
     return result
# Path: code-style-checker/function_checker.py 
