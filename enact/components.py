import elements

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


# example use case
new_card = Card(
                'Altea', 
                'https://i.pinimg.com/736x/4a/21/82/4a218232896756f33cbfe54b39aa45a0.jpg', 
                description='Discover the charm of Altea, a picturesque town with stunning coastal views and colorful streets. Plan your visit to Altea and immerse yourself in its rich culture and breathtaking scenery.'
                )
print('\n',new_card)

cards = elements.Flex(*(new_card for _ in range(20)))
cards_html = '<html><head></head><body>' + str(cards) + '</body></html>'
print('\n',cards_html)


import os

folder = os.path.dirname(__file__)
with open(os.path.join(folder,'example.html'), 'w') as f:
    f.write(cards_html)

print('Saved in ', folder)
