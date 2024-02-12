import config
import json

db = config.initFirestone()

class SongLine:
    def __init__(self, rank, artist, song, features):
        self.rank = rank
        self.artist = artist
        self.song = song
        self.features = features
    
    def to_dict(self):
        return {
            "Rank": self.rank,
            "Artist": self.artist,
            "Song": self.song,
            "Features": self.features
            }

def clear_data():
    docs = db.collection("song_rankings").get()
    for doc in docs:
        doc.reference.delete()

def upload_data():
    clear_data()
    f = open("data/songs.json")
    data = json.load(f)
    for line in data:
        song_line = SongLine(line["Rank"], line["Artist"], line["Song"], line["Features"])
        db.collection("song_rankings").add(song_line.to_dict())

upload_data()

