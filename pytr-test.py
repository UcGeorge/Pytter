from widget import Widget
from build_context import BuildContext
from application import Application
from html_file import HtmlFile
from pytr_widgets import *


class Index(HtmlFile):

    def build(self, context: BuildContext) -> str:
        return Page(
            child=Widget()
        )


my_app = Application(location='''D:\Documents\pyttr-test''')
index = Index(file_name='index')

my_app.add_file(index)
