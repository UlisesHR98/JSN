
import os

from django.core.management.base import BaseCommand, CommandError

from pdftools.utils import JudgmentsExtractor

class Command(BaseCommand):
    help = 'Compares two judgment files'

    def add_arguments(self, parser):
        parser.add_argument('jsn_pdf_file',type=str)
        parser.add_argument('cj_pdf_file',type=str)

    def handle(self, *args, **options):
        pdf_dir = os.path.join('pdftools','test_docs')
        cj_pdf_filename = os.path.join(pdf_dir, 'test.pdf')
        jsn_pdf_filename = os.path.join(pdf_dir, 'jsn_search_report.pdf')

        cj_parser = JudgmentsExtractor(cj_pdf_filename, ptype="CJ")
        cj_judgments = cj_parser.parse_pdf_judgments()
        jsn_parser = JudgmentsExtractor(jsn_pdf_filename, ptype="JSN")
        jsn_judgments = jsn_parser.parse_pdf_judgments()

        print('Extracted CJ judgments: {}'.format(cj_judgments))
        print('Extracted JSN judgments: {}'.format(jsn_judgments))
        self.stdout.write(self.style.SUCCESS("Command completed"))
