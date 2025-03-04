-- 15-groups.sql
-- List a number of records with the same score
--
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score;