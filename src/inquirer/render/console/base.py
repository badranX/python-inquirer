from blessed import Terminal

import inquirer


# Should be odd number as there is always one question selected
MAX_OPTIONS_DISPLAYED_AT_ONCE = 13
half_options = int((MAX_OPTIONS_DISPLAYED_AT_ONCE - 1) / 2)


class BaseConsoleRender:
    title_inline = False

    def __init__(self, question, theme=None, terminal=None, show_default=False, choice_call_back=None, filter_func=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.question = question
        self.terminal = terminal or Terminal()
        self.answers = {}
        self.theme = theme
        self.show_default = show_default
        self.choice_call_back = choice_call_back or (lambda x: None)
        def filter_test(text, choices):
            from fuzzyfinder import fuzzyfinder
            choices = fuzzyfinder(text, choices, accessor=lambda x: str(x))
            #if text == '':
            #    return None
            with open('logs.txt', 'w') as f:
                f.write(str(choices))
            return list(choices)
            return list(choices)[:3]
        self.filter_func = filter_func or filter_test

    def other_input(self):
        other = inquirer.text(self.question.message, autocomplete=self.question.autocomplete)
        return other

    def get_header(self):
        return self.question.message

    def get_hint(self):
        return ""

    def get_current_value(self):
        return ""

    def get_options(self):
        return []

    def process_input(self, pressed):
        raise NotImplementedError("Abstract")

    def handle_validation_error(self, error):
        if error.reason:
            return error.reason

        ret = f'"{error.value}" is not a valid {self.question.name}.'
        try:
            ret.format()
            return ret
        except (ValueError, KeyError):
            return f"Entered value is not a valid {self.question.name}."
