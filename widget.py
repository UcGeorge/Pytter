from build_context import BuildContext


class Widget(object):
    "Base class for all widgets or elements"

    def __init__(self):
        self.context = BuildContext()
        self.html = self.build(self.context)

    def __repr__(self) -> str:
        return self.html

    def __str__(self):
        return self.html

    def build(self, context: BuildContext) -> str:

        return "<h1>Hello World</h1>"
