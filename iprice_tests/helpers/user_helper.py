import random
import string


class UserHelper:

    @staticmethod
    def get_random_chars():
        """Return random Characters with random length of 7 to 10
        :return: Random Characters"""
        letters = list(string.ascii_lowercase)
        size = random.randint(7, 10)
        random.shuffle(letters)
        return ''.join(letters[:size])

    @classmethod
    def get_random_email(cls):
        """Return an email address consisting of random letters
        :return: A randomized email address
        """
        domain = random.choice(['com', 'org', 'co.uk', 'com.my'])
        return f'{cls.get_random_chars()}@Test.{domain}'

