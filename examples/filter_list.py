import sys
from pprint import pprint

import inquirer  # noqa


args = sys.argv

if 'hint' in args:
    choices_hints = {k: f'{str(v)[:10]}...' for k,v in inquirer.__dict__.items()}
else:
    choices_hints = None

if 'autocomplete' in args:
    def autocomplete_func(_text, state):
        # Every time the user presses TAB, we'll switch to the next suggestion
        # The `state` variable contains the index of the current suggestion
        # We can wrap it around to the first suggestion if we reach the end
        # The suggestion are the filtered choices in this example
        l = list(filter_func(_text, choices))
        return l[state % len(l)] if l else _text
else:
    autocomplete_func = None

carousel =  True if 'carousel' in args else False
other = True if 'other' in args else False


choice_change = []
choices = list(inquirer.__dict__.keys())
choices.sort()

if 'tag' in args:
    choices = [(k,str(inquirer.__dict__[k])[:5]) for k in choices]


def filter_func(text, collection):
    return filter(lambda x: text in x, collection)


def callback_listener(item):
    choice_change.append(item)


questions = [
    inquirer.FilterList(
        "attribute",
        message="Select item ",
        choices=choices,
        carousel=carousel,
        other=other,
        hints= choices_hints,
        filter_func=filter_func,
        autocomplete=autocomplete_func,
        choice_callback=callback_listener,
    ),
]

answers = inquirer.prompt(questions)

print(choice_change)
pprint(answers)
