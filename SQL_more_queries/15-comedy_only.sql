-- 15-comedy_only.sql
-- Import the database dump from hbtn_0d_tvshows
-- Lists all Comedy shows in the database hbtn_0d_tvshows
-- Display: tv_shows.title
-- Sorted in ascending order by the show title
--
SELECT tv_genres.title
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_genres.title = 'Comedy'
ORDER BY tv_shows.title ASC;