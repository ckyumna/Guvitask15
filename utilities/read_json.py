import json


class ReadJson:

    @staticmethod
    def get_json_data(file_path):

        with open(file_path) as file:
            data = json.load(file)

        return data