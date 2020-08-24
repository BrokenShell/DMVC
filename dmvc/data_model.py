""" Astrological Sign Prediction
Data Model

By Broken
August 2020 """
from os import getenv
import pandas as pd
from pymongo import MongoClient


__all__ = ('DataBase',)


class DataBase:
    """ Data Model for Astrological Sign Prediction """

    def connect_db(self):
        """ Returns MongoDB connection handle """
        return MongoClient(
            f"mongodb+srv://{getenv('MONGODB_USER')}:{getenv('MONGODB_PASS')}"
            f"@{getenv('MONGODB_URI')}/test?retryWrites=true&w=majority"
        ).astrology.signs

    def query_db(self, query_obj: dict) -> dict:
        """ Returns datum from database """
        return next(self.connect_db().find(query_obj))

    def read_csv(self) -> pd.DataFrame:
        """ Reads a csv file and returns a DataFrame """
        return pd.read_csv('dmvc/data.csv')

    def _make_db(self) -> None:
        """ Create and populate the database """
        db = self.connect_db()
        data = self.read_csv().to_dict(orient='records')
        db.insert_many(data)


# if __name__ == '__main__':
#     DataBase()._make_db()
