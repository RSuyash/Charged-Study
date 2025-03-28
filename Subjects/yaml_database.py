import os
import yaml
from prettytable import PrettyTable

def create_yaml_database(directory):
    files = os.listdir(directory)
    data = {}
    all_properties = set()

    for filename in files:
        if not filename.endswith(".md"):
            continue

        filepath = os.path.join(directory, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            if content.startswith("---"):
                yaml_block = content.split("---")[1]
                try:
                    yaml_data = yaml.safe_load(yaml_block)
                    data[filename] = yaml_data
                    all_properties.update(yaml_data.keys())
                except:
                    print(f"Warning: Could not parse YAML in {filename}")
            else:
                data[filename] = {}
                print(f"Warning: {filename} is missing YAML frontmatter")
        except Exception as e:
            print(f"Error: Could not open {filename}: {e}")
            data[filename] = {}

    # Create table
    table = PrettyTable()
    table.field_names = ["Filename"] + list(all_properties)
    table.align["Filename"] = "l"

    for filename in files:
        if not filename.endswith(".md"):
            continue
        row = [filename]
        for prop in all_properties:
            value = data.get(filename, {}).get(prop, "")
            row.append(value)
        table.add_row(row)

    print(table)

if __name__ == "__main__":
    directory = "KnowledgeBase/Pharmaceutical_Biotechnology/Unit_II/"
    create_yaml_database(directory)