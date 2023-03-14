-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download
-- Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- 	Each record should display: tv_shows.title - tv_show_genres.genre_id
-- 	Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- 	Only one SELECT statement.
SELECT ts.title, tsg.genre_id
FROM tv_shows AS ts
INNER JOIN tv_show_genres AS tsg
ON ts.id = tsg.show_id
ORDER BY ts.title, tsg.genre_id;
