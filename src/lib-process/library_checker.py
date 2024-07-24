import ast

class LibraryUsageChecker:
    def __init__(self, code):
        self.code = code
        self.imported_libraries = self.get_imported_libraries()
        self.used_libraries = self.get_used_libraries()

    def get_imported_libraries(self):
        imported_libraries = set()
        tree = ast.parse(self.code)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imported_libraries.add(alias.name)
            elif isinstance(node, ast.ImportFrom):
                imported_libraries.add(node.module)
        return imported_libraries

    def get_used_libraries(self):
        used_libraries = set()
        tree = ast.parse(self.code)
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Attribute):
                    used_libraries.add(node.func.value.id)
                elif isinstance(node.func, ast.Name):
                    used_libraries.add(node.func.id)
        return used_libraries

    def check_unused_libraries(self):
        unused_libraries = self.imported_libraries - self.used_libraries
        return unused_libraries

# Example usage
if __name__ == "__main__":
    code = """
import numpy as np
import pandas as pd
import requests

data = np.array([1, 2, 3])
print(data)
"""

    library_usage_checker = LibraryUsageChecker(code)
    unused_libraries = library_usage_checker.check_unused_libraries()

    if unused_libraries:
        print(f"Unused Libraries: {unused_libraries}")
    else:
        print("No unused libraries found.")
