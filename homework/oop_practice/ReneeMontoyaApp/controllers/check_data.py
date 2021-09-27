# from models.plant import Plant
# from models.employee import Employee
# from controllers.menu import Menu


def check_data_is_present(cls, key, data):
    essences_in_list_format = cls.get_all()
    for el in essences_in_list_format:
        if el[key] == data:
            return True
        else:
            return False


def check_data_is_not_present(cls, key, data):
    essences_in_list_format = cls.get_all()
    for el in essences_in_list_format:
        if el[key] != data:
            return True
        else:
            return False
