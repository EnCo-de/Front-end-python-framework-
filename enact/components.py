from . import elements

def html5(body='', css_file='', js_file=''): 
    return f'''<!DOCTYPE html>
<html>
  <head><link href="{css_file}" rel="stylesheet" /></head>
  <body>
    {body.replace('\n','\n    ')}
  <script src="{js_file}"></script>
  </body>
</html>'''


class Component:
    def __init__(self):
        self.node = 'node'
    
    def __str__(self) -> str:
        return str(self.node)


class Card(Component):
    def __init__(self, title='Card title', img_src='', img_alt='', description='Some information about the item.', *args, **kwargs):
        self.title = title
        self.img_src=img_src
        self.img_alt=img_alt
        self.description=description

        self.node = elements.Div(
            elements.Img(arg_str='width="95%" style="margin: 0 auto; display: block;"', src=img_src, alt=img_alt),
            elements.H1(title, arg_str='style="text-align:center;"'),
            elements.Pgf(description), 
            arg_str='style="width: 45%; max-width: 250px; margin:1cm; padding:.5cm; background-color:azure; border-radius:.4cm;"'
            )


def navbar(links: dict, logo_url: str = None):
    lis = [elements.Anch(value, key) for key, value in links.items()]
    ul = elements.Ul(*lis, arg_str='style="list-style-type: none; margin: 0; padding: 0;"')
    if logo_url is None:
        node = elements.Nav(ul, arg_str='class="navbar"')
    else:
        node = elements.Nav(elements.Img(
            f'src={logo_url} height="50px" alt="logo"'), 
            ul, 
            arg_str='class="navbar"'
            )
    return str(node)

def hero(title='Hero title', img_src='', description='Some information about the item.'):
    node = elements.Div(
            elements.H1(title),
            elements.Pgf(description), 
            arg_str=f'class="hero" style="--background: url({img_src});"'
            )
    return str(node)
