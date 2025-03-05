-- 5-unique_id.sql
-- Create the table unique_id must be id 1 and unique id
--
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE PRIMARY KEY,
    name VARCHAR(256)
);