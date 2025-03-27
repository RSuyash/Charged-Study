# Standardization Plan for Obsidian Notes

This document outlines the plan for standardizing the properties of notes in the Obsidian vault, ensuring consistency and facilitating AI-powered learning and memory enhancement.

## I. Standardized Properties

*   **Metadata:**
    *   `Title` (string): The title of the note.
    *   `Creator` (string): The author of the note.
    *   `Created Date` (date): The date the note was created.
    *   `Last Modified Date` (date): The date the note was last modified.
    *   `Subject` (string): The subject or course the concept belongs to.
    *   `Subject Code` (string): The course code for the subject.
    *   `Lecturer` (string): The instructor or presenter of the material.
    *   `Tags` (list of strings): Keywords or categories associated with the concept.
    *   `Related Units` (list of links): Links to related units or modules.
    *   `Connections` (list of objects): Links to related concepts and their relationships. Each object should have:
        *   `Target` (link): Link to the related concept.
        *   `Relationship` (string): Description of the relationship.
*   **Content:**
    *   `Definition` (string): A concise definition of the concept.
    *   `Key Principles` (list of strings): The fundamental principles underlying the concept.
    *   `Applications` (list of strings): Real-world applications of the concept.
    *   `Memory Hooks` (list of strings): Mnemonic devices or memory aids.
    *   `Visual Aids` (list of links): Links to relevant images or diagrams.
    *   `Active Recall Questions` (list of objects): Questions to test understanding of the concept. Each object should have:
        *   `Question` (string): The question.
        *   `Answer` (string): The answer.
*   **Source & Reliability:**
    *   `Source` (string): The origin of the information (e.g., textbook, research paper, website).
    *   `Confidence` (enum: High, Medium, Low): Subjective assessment of the reliability of the source and the accuracy of the information.
    *   `Date Accessed` (date, optional): The date the source was accessed (if applicable, e.g., for online sources).
*   **Learning & Review:**
    *   `Coverage` (float): A numerical value representing the completeness or coverage of the concept (0.0 to 1.0).
    *   `Review Dates` (list of objects): Dates for reviewing the note. Each object should have:
        *   `Date` (date): The review date.
        *   `Notes` (string, optional): Any notes or comments about the review.
    *   `Difficulty` (enum: Easy, Medium, Hard): Subjective assessment of the concept's difficulty.
    *   `Importance` (enum: High, Medium, Low): Subjective assessment of the concept's importance.
    *   `Spaced Repetition Interval` (integer): The interval (in days) for the next review, based on spaced repetition principles.
    *   `Last Reviewed Date` (date): The date when the concept was last reviewed.
    *   `Forgetting Index` (float): A measure of how well the concept is retained (0.0 to 1.0, where 1.0 is perfect retention).
    *   `Cognitive Load` (enum: Low, Medium, High): Subjective assessment of the cognitive effort required to understand the concept.
    *   `Elaboration Level` (enum: Basic, Intermediate, Advanced): Subjective assessment of the depth and detail of the note's content.
    *   `Mnemonic Encoding` (string): Description of the mnemonic technique used to encode the concept (if any).

## II. Data Types

*   `string`: Textual data.
*   `date`: Date in YYYY-MM-DD format.
*   `list`: An ordered collection of items.
*   `link`: A link to another note or resource (e.g., a URL or a wiki link).
*   `float`: A floating-point number.
*   `enum`: A set of predefined values.
*   `integer`: A whole number.

## III. Handling Missing Properties

*   For existing notes that lack certain properties, the properties should be added with a default value (e.g., an empty string for string properties, an empty list for list properties, 0.0 for coverage, etc.).
*   A script or tool should be created to automatically add these properties to existing notes.

## IV. Mermaid Diagram

\`\`\`mermaid
classDiagram
    class Note {
        +string Title
        +string Creator
        +date Created Date
        +date Last Modified Date
        +string Subject
        +string Subject Code
        +string Lecturer
        +list~string~ Tags
        +list~Link~ Related Units
        +list~Connection~ Connections
        +string Definition
        +list~string~ Key Principles
        +list~string~ Applications
        +list~string~ Memory Hooks
        +list~Link~ Visual Aids
		+list~ActiveRecallQuestion~ Active Recall Questions
        +string Source
        +enum Confidence {High, Medium, Low}
        +date Date Accessed
        +float Coverage
        +list~ReviewDate~ Review Dates
        +enum Difficulty {Easy, Medium, Hard}
        +enum Importance {High, Medium, Low}
        +integer Spaced Repetition Interval
        +date Last Reviewed Date
        +float Forgetting Index
        +enum Cognitive Load {Low, Medium, High}
        +enum Elaboration Level {Basic, Intermediate, Advanced}
        +string Mnemonic Encoding
    }

    class Link {
        +string URL
        +string Description
    }

    class Connection {
        +Link Target
        +string Relationship
    }

	class ActiveRecallQuestion {
		+string Question
		+string Answer
	}

    class ReviewDate {
        +date Date
        +string Notes
    }

    Note "1" -- "*" Link : Related Units
    Note "1" -- "*" Connection : Connections
	Note "1" -- "*" ActiveRecallQuestion : Active Recall Questions
    Note "1" -- "*" ReviewDate : Review Dates
\`\`\`

## V. Implementation Plan

1.  **Initialize a Git repository:** If one doesn't already exist, initialize a Git repository in the ObsidianVault directory.
2.  **Create a new branch:** Create a new branch (e.g., "standardize-properties") to isolate the changes.
3.  **Create a Python script:** This script will:
    *   Read each markdown file in the vault.
    *   Parse the YAML frontmatter (if it exists).
    *   Add any missing properties to the frontmatter with default values.
        *   Default values for new properties:
            *   `Source`: ""
            *   `Confidence`: Medium
            *   `Date Accessed`: null
            *   `Spaced Repetition Interval`: 1
            *   `Last Reviewed Date`: null
            *   `Forgetting Index`: 1.0
            *   `Cognitive Load`: Medium
            *   `Elaboration Level`: Basic
            *   `Mnemonic Encoding`: ""
    *   Write the modified content back to the markdown file.
4.  **Run the script on the entire vault:** This will ensure that all notes have the standardized properties.
5.  **Validate the results:** Manually inspect a few notes to ensure that the properties have been added correctly.
6.  **Commit the changes:** Commit the changes to the "standardize-properties" branch.
7.  **Push the branch to GitHub:** Push the "standardize-properties" branch to the user's GitHub repository (RSuyash/Charged-Study).