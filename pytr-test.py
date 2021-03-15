from build_context import BuildContext
from application import Application
from html_file import HtmlFile
from web_page import WebPage


class Index(HtmlFile):

    def build(self, context: BuildContext) -> str:
        return WebPage()


my_app = Application(location='''D:\Documents\pyttr-test''')

index = Index(file_name='index')
contacts = Index(file_name='contacts')

my_app.add_file(index, contacts)
