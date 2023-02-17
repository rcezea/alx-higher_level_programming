-- lists all genres of the show Dexter
SELECT tvg.name
FROM tv_genres AS tvg INNER JOIN tv_show_genres AS tsg
ON tsg.genre_id = tvg.id
/*WHERE tsg.show_id = (
    SELECT id FROM tv_shows AS ts
    WHERE ts.title = 'Dexter'
)*/
INNER JOIN tv_shows AS ts
ON tsg.show_id = ts.id
WHERE ts.title = 'Dexter'
ORDER BY tvg.name;
