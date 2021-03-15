from widget import Widget
from build_context import BuildContext
from html_meta import (HtmlVersion, Lang, Charset)


class WebPage(Widget):

    def __init__(
            self,
            html_version=HtmlVersion.HTML5,
            lang=Lang.EN,
            charset=Charset.UTF_8,
            child=Widget()):

        # super().__init__()
        self.html_version = html_version
        self.lang = lang
        self.charset = charset
        self.child = child
        self.context = BuildContext()
        self.html = self.build(self.context)

    def __repr__(self):
        return self.html

    def __str__(self):
        return self.html

    def build(self, context: BuildContext) -> str:

        return f'''
            <!DOCTYPE html>
            <html lang="{self.lang}">
            <head>
                <meta charset="{self.charset}">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>
            <body>
                {self.child}
            </body>
            </html>
        '''
