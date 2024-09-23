import random

BASE_URL = 'https://qa-scooter.praktikum-services.ru/'
DZEN_URL = 'https://dzen.ru/?yredirect=true'
DZEN_TITLE = "Дзен"

name = ['Александр', 'Николай', 'Вадим', 'Павел']
RANDOM_NAME = random.choice(name)
first_name = ['Иванов', 'Фёдоров', 'Степанов', 'Сергеев']
RANDOM_FIRST_NAME = random.choice(first_name)
address = ['Советская', 'Молодежная', 'Рабочая', 'проспект Мира']
RANDOM_ADDRESS = random.choice(address)
PHONE_NUM = '8' + ''.join([str(random.randint(0, 9)) for _ in range(10)])
DATA_OF_RENT = "12.12.2024"

