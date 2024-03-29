import config
import json

db = config.initFirestone()

# used to define/create a song object
class Song:
    def __init__(self, rank, artist, song, features, has_feature):
        self.rank = rank
        self.artist = artist
        self.song = song
        self.features = features
        self.has_feature = has_feature
    
    def to_dict(self):
        return {
            "Rank": self.rank,
            "Artist": self.artist,
            "Song": self.song,
            "Features": self.features,
            "has_feature": self.has_feature
            }

# clear the current data in the DB
def clear_data():
    docs = db.collection("song_rankings").get()
    for doc in docs:
        doc.reference.delete()

# get the filename to be referenced for data
def get_filename():
    f = input("Please enter the name of the json file you would like to upload: ")
    while not(f.endswith(".json")):
        print("Error: file must be in .json form")
        f = input("Please enter the name of the json file you would like to upload: ")
    return f

# upload the data using a .json file
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
            song_line = Song(line["Rank"], line["Artist"], line["Song"], line["Features"], line["has_feature"])
            db.collection("song_rankings").add(song_line.to_dict())
        print("Data successfully uploaded")

upload_data()

