from styles import TextAlign, TextTransformation
from build_context import BuildContext
from application import Application
from html_file import HtmlFile
from pytr_widgets import *

lorem_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'


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
                'GitHub': 'https://github.com/UcGeorge/Pytter'
            },
            child=Column(
                children=[
                    Text(
                        text='Rows and Columns',
                        style=TextStyle(
                            color=Color.black.value,
                            font_size=50,
                            letter_spacing=2
                        )  # TextStyle
                    ),  # Text
                    Row(
                        children=[
                            Text(
                                text=lorem_text,
                                style=TextStyle(
                                    color=Color.colors('#555'),
                                    font_size=20
                                )  # TextStyle
                            )  # Text
                        ]
                    ),  # Row
                    Row(
                        children=[
                            PaddedBox(
                                child=Text(
                                    text=lorem_text,
                                    style=TextStyle(
                                        color=Color.colors('#555'),
                                        font_size=20,
                                        text_align=TextAlign.justify.value
                                    )  # TextStyle
                                ),  # Text
                                padding=Padding(
                                    right=10
                                )  # Padding
                            ),  # PaddedBox
                            PaddedBox(
                                child=Text(
                                    text=lorem_text,
                                    style=TextStyle(
                                        color=Color.colors('#555'),
                                        font_size=20,
                                        text_align=TextAlign.justify.value
                                    )  # TextStyle
                                ),  # Text
                                padding=Padding(
                                    left=10
                                )  # Padding
                            )  # PaddedBox
                        ]  # list[Widget]
                    ),  # Row
                    Row(
                        children=[
                            PaddedBox(
                                child=Text(
                                    text=lorem_text,
                                    style=TextStyle(
                                        color=Color.colors('#555'),
                                        font_size=20,
                                        text_align=TextAlign.justify.value
                                    )  # TextStyle
                                ),  # Text
                                padding=Padding(
                                    right=10
                                )  # Padding
                            ),  # PaddedBox
                            PaddedBox(
                                child=Text(
                                    text=lorem_text,
                                    style=TextStyle(
                                        color=Color.colors('#555'),
                                        font_size=20,
                                        text_align=TextAlign.justify.value
                                    )  # TextStyle
                                ),  # Text
                                padding=Padding(
                                    left=10
                                )  # Padding
                            )  # PaddedBox
                        ]  # list[Widget]
                    ),  # Row
                ]  # list[Widget]
            )  # Column
        )  # MenuPage


my_app = Application(location='''D:\Documents\pyttr-test''')
index = LandingPage(file_name='index')

my_app.add_file(index)
