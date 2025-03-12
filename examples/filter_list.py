import random
from pprint import pprint

import inquirer  # noqa


choice_change = []
choices = list(random.__dict__.keys())
random.shuffle(choices)


def filter_func(text, collection):
    f = filter(lambda x: text in x, collection)
    return list(f)


def callback_listener(item):
    choice_change.append(item)


questions = [
    inquirer.FilterList(
        "food selection",
        message="Select item ",
        choices=choices,
        carousel=False,
        filter_func=filter_func,
        choice_callback=callback_listener,
    ),
]

answers = inquirer.prompt(questions)

pprint(choice_change)
pprint(answers)
