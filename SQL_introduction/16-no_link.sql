-- 16-no_link.sql
-- List all records from second_table with score and name
--
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;