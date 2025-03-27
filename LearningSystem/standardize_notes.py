import os
import glob
import yaml
from datetime import date
import git
import re

# Define default values for new properties
DEFAULT_VALUES = {
    "Source": "",
    "Confidence": "Medium",
    "Date Accessed": None,
    "Spaced Repetition Interval": 1,
    "Last Reviewed Date": None,
    "Forgetting Index": 1.0,
    "Cognitive Load": "Medium",
    "Elaboration Level": "Basic",
    "Mnemonic Encoding": ""
}

def standardize_notes(vault_path):
    md_files = glob.glob(os.path.join(vault_path, "**/*.md"), recursive=True)

    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Split the file into frontmatter and content
            parts = content.split('---', 2)
            if len(parts) < 3:
                print(f"No frontmatter found in {md_file}")
                continue

            frontmatter_str = parts[1].strip()
            content_str = parts[2].strip()

            # Fix YAML syntax errors
            frontmatter_str = re.sub(r"\*\*Type:\*\*", "Type:", frontmatter_str)

            # Load the frontmatter using yaml
            try:
                metadata = yaml.safe_load(frontmatter_str) if frontmatter_str else {}
            except yaml.YAMLError as e:
                print(f"YAML error in {md_file}: {e}")
                continue

            if not isinstance(metadata, dict):
                print(f"Invalid frontmatter in {md_file}: Frontmatter is not a dictionary")
                continue

            # Add missing properties with default values
            for key, value in DEFAULT_VALUES.items():
                if key not in metadata:
                    metadata[key] = value

            # Write the modified frontmatter back to the file
            new_frontmatter_str = yaml.dump(metadata, sort_keys=False)
            new_content = f"---\n{new_frontmatter_str}\n---\n{content_str}"

            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(new_content)

            print(f"Standardized properties in: {md_file}")

        except Exception as e:
            print(f"Error processing {md_file}: {e}")

def main():
    vault_path = "."  # Current working directory is the vault path
    standardize_notes(vault_path)

    # Commit and push changes
    try:
        repo = git.Repo(vault_path)
        repo.git.add(all=True)
        repo.git.commit(message="Standardized note properties")
        repo.git.push("origin", "standardize-properties")  # Assuming branch name is "standardize-properties"
        print("Changes committed and pushed to GitHub.")
    except Exception as e:
        print(f"Error committing and pushing to GitHub: {e}")

if __name__ == "__main__":
    main()