class Music_Record():
    def __init__(self, artist, track, title, album, year):
        self.artist = artist
        self.year = year
        self.track = track
        self.title = title
        self.album = album
    def __str__(self):
        return str({
            "Artist":self.artist,
            "Track": self.track,
            "Year": self.year,
            "Title": self.title,
            "Album": self.album
        })

cd = Music_Record("AC/DC", "-", "Back in Black", "AC/DC", 1980)
print(cd)
        