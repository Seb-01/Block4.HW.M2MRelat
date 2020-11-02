from django.core.management.base import BaseCommand, CommandError
from articles.models import Article
import json

class Command(BaseCommand):
    help = 'Загрузка данных из json файла'

    def add_arguments(self, parser):
        # Парсер наследуется от argparse.ArgumentParser, и про аргументы, принимаемые функцией add_argument,
        # можно почитать в документации к библиотеке argparse в документации python

        # получаем один неименованный аргумент (dest='args')
        # nargs=1 - количество аргументов
        parser.add_argument(nargs=1, type=str, dest='args', help='Имя файла с json данными')


    # требуется аргумент - имя файла, например так:
    # python manage.py insert_data_from_json <jsonfile name>
    def handle(self, *args, **options):
        #self.stdout.write(*args)

        with open(*args, encoding='utf-8') as data_file:
            json_data = json.loads(data_file.read())

            for record in json_data:
                result=Article(
                    title=record['fields']['title'],
                    text=record['fields']['text'],
                    published_at=record['fields']['published_at'],
                    image=record['fields']['image'],
                )
                result.save()
