from pyknp import KNP as PYKNP, JUMAN_FORMAT


class KNP:
    def __init__(self, *args, **kwargs):
        self.knp = PYKNP(*args, **kwargs)

    def parse(self, sentence, juman_format=JUMAN_FORMAT.DEFAULT):
        return self.parse(sentence, juman_format)
