from styles import TextTransformation
from build_context import BuildContext
from application import Application
from html_file import HtmlFile
from pytr_widgets import *


class LandingPage(HtmlFile):

    def build(self, context: BuildContext) -> str:
        return MenuPage(
            title='Pytter test page',
            toogle=Text(
                text='Menu',
                style=TextStyle(
                    color=Color.colors('#04AA6D'),
                    transformation=TextTransformation.uppercase.value,
                    letter_spacing=1.5,
                    font_size=20
                )  # TextStyle
            ),  # Text
            nav_links={
                'GitHub': 'https://github.com/UcGeorge/Pytter',
                'Services': 'https://github.com/UcGeorge/Pytter',
                'Clients': 'https://github.com/UcGeorge/Pytter',
                'Contacts': 'https://github.com/UcGeorge/Pytter'
            },
            child=Text(
                text='Pytter demo page',
                style=TextStyle(
                    color=Color.black.value,
                    font_size=50,
                    letter_spacing=2
                )  # TextStyle
            )  # Text
        )  # MenuPage


my_app = Application(location='''D:\Documents\pyttr-test''')
index = LandingPage(file_name='index')

my_app.add_file(index)
