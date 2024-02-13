import Parser
import config
from Parser import Query

db = config.initFirestone()
song_ref = db.collection("song_rankings")

example_query = Query(5, None, None, None, None, False)

def query_db(query):
    example_query.Lower_Rank
    print (example_query.Lower_Rank)

query_db(example_query)