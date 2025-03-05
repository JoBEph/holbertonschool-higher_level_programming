-- 14-my_genres.sql
-- Import the database dump of hbtn_0d_tvshows
--  uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
-- The tv_shows table contains only one record where title = Dexter
-- Display: tv_genres.name
-- Results sorted in ascending order by the genre name

SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_show_genres.show_id = (SELECT id FROM tv_shows WHERE title = 'Dexter')
ORDER BY tv_genres.name ASC;