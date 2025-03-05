-- 4-never_empty.sql
-- Create the table id_not_null
--
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT default 1,
    name VARCHAR(256)
);