-- List score then name from second_table, exclude rows where name is NULL or empty, order by score descending.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name <> ''
ORDER BY score DESC;
