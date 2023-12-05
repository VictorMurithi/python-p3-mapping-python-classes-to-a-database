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
    
    @classmethod
    def new_from_db(cls,row):
        song = cls(row[1],row[2])
        song.id = row[0]

    @classmethod
    def all(cls):
        sql = """
        SELECT * FROM songs
        """

        all = CURSOR. execute(sql).fetchall()
        cls.all = [cls.new_from_db(row) for row in all]

    @classmethod
    def find_by_name(cls,name):
        sql = """
        SELECT * FROM songs
        WHERE name = ?
        LIMIT 1
        """

        song = CURSOR.execute(sql, (name,)).fetchone()
        return cls.new_from_db(song)
    
# Create the table
Song.create_table()

# Create a Song instance and save it to the database
hello = Song('Hello', "25")
hello.save()
[song.__dict__ for song in Song.all()]
