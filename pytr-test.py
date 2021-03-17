from styles import TextAlign, TextTransformation, EdgeInsetsProperty
from build_context import BuildContext
from application import Application
from html_file import HtmlFile
from pytr_widgets import *

lorem_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
title_text = 'Pytter - Box'


def page_title() -> Widget:
    return Text(
        text=title_text,
        style=TextStyle(
            color=Color.black.value,
            font_size=50,
            letter_spacing=2
        )  # TextStyle
    )  # Text


def paragraph_row() -> Widget:
    return Row(
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
                padding=EdgeInsets(
                    property=EdgeInsetsProperty.padding.value,
                    left=10,
                    right=10
                )
            ),
            PaddedBox(
                child=Text(
                    text=lorem_text,
                    style=TextStyle(
                        color=Color.colors('#555'),
                        font_size=20,
                        text_align=TextAlign.justify.value
                    )  # TextStyle
                ),  # Text
                padding=EdgeInsets(
                    property=EdgeInsetsProperty.padding.value,
                    left=10,
                    right=10
                )
            )
        ]
    )


def paragraph_col() -> Widget:
    return Column(
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
                padding=EdgeInsets(
                    property=EdgeInsetsProperty.padding.value,
                    left=10,
                    right=10
                )
            ),
            PaddedBox(
                child=Text(
                    text=lorem_text,
                    style=TextStyle(
                        color=Color.colors('#555'),
                        font_size=20,
                        text_align=TextAlign.justify.value
                    )  # TextStyle
                ),  # Text
                padding=EdgeInsets(
                    property=EdgeInsetsProperty.padding.value,
                    left=10,
                    right=10
                )
            )
        ]
    )


def paragraph() -> Widget:
    return PaddedBox(
        child=Text(
            text=lorem_text,
            style=TextStyle(
                color=Color.colors('#555'),
                font_size=20,
                text_align=TextAlign.justify.value
            )  # TextStyle
        ),  # Text
        padding=EdgeInsets(
            property=EdgeInsetsProperty.padding.value,
            left=10,
            right=10)
    )


def toogle_widget() -> Widget:
    return Text(
        text='Menu',
        style=TextStyle(
            color=Color.colors('#04AA6D'),
            transformation=TextTransformation.uppercase.value,
            letter_spacing=1.5,
            font_size=20
        )  # TextStyle
    )


def box(color: Color = Color.colors('#111')) -> Widget:
    return Box(
        width=Length.percent(100),
        height=Length.px(100),
        box_style=BoxStyle(
            background_color=color
        )
    )


class LandingPage(HtmlFile):

    def build(self, context: BuildContext) -> str:
        return MenuPage(
            title='Pytter test page',
            toogle=toogle_widget(),
            nav_links={
                'GitHub': 'https://github.com/UcGeorge/Pytter'
            },
            child=Column(
                width=Length.percent(100),
                children=[
                    page_title(),
                    Column(
                        children=[
                            Row(
                                children=[
                                    box() if i % 2 == 0 else box(Color.transparent.value) for i in range(10)
                                ]  # list[Widget]
                            )  # Row
                            if i % 2 == 0 else
                            Row(
                                children=[
                                    box() if i % 2 != 0 else box(Color.transparent.value) for i in range(10)
                                ]  # list[Widget]
                            )  # Row
                            for i in range(10)]  # list[Widget]
                    )  # Column
                ]  # list[Widget]
            )  # Column
        )  # MenuPage


my_app = Application(location='''D:\Documents\pyttr-test''')
index = LandingPage(file_name='index')

my_app.add_file(index)
