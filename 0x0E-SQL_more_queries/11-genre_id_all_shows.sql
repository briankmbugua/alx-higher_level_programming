-- list all shows contained in the database hbtn_0d_tvshows display tv_shows.title-tv_show_genres.genre_id sort in ASC by tv_shows.title and tv_shows_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
