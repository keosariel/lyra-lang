import re

class Outcommentor():

    code = ""

    def __init__(self, code):
        self.code = re.sub(code, r'(\/\*\*)(.|\n)+?(\*\/)', '')
