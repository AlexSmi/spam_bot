

class Message(object):
    def __init__(self, text, **options):
        self.text = text
        self.options = options


class Markdown(Message):
    def __init__(self, text, **options):
        super(Markup, self).__init__(text, parse_mode="Markdown", **options)


class HTML(Message):
    def __init__(self, text, **options):
        super(HTML, self).__init__(text, parse_mode="HTML", **options)