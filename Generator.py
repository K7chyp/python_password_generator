from random import choice, randint, sample
import string
from hashlib import sha256
import functools


class Generator:

    def __init__(self, count):
        self.count = count

    def preprocessing(self):
        symbol_lst = list(string.printable)
        symbol_lst = sample(symbol_lst, len(symbol_lst))
        return symbol_lst

    def generate_pass(self):

        symbol_lst = self.preprocessing()
        password = []

        for i in range(self.count):
            password.append(choice(symbol_lst))

        return password

    def make_pass_list(self):
        pass_list = []

        for iter in range(100):
            some_pass = self.generate_pass()
            pass_list.append(sample(some_pass, len(some_pass)))

        return pass_list

    def build_pass(self):
        generated_pass = []
        pass_list = self.make_pass_list()

        for i in range(self.count+1):
            generated_pass.append(
                pass_list[randint(0, len(pass_list) - 1)][
                    randint(0, len(pass_list[0]) - 1)
                ]
            )

        return generated_pass

    def edit_it(self, pass_):
        pass_ = (
            pass_.replace("'", "")
            .replace(",", "")
            .replace("[", "")
            .replace("]", "")
            .replace(" ", "")
        )
        return pass_

    def hash_it(self):
        pass_ = self.edit_it(str(self.build_pass()))
        hash_pass = hashlib.sha256(pass_.encode("utf-8")).hexdigest()
        return hash_pass

    def post_processing(self):

        pass_ = list(self.hash_it())
        true_pass = []

        for iter in range(self.count+1):
            conditional = bool(randint(0, 1))
            if conditional == True:
                true_pass.append(pass_[randint(1, len(pass_) - 1)].upper())
            else:
                true_pass.append(pass_[randint(1, len(pass_) - 1)].lower())

        true_pass = self.edit_it(str(true_pass))

        return true_pass

    def make_it_more_randomly(self):
        pass_list = []
        for iter in range(100):
            pass_list.append(self.post_processing())
        return choice(pass_list)
