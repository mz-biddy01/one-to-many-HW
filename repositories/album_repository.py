from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository


def save(album):
    sql = f"INSERT INTO albums (title, artist_id, genre) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.artist, album.genre]
    results = run_sql(sql, values)
    id = results[0][0]
    album.id = id
    return album


def delete_all():
    sql = 'DELETE FROM albums'
    run_sql(sql)


def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    print(result)

    if result is not None:
        album = Album(result[1], result[2], result[3], result[0])
    return album



def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        # album = album_repository.select(row[0])
        album = Album(row[0], row[0], row[0], row[0])
        albums.append(album)
    return albums


# Extensions

def delete(id):
    sql = "DELETE FROM tasks WHERE ID = %s"
    values =[0]
    run_sql(sql, values)


def update(album):
    pass
