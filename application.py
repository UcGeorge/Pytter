from html_file import HtmlFile
import os


class Application:
    def __init__(self, location):
        self.location = location

    def add_file(self, *html_files: HtmlFile):

        for html_file in html_files:
            html_string = str(html_file)
            file_name = html_file.file_name

            with open(self.location + f'''\{file_name}.html''', 'w', encoding='utf-8') as file:
                file.write(html_string)
