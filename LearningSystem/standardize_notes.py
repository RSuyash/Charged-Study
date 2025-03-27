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

            # Fix YAML syntax errors - More general approach
            frontmatter_str = re.sub(r"\*\*(.*?):\*\*", r"\1:", frontmatter_str) # Remove ** around any key
            frontmatter_str = re.sub(r"-\s*\[\[(.*?)\]\]:\s*\"(.*?)\"", r"- '\1': \"\2\"", frontmatter_str) # Fix list keys

            # Load the frontmatter using yaml
            try:
                # Attempt to load with safe_load first
                metadata = yaml.safe_load(frontmatter_str) if frontmatter_str else {}
            except yaml.YAMLError as e:
                 print(f"YAML error in {md_file}: {e}")
                 # If safe_load fails, try to load ignoring aliases (might help with some errors)
                 try:
                     metadata = yaml.load(frontmatter_str, Loader=yaml.BaseLoader) if frontmatter_str else {}
                     print(f"Loaded {md_file} with BaseLoader after safe_load failed.")
                 except yaml.YAMLError as e2:
                     print(f"YAML error even with BaseLoader in {md_file}: {e2}")
                     continue # Skip file if both loaders fail

            if not isinstance(metadata, dict):
                # If loaded with BaseLoader, it might not be a dict, skip if so
                print(f"Invalid frontmatter structure in {md_file}: Frontmatter is not a dictionary")
                continue

            # Add missing properties with default values
            for key, value in DEFAULT_VALUES.items():
                if key not in metadata:
                    metadata[key] = value

            # Write the modified frontmatter back to the file
            # Use safe_dump for writing standard YAML
            new_frontmatter_str = yaml.safe_dump(metadata, sort_keys=False, allow_unicode=True)
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