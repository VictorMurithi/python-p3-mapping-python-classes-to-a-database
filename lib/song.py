from config import CONN, CURSOR

class Song:
    def __init__(self, name, album):
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = '''
        CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY,
            name TEXT,
            album TEXT
        )
        '''
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
        INSERT INTO songs (name, album)
        VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.album))
        CONN.commit()
        self.id = CURSOR.lastrowid
    @classmethod
    def create(cls,name,album):
        song = Song(name,album)
        song.save()
        return song

# Create the table
Song.create_table()

# Create a Song instance and save it to the database
hello = Song('Hello', "25")
hello.save()

songs = CURSOR.execute('SELECT * FROM songs')
[row for row in songs]

print(songs)