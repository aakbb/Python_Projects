import sqlite3
def joinAlbums():
    connection = sqlite3.connect("chinook.db")
    cursor = connection.execute("""select albums.Title , artists.Name from artists inner join albums
                        on artists.ArtistId = albums.ArtistId""")
    for row in cursor:
        print("\n")
        print("Title: " + row[0])
        print("Name: " + row[1])
        print("\n")
        print("***********************************************")
    connection.commit()
    connection.close()

joinAlbums()