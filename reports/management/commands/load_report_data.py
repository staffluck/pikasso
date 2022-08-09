import csv

from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand
# from django.db import transaction

from reports.models import Report


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('file_paths', nargs='+', type=str)

    def handle(self, *args, **options):
        paths = options["file_paths"]
        exc_msgs = []
        for file_path in paths:
            with open(file_path, "r", newline="") as f:
                reader = csv.reader(f, delimiter=",", quotechar="|")
                next(reader, None)  # Пропустить название столбцов
                for row in reader:
                    if len(row) > 14:
                        print("Bad row")
                    else:
                        print(f"Processing: {row[0]}")
                        Report.objects.create(
                            crime_id = row[0],
                            crime_type_name = row[1],
                            report_date = row[2],
                            call_date = row[3],
                            offense_date = row[4],
                            call_time = row[5],
                            call_datetime = row[6],
                            disposition = row[7],
                            address = row[8],
                            city = row[9],
                            state = row[10],
                            agency_id = row[11],
                            address_type = row[12],
                            common_location = row[13],
                        )
        print(exc_msgs)