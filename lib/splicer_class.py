import math


class Splicer:

    def __init__(self, _text, _delimiting_size=280):
        self.text = _text
        self.split = split(self.text, delimiting_size=_delimiting_size)

    def get_split(self):
        return self.split


def split(text, delimiting_size):
    size_of_current_text = float(len(text))
    range_number = math.ceil(size_of_current_text / float(delimiting_size))
    return [text[i * delimiting_size:(i+1) * delimiting_size] for i in range(range_number)]
