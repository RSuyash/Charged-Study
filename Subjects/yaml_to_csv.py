import os
import yaml
import csv

def create_yaml_csv(directory, csv_filename="yaml_database.csv"):
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
                yaml_data = yaml.safe_load(yaml_block)
                data[filename] = yaml_data
                all_properties.update(yaml_data.keys())
            else:
                data[filename] = {}
                print(f"Warning: {filename} is missing YAML frontmatter: {filename}")
        except Exception as e:
            print(f"Error: Could not parse YAML in {filename}: {e}")
            data[filename] = {}

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

if __name__ == "__main__":
    directory = "KnowledgeBase/Pharmaceutical_Biotechnology/Unit_II/"
    create_yaml_csv(directory)