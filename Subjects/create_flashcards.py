import os
import yaml

def create_flashcards(directory):
    def process_directory(dirpath):
        for filename in os.listdir(dirpath):
            filepath = os.path.join(dirpath, filename)
            if os.path.isdir(filepath):
                process_directory(filepath)
            elif filename.endswith(".md"):
                add_flashcard_properties(filepath)

    def add_flashcard_properties(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            if content.startswith("---"):
                parts = content.split("---")
                yaml_block = parts[1]
                try:
                    yaml_data = yaml.safe_load(yaml_block)
                except:
                    print(f"Could not parse YAML in {filepath}")
                    return
                if yaml_data is None:
                    yaml_data = {}

                if 'sr-interval' not in yaml_data:
                    yaml_data['sr-interval'] = 1
                if 'sr-ease' not in yaml_data:
                    yaml_data['sr-ease'] = 270

                new_yaml = yaml.dump(yaml_data, allow_unicode=True, sort_keys=False)
                new_content = f"---\n{new_yaml}---\n{parts[2]}"
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Added flashcard properties to {filepath}")
            else:
                print(f"Warning: {filepath} is missing YAML frontmatter, skipping")

        except Exception as e:
            print(f"Error processing {filepath}: {e}")

    process_directory(directory)

if __name__ == "__main__":
    directory = "."
    create_flashcards(directory)