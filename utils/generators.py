import random
import string


class Generator:


    def random_string_lowercase(self, lenth=10):
        # returns lowercase
        return (''.join(random.choice(string.ascii_lowercase) for i in range(lenth)))


    def random_string_uppercase(self,lenth=10):
        # returns uppercase
        return (''.join(random.choice(string.ascii_uppercase) for i in range(lenth)))


    def random_digits(self, lenth=10):
        # returns digits
        return (''.join(random.choice(string.digits) for i in range(lenth)))

    def random_email(self, lenth=10):
        # returns digits
        return self.random_string_lowercase() + "@mail.com"

    def random_punctuation(self, lenth=10):
        # returns punctuation
        return (''.join(random.choice(string.punctuation) for i in range(lenth)))


    def generate_password(self,length=10, chars=string.ascii_letters + string.digits):
        return ''.join([random.choice(chars) for i in range(length)])
