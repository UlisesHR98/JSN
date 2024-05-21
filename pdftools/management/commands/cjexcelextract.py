
import os

from django.core.management.base import BaseCommand, CommandError

from pdftools.utils import CJPDFExtractor

class Command(BaseCommand):
    help = 'Extract data from a CJ pdf for incorporation into an excel file'

    # def add_arguments(self, parser):
        # parser.add_argument('jsn_pdf_file',type=str)
        # parser.add_argument('cj_pdf_file',type=str)

    def handle(self, *args, **options):
        pdf_dir = os.path.join('pdftools','test_docs')
        # cj_pdf_filename = os.path.join(pdf_dir, '5304345 Charles Jones.pdf')
        cj_pdf_filename = os.path.join(pdf_dir, 'copy of 100107 CJ 100125.pdf')

        cj_parser = CJPDFExtractor(cj_pdf_filename, ptype="CJ")
        cj_parser.parse_pdf_data_for_excel()

        # print('Extracted CJ judgments: {}'.format(cj_parser.parsed_judgments))
        self.stdout.write(self.style.SUCCESS("Command completed"))