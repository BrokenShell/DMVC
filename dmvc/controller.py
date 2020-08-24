""" Astrological Sign Prediction
Control Bot

By Broken
August 2020 """
from Fortuna import random_below
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from dmvc.data_model import DataBase


__all__ = ('Bot',)


class Bot:
    """ NLP Suggestion Bot """

    db = DataBase()
    df = db.read_csv()
    tfidf = TfidfVectorizer(
        stop_words='english',
        ngram_range=(1, 3),
        max_features=15000,
    )
    knn = NearestNeighbors(
        n_neighbors=1,
        n_jobs=-1,
    ).fit(tfidf.fit_transform(df['Text']).todense())

    def id_lookup(self, _id: int) -> dict:
        """ Lookup by id """
        return self.db.query_db({'_id': _id})

    def sign_lookup(self, sign: str) -> dict:
        """ Lookup by sign """
        return self.db.query_db({'Sign': sign})

    def search(self, user_input: str) -> dict:
        """ Natural language search """
        vec = self.tfidf.transform([user_input]).todense()
        idx = self.knn.kneighbors(vec, return_distance=False)[0][0]
        return self.id_lookup(int(idx))

    def random(self) -> dict:
        """ Returns a random entry """
        idx = random_below(len(self.df))
        return self.id_lookup(idx)


if __name__ == '__main__':
    bot = Bot()
    print(bot.search("intelligent self awareness"))
