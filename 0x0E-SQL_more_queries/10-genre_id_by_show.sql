-- list all shows contained in hbtn_0d_tvshwos
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
