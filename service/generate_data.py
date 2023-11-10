import csv
import random

async def create_name():
    with open('data/name_data.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    random_row = random.choice(data)
    return random_row[0]

async def create_adjectives():
    with open('data/adjectives.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    random_row = random.choice(data)
    return random_row[0]