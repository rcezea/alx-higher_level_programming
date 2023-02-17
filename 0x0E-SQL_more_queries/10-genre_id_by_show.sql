-- list all shows contained in hbtn_0d_tvshows
-- that have at least one genre linked
SELECT ts.title, tsg.genre_id
FROM tv_shows AS ts INNER JOIN tv_show_genres AS tsg
WHERE ts.id = tsg.show_id
ORDER BY ts.title, tsg.genre_id;
