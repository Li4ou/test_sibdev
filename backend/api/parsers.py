import csv

from rest_framework.parsers import BaseParser

class CSVTextParser(BaseParser):
    media_type = 'multipart/form-data'

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Return a list of lists representing the rows of a CSV file.
        """
        media_type_params = dict([param.strip().split('=') for param in media_type.split(';')[1:]])
        charset = media_type_params.get('charset', 'utf-8')
        txt = stream.FILES.get('file').read().decode(charset)
        csv_table = list(csv.DictReader(txt.splitlines()))
        return csv_table
