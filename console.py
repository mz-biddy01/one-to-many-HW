import pdb
from models.artist import Artist
from models.album import Album
from db.run_sql import run_sql

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist1 = Artist("Rihanna")
artist_repository.save(artist1)

artist2 = Artist("Burna Boy")
artist_repository.save(artist2)




album_1 = Album("African Giant", 2, "Afro Beats")
album_2 = Album("Unapologetic", 1, "nobody" "Pop")



album_repository.save(album_1)
album_repository.save(album_2)

# album_repository.delete_all()
# artist_repository.delete_all()

artist_repository.select(1)
album_repository.select(2)

# res = album_repository.select_all()
# for album in res:
#     print(album.__dict__)


# res = artist_repository.select_all()
# for artist in res:
#     print(artist.__dict__)



pdb.set_trace()
