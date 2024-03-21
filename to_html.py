import os
from enact.components import Card, html5, navbar, hero
from enact.elements import Flex

# example use case
nav_links = {
    'index': '#',
    'python': 'https://www.python.org/',
    'pep-8': 'https://peps.python.org/pep-0008/',
    'f-strings': 'https://peps.python.org/pep-0701/'
}
nav = navbar(nav_links)

new_card = Card(
                title='Altea', 
                img_src='https://i.pinimg.com/736x/4a/21/82/4a218232896756f33cbfe54b39aa45a0.jpg', 
                description='Discover the charm of Altea, a picturesque town with stunning coastal views and colorful streets. Plan your visit to Altea and immerse yourself in its rich culture and breathtaking scenery.'
                )
cards = Flex(*(new_card for _ in range(5)))

header = hero(
    title='Top Tourist Destinations',
    img_src='https://images.wallpapersden.com/image/wl-mountain-peak-sky_16234.jpg',
    description="Let's Get Started"
)

footer = '<footer class="footer">Beautiful and elegant CSS footer design with a logo placeholder, menu items and icon list. The design also contains an attractive minimal background.</footer>'
body =  nav + header + str(cards) + footer
page = html5(body, 'styles.css')

folder = os.path.dirname(__file__)
with open(os.path.join(folder,'example.html'), 'w') as f:
    f.write(page)

print('Saved in \t', folder.replace('\\', '/'), '/example.html', sep='')
