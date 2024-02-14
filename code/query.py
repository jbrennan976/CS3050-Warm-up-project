from google.cloud import firestore
from Parser import Query
import config
db = config.initFirestone()
song_ref = db.collection("song_rankings")

def query_db(query):
    req = song_ref.where("Rank", '>=', query.Lower_Rank).where("Rank", '<=', query.Upper_Rank)
    if query.Artist is not None:
        req = req.where('Artist', '==', query.Artist)
    if query.Title is not None:
        req = req.where('Song', '==', query.Title)
    if query.Features:
        req = req.where("has_feature", "==", True)
    if not query.Desc:
        req = req.order_by('Rank', direction=firestore.Query.ASCENDING)

    res = []
    data = req.get()
    for e in data:
        res.append(e.to_dict())
    return res


if __name__ == "__main__":
    ex_q = query_db(Query(1, 40, "Lady GaGa", None, False, True))
    print(ex_q)
