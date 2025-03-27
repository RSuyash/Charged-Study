import os
import glob
import yaml
from datetime import datetime

# YAML frontmatter to add
default_frontmatter = """---
connections:
  - Primary Metabolites: "Key differences in function, production, etc."
  - Pharmaceutical Biotechnology: "Significance and applications in pharmaceuticals"
  - Industrial Biotechnology: "Production and optimization in industrial settings"
  - Sources of Secondary Metabolites: "Classification based on biological sources"
  - Plant Sources of Secondary Metabolites: "Detailed list of plant-derived secondary metabolites"
  - Fungal Sources of Secondary Metabolites: "Detailed list of fungal-derived secondary metabolites"
  - Bacterial Sources of Secondary Metabolites: "Detailed list of bacterial-derived secondary metabolites"
  - Animal Sources of Secondary Metabolites: "Detailed list of animal-derived secondary metabolites"
  - Biosynthetic Pathways/Biosynthetic Pathways Overview: "Overview of how secondary metabolites are synthesized"
review_dates:
  - 2025-03-27: Initial creation
coverage: 0.0
tags:
  - concept
  - metabolite
  - classification
  - source
  - pharmaceutical_biotechnology
  - PB_Unit_I
Source: ''
Confidence: Medium
Date Accessed: null
Spaced Repetition Interval: 1
Last Reviewed Date: null
Forgetting Index: 1.0
Cognitive Load: Medium
Elaboration Level: Basic
Mnemonic Encoding: ''
---"""

def update_markdown_files(root_dir):
    md_files = glob.glob(os.path.join(root_dir, "**/*.md"), recursive=True)

    for md_file in md_files:
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Check if YAML frontmatter exists
        if content.startswith("---"):
            try:
                # Load existing frontmatter
                _, existing_frontmatter, body = content.split("---", 2)
                existing_data = yaml.safe_load(existing_frontmatter) if existing_frontmatter else {}

                # Load default frontmatter
                default_data = yaml.safe_load(default_frontmatter.split("---")[1])

                # Merge frontmatters, preserving existing values
                merged_data = default_data.copy()
                merged_data.update(existing_data)

                # Add current date to review_dates if it doesn't exist
                if "review_dates" not in existing_data:
                    now = datetime.now()
                    current_date = now.strftime("%Y-%m-%d")
                    merged_data["review_dates"] = merged_data.get("review_dates", []) + [f"{current_date}: Added by script"]

                # Write merged frontmatter back to file
                new_frontmatter = yaml.dump(merged_data, indent=2)
                new_content = f"---\n{new_frontmatter}---\n{body}"

            except Exception as e:
                print(f"Error processing {md_file}: {e}")
                continue
        else:
            # Add YAML frontmatter
            now = datetime.now()
            current_date = now.strftime("%Y-%m-%d")
            frontmatter = default_frontmatter.replace("2025-03-27: Initial creation", f"{current_date}: Initial creation")
            new_content = f"{frontmatter}\n{content}"

        with open(md_file, "w", encoding="utf-8") as f:
            f.write(new_content)

# Get the project root directory
root_dir = "."

# Update the markdown files
update_markdown_files(root_dir)