import os
import yaml

def check_yaml(directory):
    files = os.listdir(directory)
    missing_yaml = False

    for filename in files:
        if not filename.endswith(".md"):
            continue

        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        if not content.startswith("---"):
            print(f"Error: {filename} is missing YAML frontmatter")
            missing_yaml = True

    if missing_yaml:
        print("There are files missing YAML frontmatter")
    else:
        print("All files have YAML frontmatter")

if __name__ == "__main__":
    directory = "KnowledgeBase/Pharmaceutical_Biotechnology/Unit_II/"
    check_yaml(directory)