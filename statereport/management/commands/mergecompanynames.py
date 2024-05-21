

import logging

from django.core.management.base import BaseCommand, CommandError
from django.db import connection

from statereport.models import Party


class Command(BaseCommand):
    help = 'Updates the statereport_party table with merged company names after data is imported'

    # def add_arguments(self, parser):
    #     parser.add_argument('quickbooks_csv_file', type=str)

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def handle(self, *args, **options):
        sql = """
            UPDATE statereport_party 
            SET merged_party_name = RTRIM(CONCAT(party_last_name, party_first_name, party_initial))
            where ((length(party_last_name) = 20 and length(party_first_name) > 0)
            or (length(party_last_name) <= 20 and party_first_name = ''))
            and (merged_party_name = '');;
        """
        sql2 = """
            UPDATE statereport_party
            SET full_search_party_name = CONCAT(party_last_name, party_first_name, party_initial, ' ',
                                                party_last_name, ' ', party_first_name, ' ', party_initial)
            WHERE full_search_party_name = '';
        """
        self.logger.info("Executing merged party update commands...")
        with connection.cursor() as cursor:
            cursor.execute(sql)
            cursor.execute(sql2)
            count_sql = """
                select count(1)
                from statereport_party
                where full_search_party_name <> ''        
            """
            cursor.execute(count_sql)
            count_results = cursor.fetchall()
            new_num_records = int(count_results[0][0])
            self.logger.info("Num merged full party names in database: {}".format(new_num_records))


