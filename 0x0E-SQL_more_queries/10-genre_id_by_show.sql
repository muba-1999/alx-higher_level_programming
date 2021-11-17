-- lists the shows containedin hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_show_genres INNER JOIN tv_shows ON tv_show_genres.genre_id = tv_show.id ORDER BY tv_shows.title, tv_show_genres.genre_id;
