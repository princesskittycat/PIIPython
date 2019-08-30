import re


class RegexValidator(object):
    EMAILS = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\b'
    SSNS = r'[0-9]{3}-{0,1}[0-9]{2}-{0,1}[0-9]{4}'
    PHONE_NUMBERS = r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4})'
    VISA_CC = r'4[0-9]{12}(?:[0-9]{3})?'
    MASTERCARD_CC = r'(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14})'
    AMEX_CC = r'\d{4}-?\d{4}-?\d{4}-?\d{4}'

    def __init__(self):
        self.__dict = {'EMAILS': RegexValidator.EMAILS,
                       'SSNS': RegexValidator.SSNS,
                       'PHONE_NUMBERS': RegexValidator.PHONE_NUMBERS,
                       'VISA_CC': RegexValidator.VISA_CC,
                       'MASTERCARD_CC': RegexValidator.MASTERCARD_CC,
                       'AMEX_CC': RegexValidator.AMEX_CC
                       }

    def find_match(self, input_string):
        """
        :param input_string: string
        :return: self.__dict key when matching value or None when not matching anything
        """
        for key in self.__dict:
            match = re.search(self.__dict[key], input_string)
            if match:
                return key
        return None
