import random


def get_data_for_make_order():
    """
    :return: name, first_name, address, tel., data
    """
    name = ['Александр', 'Николай', 'Вадим', 'Павел']
    random_name = random.choice(name)
    first_name = ['Иванов', 'Фёдоров', 'Степанов', 'Сергеев']
    random_first_name = random.choice(first_name)
    address = ['Советская', 'Молодежная', 'Рабочая', 'проспект Мира']
    random_address = random.choice(address)
    phone_num = '8' + ''.join([str(random.randint(0, 9)) for _ in range(10)])
    data_of_rent = "12.12.2024"
    return random_name, random_first_name, random_address, phone_num, data_of_rent
