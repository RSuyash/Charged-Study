---
Type: Guideline
Purpose: Example prompts for requesting different types of connections from Roo (AI
  Assistant).
Related:
- - ROO_CONNECTION_GUIDELINES
Date: 2025-03-27
Tags: null
Source: ''
Confidence: Medium
Date Accessed: null
Spaced Repetition Interval: 1
Last Reviewed Date: null
Forgetting Index: 1.0
Cognitive Load: Medium
Elaboration Level: Basic
Mnemonic Encoding: ''

---
# Prompt Examples for Creating Connections (for Roo)

This document provides examples of how to ask Roo to create different kinds of connections between notes in this Obsidian vault. Refer to [[ROO_CONNECTION_GUIDELINES]] for the underlying strategies.

## 1. Direct Inline Links (`[[Wikilinks]]`)

*   **Goal:** Link concepts directly within the text.
*   **Example Prompts:**
    *   "In the `[[Alkaloids]]` note, add an inline link to `[[Amino Acid Derived Pathways]]` where biosynthesis is mentioned."
    *   "Find the section discussing Taxol in `[[Terpenoids]]` and add an inline link to `[[Anticancer Activity]]`."
    *   "Link the mention of 'flavonoids' in `[[Phenolic Compounds]]` to a potential future note named `[[Flavonoids]]`."

## 2. Backlinks

*   **Goal:** Backlinks are created automatically when you create a `[[Wikilink]]`. You can ask Roo to *check* for existing backlinks.
*   **Example Prompts:**
    *   "Check the backlinks for the `[[Shikimic Acid Pathway]]` note. Are `[[Phenolic Compounds]]` and `[[Alkaloids]]` linking to it?"
    *   "List the notes that currently link to `[[Secondary Metabolites]]`."

## 3. Frontmatter Connections (Typed Relationships)

*   **Goal:** Add structured relationships using YAML frontmatter keys (like `connections`, `parent`, `related`, `products`, `precursors`, `type`, `status`).
*   **Example Prompts:**
    *   "Add `[[Secondary Metabolites]]` to the `parent` field in the frontmatter of `[[Alkaloids]]`."
    *   "In the `[[Shikimic Acid Pathway]]` frontmatter, add `[[Phenolic Compounds]]` and `Aromatic Amino Acids` to the `products` field."
    *   "Add a connection link in the frontmatter of `[[Polyketides]]` pointing to `[[Antimicrobial Activity]]`, mentioning it's a major source of antibiotics."
    *   "Update the `status` field in `[[Terpenoids]]` to `Developing`."
    *   "Add `[[Note A]]` and `[[Note B]]` to the `related` list in the frontmatter of `[[Note C]]`."

## 4. Tagging

*   **Goal:** Categorize notes using tags (e.g., `#concept`, `#biological_activity`, `#todo`). Preferably add to the frontmatter `tags:` list.
*   **Example Prompts:**
    *   "Add the tags `#metabolite` and `#phenolic_compound` to the frontmatter of `[[Coumarins]]`."
    *   "Ensure all notes in the `LearningSystem/connections/Biological Activity/` folder have the `#biological_activity` tag in their frontmatter."
    *   "Add an inline tag `#review_needed` in the `[[Glycosides]]` note section about Saponins."

## 5. Folder Organization

*   **Goal:** Move notes into appropriate folders for high-level structure.
*   **Example Prompts:**
    *   "Move the `[[Meroterpenoids and Prenylation]]` note into a new folder named `LearningSystem/connections/Structural Features/`."
    *   "Create a folder `LearningSystem/connections/Biological Activity/` and move the `[[Antimicrobial Activity]]` note into it."

## 6. External Links

*   **Goal:** Add links to web pages or external resources.
*   **Example Prompts:**
    *   "Add an external link to the Wikipedia page for 'Terpenoid' in the `[[Terpenoids]]` note."
    *   "In `[[Sources of Secondary Metabolites]]`, add a link `[PubMed Search](URL_HERE)` under a 'Further Reading' section."

## 7. Embeds / Transclusion

*   **Goal:** Embed content from one note into another.
*   **Example Prompts:**
    *   "In the `[[Secondary Metabolites]]` note, embed the definition section from `[[Alkaloids]]` using `![[Alkaloids#Definition]]`."
    *   "Embed the image `![[Metabolism Overview.png]]` into the `[[Biosynthetic Pathways Overview]]` note."

## 8. Combined / Complex Requests

*   **Goal:** Combine multiple connection types for a comprehensive update.
*   **Example Prompts:**
    *   "Create a new note for `[[Anti-inflammatory Activity]]` in the `Biological Activity` folder. Add `#biological_activity` tag. Link `[[Phenolic Compounds]]` and `[[Terpenoids]]` to it via frontmatter, mentioning they exhibit this activity. Also add inline links in those notes where anti-inflammatory effects are discussed."
    *   "Review the `[[Polyketides]]` note. Ensure it links to its biosynthetic pathway, relevant structural features (like prenylation if applicable), and key biological activities (Antimicrobial, Anticancer) using both frontmatter and inline links where appropriate."