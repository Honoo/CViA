import abc
import json
from data_source import DataSource

class JSONDataSource(DataSource):

    @classmethod
    def load(cls, filepath):
        with open(filepath) as data_file:
            data = json.load(data_file)
        return data
