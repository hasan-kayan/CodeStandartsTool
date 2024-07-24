class LibraryNameChecker:
    def __init__(self, allowed_libraries):
        self.allowed_libraries = allowed_libraries

    def check_library_name(self, library_name):
        if library_name in self.allowed_libraries:
            return True
        else:
            return False

# Example usage
if __name__ == "__main__":
    allowed_libraries = ["numpy", "pandas", "requests"]
    library_name_checker = LibraryNameChecker(allowed_libraries)

    library_name = "numpy"
    if library_name_checker.check_library_name(library_name):
        print(f"Library '{library_name}' is allowed.")
    else:
        print(f"Library '{library_name}' is not allowed.")
