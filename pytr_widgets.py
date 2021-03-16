from styles import Color, Padding, TextStyle
from typing import Dict
from widget import Widget
from build_context import BuildContext
from html_meta import (HtmlVersion, Lang, Charset)


class Page(Widget):

    def __init__(
        self,
        html_version: HtmlVersion = HtmlVersion.HTML5,
        lang: Lang = Lang.EN,
        charset: Charset = Charset.UTF_8,
        title: str = 'Page',
        child: Widget = Widget()
    ):

        # super().__init__()
        self.html_version = html_version
        self.lang = lang
        self.charset = charset
        self.child = child
        self.title = title
        self.context = BuildContext()
        self.html = self.build(self.context)

    def build(self, context: BuildContext) -> str:

        return f'''
            <!DOCTYPE html>
            <html lang="{self.lang}">
            <head>
                <meta charset="{self.charset}">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>{self.title}</title>
            </head>
            <body>
                {self.child}
            </body>
            </html>
                    '''


class MenuPage(Widget):

    def __init__(
        self,
        html_version: HtmlVersion = HtmlVersion.HTML5.value,
        lang: Lang = Lang.EN.value,
        title: str = 'Document',
        nav_links: 'Dict[str:str]' = {
            'About': '#',
            'Services': '#',
            'Clients': '#',
            'Contact': '#'
        },
        toogle: Widget = 'open',
        child: Widget = Widget(),
        background_color: Color = Color.colors('#111'),
        charset: Charset = Charset.UTF_8.value,
    ):

        # super().__init__()
        self.html_version = html_version
        self.lang = lang
        self.charset = charset
        self.title = title
        self.nav_links = ''.join(
            [f'''<a href="{href}">{key}</a>\n''' for key, href in nav_links.items()])
        self.toogle = toogle
        self.child = child
        self.background_color = background_color
        self.context = BuildContext()
        self.html = self.build(self.context)

    def build(self, context: BuildContext) -> str:

        return f'''
            <!DOCTYPE html>
            <html lang="{self.lang}">
            <head>
                <meta charset="{self.charset}">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>{self.title}</title>
            </head>

            <body>
                <div id="mySidenav" class="sidenav">
                    <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
                    {self.nav_links}
                </div>

                <!-- Use any element to open the sidenav -->
                <span onclick="openNav()">{self.toogle}</span>

                <!-- Add all page content inside this div if you want the side nav to push page content to the right (not used if you only want the sidenav to sit on top of the page -->
                <div id="main">
                    {self.child}
                </div>
                <style>
                    /* The side navigation menu */
                    
                    .sidenav {{
                        height: 100%;
                        /* 100% \Full-height */
                        width: 0;
                        /* 0 width - change this with JavaScript */
                        position: fixed;
                        /* Stay in place */
                        z-index: 1;
                        /* Stay on top */
                        top: 0;
                        /* Stay at the top */
                        left: 0;
                        background-color: {self.background_color};
                        /* Black*/
                        overflow-x: hidden;
                        /* Disable horizontal scroll */
                        padding-top: 60px;
                        /* Place content 60px from the top */
                        transition: 0.5s;
                        /* 0.5 second transition effect to slide in the sidenav */
                    }}
                    /* The navigation menu links */
                    
                    .sidenav a {{
                        padding: 8px 8px 8px 32px;
                        text-decoration: none;
                        font-size: 25px;
                        color: #818181;
                        display: block;
                        transition: 0.3s;
                    }}
                    /* When you mouse over the navigation links, change their color */
                    
                    .sidenav a:hover {{
                        color: #f1f1f1;
                    }}
                    /* Position and style the close button (top right corner) */
                    
                    .sidenav .closebtn {{
                        position: absolute;
                        top: 0;
                        right: 25px;
                        font-size: 36px;
                        margin-left: 50px;
                    }}
                    /* Style page content - use this if you want to push the page content to the right when you open the side navigation */
                    
                    #main {{
                        transition: margin-left .5s;
                        padding: 20px;
                    }}
                    /* On smaller screens, where height is less than 450px, change the style of the sidenav (less padding and a smaller font size) */
                    
                    @media screen and (max-height: 450px) {{
                        .sidenav {{
                            padding-top: 15px;
                        }}
                        .sidenav a {{
                            font-size: 18px;
                        }}
                    }}
                </style>
                <script>
                    /* Set the width of the side navigation to 250px and the left margin of the page content to 250px and add a black background color to body */
                    function openNav() {{
                        document.getElementById("mySidenav").style.width = "250px";
                        document.getElementById("main").style.marginLeft = "250px";
                        document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
                    }}

                    /* Set the width of the side navigation to 0 and the left margin of the page content to 0, and the background color of body to white */
                    function closeNav() {{
                        document.getElementById("mySidenav").style.width = "0";
                        document.getElementById("main").style.marginLeft = "0";
                        document.body.style.backgroundColor = "white";
                    }}
                </script>
            </body>
            </html>
                    '''


class Text(Widget):

    def __init__(
        self,
        text: str,
        style: TextStyle = TextStyle(),
    ):
        self.text = text
        self.style = style
        self.context = BuildContext()
        self.html = self.build(self.context)

    def build(self, context: BuildContext) -> str:
        return f'''<p style="{self.style}">{self.text}</p>'''


class Column(Widget):
    def __init__(
        self,
        children: 'list[Widget]' = [Widget()],
        style: TextStyle = TextStyle(),
    ):
        self.children = ''.join([f'<tr>{widget}</tr>' for widget in children])
        self.style = style
        self.context = BuildContext()
        self.html = self.build(self.context)

    def build(self, context: BuildContext) -> str:
        return f'''
            <table style="height:100%">
                {self.children}
            </table>
        '''


class Row(Widget):
    def __init__(
        self,
        children: 'list[Widget]' = [Widget()],
        style: TextStyle = TextStyle(),
    ):
        self.children = ''.join([f'<td>{widget}</td>' for widget in children])
        self.style = style
        self.context = BuildContext()
        self.html = self.build(self.context)

    def build(self, context: BuildContext) -> str:  # {self.style}
        return f'''
            <table style="width:100%">
            <tr>
                {self.children}
            </tr>
            </table>
        '''


class PaddedBox(Widget):
    def __init__(
        self,
        child: Widget = Widget(),
        padding: Padding = Padding(),
    ):
        self.child = child
        self.padding = padding
        self.context = BuildContext()
        self.html = self.build(self.context)

    def build(self, context: BuildContext) -> str:
        return f'''
            <div style="{self.padding}">
            {self.child}
            </div>
        '''
