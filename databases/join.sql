SELECT 
    authors.publication_id,
    authors.author_role, 
    (all_contributors.first_name || " " || all_contributors.last_name) as fullname,
    all_contributors.first_name,
    all_contributors.last_name,
    all_contributors.organization,
    all_contributors.is_associate,
    all_contributors.is_refered
FROM
    authors 
    INNER JOIN all_contributors ON authors.short_name = all_contributors.short_name
    LEFT JOIN publications ON authors.publication_id = publications.publication_id
ORDER BY publications.publication_id