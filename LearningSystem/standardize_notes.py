import os
import glob
import frontmatter
from datetime import date
import git

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
                post = frontmatter.load(f)

            # Add missing properties with default values
            for key, value in DEFAULT_VALUES.items():
                if key not in post.metadata:
                    post.metadata[key] = value

            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(frontmatter.dumps(post))

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