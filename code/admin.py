import config
import json

db = config.initFirestone()

f = open("data/songs.json")
data = json.load(f)