from build_context import BuildContext
from widget import Widget


class HtmlFile(Widget):

    def __init__(self, file_name='index'):
        super().__init__()

        self.file_name = file_name
        self.html = str(self.build(BuildContext()))

    def __repr__(self) -> str:
        return self.html

    def __str__(self):
        return self.html

    def build(self, context: BuildContext) -> str:
        return Widget()
