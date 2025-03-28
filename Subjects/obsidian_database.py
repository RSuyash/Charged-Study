import os
import yaml
import csv

def create_obsidian_database(directory, csv_filename="obsidian_database.csv", js_filename="obsidian_database.js"):
    data = {}
    all_properties = set()

    def extract_yaml(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            if content.startswith("---"):
                yaml_block = content.split("---")[1]
                yaml_data = yaml.safe_load(yaml_block)
                return yaml_data
            else:
                print(f"Warning: {filepath} is missing YAML frontmatter")
                return {}
        except Exception as e:
            print(f"Error: Could not parse YAML in {filepath}: {e}")
            return {}

    def process_directory(dirpath):
        for filename in os.listdir(dirpath):
            filepath = os.path.join(dirpath, filename)
            if os.path.isdir(filepath):
                process_directory(filepath)
            elif filename.endswith(".md"):
                yaml_data = extract_yaml(filepath)
                data[filepath] = yaml_data
                all_properties.update(yaml_data.keys())

    process_directory(directory)

    # Write to CSV
    with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["Filename"] + list(all_properties)
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for filename, yaml_data in data.items():
            row = {"Filename": filename}
            for prop in all_properties:
                row[prop] = yaml_data.get(prop, "")
            writer.writerow(row)

    print(f"YAML data written to {csv_filename}")

    # Create Javascript for Dataview
    js_content = f"""
    ```dataview
    TABLE
    {",".join(all_properties)}
    FROM ""
    WHERE file.name != this.file.name
    ```
    """

    with open(js_filename, "w", encoding="utf-8") as jsfile:
        jsfile.write(js_content)

    print(f"Dataview Javascript written to {js_filename}")


if __name__ == "__main__":
    directory = "."
    create_obsidian_database(directory)