import json
from abc import ABC, abstractmethod
# from models.employee import Employee


class Model(ABC):
    file = 'default.json'

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def _generate_dict(self):
        pass

    @classmethod
    def get_by_id(cls, id):
        data = cls.get_file_data(cls.file)
        for el in data:
            if el['id'] == id:
                return el

        raise Exception("Not found")

    @classmethod
    def get_all(cls):
        data = cls.get_file_data(cls.file)
        return data

    @staticmethod
    def get_file_data(file_name):
        file = open("database/" + file_name, 'r')
        data = json.loads(file.read())
        file.close()
        return data

    @classmethod
    def _generate_dict(cls):
        return cls.set_dict(cls)

    @classmethod
    def save(cls):
        essence_in_dict_format = cls._generate_dict()
        essence = cls.get_file_data(cls.file)
        essence.append(essence_in_dict_format)
        cls.save_to_file(essence)

    def save_to_file(self, data):
        data = json.dumps(data)
        file = open('database/' + self.file, "w")
        file.write(data)
        file.close()
