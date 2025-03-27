---
Cognitive Load: Medium
Confidence: Medium
Date: 2025-03-27
Date Accessed: null
Elaboration Level: Basic
Forgetting Index: 1.0
Last Reviewed Date: null
Mnemonic Encoding: ''
Purpose: Reference for Roo (AI Assistant) on creating logical connections in this
  Obsidian vault.
Source: ''
Spaced Repetition Interval: 1
Tags: null
Type: Guideline
connections:
- Primary Metabolites: Key differences in function, production, etc.
- Pharmaceutical Biotechnology: Significance and applications in pharmaceuticals
- Industrial Biotechnology: Production and optimization in industrial settings
- Sources of Secondary Metabolites: Classification based on biological sources
- Plant Sources of Secondary Metabolites: Detailed list of plant-derived secondary
    metabolites
- Fungal Sources of Secondary Metabolites: Detailed list of fungal-derived secondary
    metabolites
- Bacterial Sources of Secondary Metabolites: Detailed list of bacterial-derived secondary
    metabolites
- Animal Sources of Secondary Metabolites: Detailed list of animal-derived secondary
    metabolites
- Biosynthetic Pathways/Biosynthetic Pathways Overview: Overview of how secondary
    metabolites are synthesized
coverage: 0.0
review_dates:
- 2025-03-27: Initial creation
- '2025-03-27: Added by script'
tags:
- concept
- metabolite
- classification
- source
- pharmaceutical_biotechnology
- PB_Unit_I
---


# Roo: Obsidian Connection Guidelines

This document outlines the preferred methods for creating connections between notes in this Obsidian vault, ensuring logical structure and consistency.

## Core Connection Methods & Usage

1.  **Internal Links (`[[Wikilinks]]`)**:
    *   **Use:** Primary method for linking directly related concepts within the main text. Use for explicit relationships mentioned in the content. Link to specific headings (`#Heading`) or blocks (`#^blockid`) where appropriate for precision.
    *   **Logic:** Represents a direct conceptual association or reference.
    *   **Example:** `[[Alkaloids]] are derived from [[Amino Acid Derived Pathways]].`

2.  **Frontmatter (YAML Metadata)**:
    *   **Use:** Define structured relationships and metadata. Essential for Dataview queries and maintaining consistency. Use specific keys for common relationships:
        *   `type:` (e.g., `Concept`, `Pathway`, `Source`, `Overview`, `Guideline`)
        *   `status:` (e.g., `Stub`, `Developing`, `Complete`)
        *   `parent:` (Link to broader category/topic note)
        *   `related:` (List of generally related concepts)
        *   `connections:` (List of key links with brief descriptions, as used previously)
        *   `products:` (For pathways: link to resulting metabolite classes)
        *   `precursors:` (For pathways/metabolites: link to starting materials)
        *   `source_of:` (For source notes: link to metabolites found there)
        *   `derived_from:` (For metabolites: link to source types)
        *   `tags:` (List of relevant tags - see below)
    *   **Logic:** Establishes explicit, typed relationships and provides structured data about the note. Crucial for organization and automated retrieval.
    *   **Example:**
        ```yaml
        ---
        type: Pathway
        parent: [[Biosynthetic Pathways Overview]]
        products: [[Terpenoids]]
        precursors: [Acetyl-CoA]
        tags: [biochemistry, pathway, MVA]
        ---
        ```

3.  **Tags (`#tagname`)**:
    *   **Use:** Primarily for categorization, status tracking, and filtering. Use consistently. Prefer adding tags in the frontmatter `tags:` list for cleaner notes, but inline tags are acceptable for quick marking. Use nested tags for hierarchy (e.g., `#metabolite/alkaloid`).
    *   **Logic:** Groups notes by broad categories, themes, or status, enabling efficient filtering and searching. Less specific than direct links or typed frontmatter relationships.
    *   **Current Tags:** `#concept`, `#metabolite`, `#pathway`, `#source`, `#classification`, `#guideline`, subject tags (e.g., `#pharmaceutical_biotechnology`), unit tags (e.g., `#PB_Unit_I`).

4.  **Folders**:
    *   **Use:** High-level structural organization. Group related notes logically (e.g., `Metabolites`, `Sources`, `Biosynthetic Pathways`, `Subjects`). Use `path:` queries in graph view/Dataview based on this structure.
    *   **Logic:** Provides a hierarchical overview and aids file system navigation. Complements linking/tagging.

5.  **Embeds / Transclusion (`![[Note Name]]`)**:
    *   **Use:** Sparingly, primarily for embedding definitions, reusable blocks, or figures where seeing the content inline is beneficial. Avoid over-embedding, as it can make notes long and harder to edit.
    *   **Logic:** Creates a link while displaying content, useful for composition and avoiding repetition.

## General Principles

*   **Bidirectionality:** When adding a significant link (especially structural ones like pathway -> metabolite), ensure the corresponding link exists or is added in the target note's frontmatter or body (e.g., metabolite -> pathway).
*   **Clarity:** Use descriptive link text or frontmatter descriptions (`connections:` field) where the relationship isn't immediately obvious from the context.
*   **Consistency:** Adhere to these guidelines to maintain a predictable and useful knowledge graph. Use established frontmatter keys and tags.
*   **Purpose:** Always consider *why* a connection is being made and choose the most appropriate method (link, tag, metadata) to represent that relationship.