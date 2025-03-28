---
dataview: true
sr-interval: 1
sr-ease: 270
---


This is a dynamic database generated using Dataview. You can customize the table by modifying the code block below.

```dataview
TABLE WITHOUT ID file.link AS "File", title AS "Title", subject AS "Subject", unit AS "Unit", tags AS "Tags", aliases AS "Aliases", related_concepts AS "Related Concepts", status AS "Status", source_path AS "Source Path", concept_type AS "Concept Type", creation_date AS "Creation Date"
FROM ""
SORT file.name ASC
```

**Customization:**

*   **Columns:** You can add or remove columns by adding or removing the corresponding YAML property name after `file.link AS "File"`. For example, to add the `author` property, add `, author AS "Author"` to the `TABLE` line.
*   **Sorting:** You can change the sorting order by modifying the `SORT` line. For example, to sort by `title` in descending order, change it to `SORT title DESC`.
*   **Filtering:** You can filter the results by adding a `WHERE` clause. For example, to only show files with the tag `PharmaBio`, add `WHERE contains(tags, "PharmaBio")`.

**Available Properties:**

*   `file.path`: The path to the file.
*   `file.link`: A link to the file.
*   `title`: The title of the file.
*   `subject`: The subject of the file.
*   `unit`: The unit of the file.
*   `tags`: The tags of the file.
*   `aliases`: The aliases of the file.
*   `related_concepts`: The related concepts of the file.
*   `status`: The status of the file.
*   `source_path`: The source path of the file.
*   `concept_type`: The concept type of the file.
*   `creation_date`: The creation date of the file.

You can use any of these properties in the `TABLE`, `SORT`, and `WHERE` clauses.
