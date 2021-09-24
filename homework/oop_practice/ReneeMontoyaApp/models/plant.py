from framework.models import Model
from models.employee import Employee


class Plant(Model):
    file = "plants.json"

    def __init__(self, id_plant, location, name, director_id):
        self.id = id_plant
        self.location = location
        self.name = name
        self.director_id = director_id

    def _set_dict(self):
        return {'id': self.id,
                'location': self.location,
                'name': self.name,
                'director_id': self.director_id}

    # def save(self):
    #     plant_in_dict_format = self._generate_dict()
    #     plants = self.get_file_data(self.file)
    #     plants.append(plant_in_dict_format)
    #     self.save_to_file(plants)

    @staticmethod
    def get_employee_class():
        return Employee.__name__

    @staticmethod
    def get_by_email(email):
        data_employees = Employee.get_file_data(Employee.file)
        for el in data_employees:
            if el['email'] == email:
                return el["id"]

        raise Exception("Not found")
