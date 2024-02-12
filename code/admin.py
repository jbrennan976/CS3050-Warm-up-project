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

def get_filename():
    f = input("Please enter the name of the json file you would like to upload: ")
    while not(f.endswith(".json")):
        print("Error: file must be in .json form")
        f = input("Please enter the name of the json file you would like to upload: ")
    return f

def upload_data():
    clear_data()
    filename = get_filename()
    filepath = "data/" + filename
    try:
        f = open(filepath)
    except FileNotFoundError:
        print("The file does not exist or cannot be found, please try again")   
    else:
        data = json.load(f)
        for line in data:
            song_line = SongLine(line["Rank"], line["Artist"], line["Song"], line["Features"])
            db.collection("song_rankings").add(song_line.to_dict())
        print("Data successfully uploaded")

upload_data()

