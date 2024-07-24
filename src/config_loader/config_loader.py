import json

class ConfigLoader:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self):
        try:
            with open(self.config_path, 'r') as config_file:
                config = json.load(config_file)
                return config
        except FileNotFoundError:
            print(f"Error: Config file '{self.config_path}' not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error: Config file '{self.config_path}' contains invalid JSON.")
            return None

    def get_naming_conventions(self):
        return self.config.get("naming_conventions", {})

    def should_check_unused_variables(self):
        return self.config.get("check_unused_variables", False)

    def should_check_unused_libraries(self):
        return self.config.get("check_unused_libraries", False)

    def get_allowed_libraries(self):
        return self.config.get("allowed_libraries", [])

# Example usage
if __name__ == "__main__":
    config_loader = ConfigLoader('Cst.config')
    print("Naming Conventions:", config_loader.get_naming_conventions())
    print("Check Unused Variables:", config_loader.should_check_unused_variables())
    print("Check Unused Libraries:", config_loader.should_check_unused_libraries())
    print("Allowed Libraries:", config_loader.get_allowed_libraries())
