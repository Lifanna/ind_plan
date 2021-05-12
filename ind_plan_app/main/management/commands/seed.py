from django.core.management.base import BaseCommand
from django.core.files import File
from django.utils.timezone import now
from main import models
from edu_work._models import edu_method_work_models
import datetime
import os
from pathlib import Path
import logging


class Command(BaseCommand):
    def handle(self, *args, **options):
        # assert(os.getenv('DJANGO_ENVIRONMENT') == "DEVELOPMENT")
        # self.clear_db()
        self.populate_db()

    def clear_db(self):
        # по пользователю
        models.Status.objects.all().delete()
        models.AcademicDegree.objects.all().delete()
        models.AcademicRank.objects.all().delete()
        models.Rate.objects.all().delete()
        models.BusinessForm.objects.all().delete()
        models.Chair.objects.all().delete()
        models.Faculty.objects.all().delete()

        # по учебной работе

        # по учебно-методической работе

        # по научно-методической работе

        # по организационно-методической работе


    # запись данных в таблицу по файлу
    def insert_records_from_file(self, file_name, model_instance):
        records = []
        with open(file_name, 'r', encoding='utf8') as file:
            records = file.readlines()

        success = False

        try:
            for record in records:
                model_table = model_instance(name=record.strip())
                model_table.save()

            success = True

            # логгируем об успешности записи
            logger = logging.getLogger(__name__)
            logging.info("Добавлена запись в таблицу модели %s"%model_instance._meta.verbose_name.title())
        except Exception as e:
            # логгируем об ошибке
            logging.error(e.message)
            success = False
        finally:
            return success

    def populate_db(self):
        # должности
        # self.insert_records_from_file('main/management/commands/statuses.txt', models.Status)
        # self.insert_records_from_file('main/management/commands/academic_degrees.txt', models.AcademicDegree)
        # self.insert_records_from_file('main/management/commands/academic_ranks.txt', models.AcademicRank)
        # self.insert_records_from_file('main/management/commands/chairs.txt', models.Chair)
        # self.insert_records_from_file('main/management/commands/faculties.txt', models.Faculty)
        # self.insert_records_from_file('main/management/commands/specialties.txt', edu_method_work_models.Specialty)
        self.insert_records_from_file('main/management/commands/edu_method_work_types.txt', edu_method_work_models.EduMethodWorkType)
        
        # BASE_DIR = Path(__file__).resolve().parent
