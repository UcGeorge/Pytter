import enum


class Style(object):

    def __init__(self):
        self.css = ''
        pass

    def __repr__(self) -> str:
        return self.css

    def __str__(self) -> str:
        return self.css


class Color(enum.Enum):
    black = '#000'
    white = '#FFF'
    transparent = 'rgba(0,0,0,0)'

    def colors(color='#FFF') -> 'Color':
        return color

    def with_opacity(color: 'Color' = '#FFF', opacity: float = 1.0):

        return f"{color}; opacity:{opacity}"


class FontWeight(enum.Enum):
    bold = 'bold'
    normal = 'normal'


class TextDecoration(enum.Enum):
    none = 'none'
    overline = 'overline'
    line_through = 'line-through'
    underline = 'underline'


class TextTransformation(enum.Enum):
    none = 'none'
    uppercase = 'uppercase'
    lowercase = 'lowercase'
    capitalize = 'capitalize'


class VerticalAlign(enum.Enum):
    center = 'middle'
    top = 'top'
    bottom = 'bottom'


class TextAlign(enum.Enum):
    center = 'center'
    left = 'left'
    right = 'right'
    justify = 'justify'


class TextDirection(enum.Enum):
    right_to_left = 'rtl'
    left_to_right = 'ltr'


class TextStyle(Style):

    def __init__(
            self,
            color: Color = Color.black.value,
            font_size: float = 15.0,
            letter_spacing: float = 1.0,
            background_color: Color = Color.transparent.value,
            font_weight: FontWeight = FontWeight.normal.value,
            decoration: TextDecoration = TextDecoration.none.value,
            transformation: TextTransformation = TextTransformation.none.value,
            text_align: TextAlign = TextAlign.left.value,
            vertical_align: VerticalAlign = VerticalAlign.center.value,
            direction: TextDirection = TextDirection.left_to_right.value,
            text_indent: float = 0,
            line_height: float = 1.1,
            word_spacing: float = 5,
            shadow: str = 'none'
            # TODO Add text-overflow property.
    ):
        self.style = {
            'color': color,
            'font-size': str(font_size) + 'px',
            'letter-spacing': str(letter_spacing) + 'px',
            'background-color': background_color,
            'font-weight': font_weight,
            'text-decoration': decoration,
            'text-transform': transformation,
            'text-align': text_align,
            'vertical-align': vertical_align,
            'direction': direction,
            'text-indent': str(text_indent) + 'px',
            'line-height': str(line_height),
            'word-spacing': str(word_spacing) + 'px',
            'text-shadow': shadow,
            'unicode-bidi': 'bidi-override'
        }
        self.css = ''
        for property, value in self.style.items():
            self.css += f'{property}:{value};'


class EdgeInsetsProperty(enum.Enum):
    padding = 'padding'
    margin = 'margin'


class Length(enum.Enum):
    MAX = '100%'
    def percent(x: float): return f'{x}%'
    def px(x: float): return f'{x}px'


class EdgeInsets(Style):
    def __init__(
        self,
        property: EdgeInsetsProperty = EdgeInsetsProperty.padding.value,
        top: Length = Length.px(0),
        right: Length = Length.px(0),
        bottom: Length = Length.px(0),
        left: Length = Length.px(0),
    ):
        self.css = f'{property}-top:{top};{property}-right:{right};{property}-bottom:{bottom};{property}-left:{left};'


class BoxStyle(Style):
    def __init__(
        self,
        color: Color = Color.white.value,
        background_color: Color = Color.black.value
    ):
        self.css = f'color:{color};background-color:{background_color};'
