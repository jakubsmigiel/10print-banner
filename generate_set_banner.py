import requests
import tenprint_gradient
from io import BytesIO

OAUTH_TOKEN = 'OAUTH_TOKEN' # OAuth token to access your account through the Pleroma API

base_url = 'https://example.com' # The base URL of the Pleroma instance

# The list of color palettes. It contains tuples, where the first two elements 
# of each tuple are the colors for the background gradient and the last two are
# the foreground (slashes) gradient colors.
# I put them in separate lists grouped by the 4 colors they use so that there is an equal 
# probability of getting each 4-color scheme. And only then the color tuple is picked, 
# determining the orientations of the gradients.
palettes = [
    [
        (0xef5d60,0xec4067,0xa01a7d,0x311847),
    ],
    [
        (0x0a1128,0x001f54,0x034078,0x1282a2),
    ],
    [
        (0x212d40,0x11151c,0xb9314f,0xedddd4),
    ],
    [
        (0x191d32,0x282f44,0x453a49,0x6d3b47),
    ],
    [
        (0x0b3c49,0x731963,0xfffdfd,0xcbd2d0),
        (0x0b3c49,0x731963,0xcbd2d0,0xfffdfd),
        (0x731963,0x0b3c49,0xcbd2d0,0xfffdfd),
        (0x731963,0x0b3c49,0xfffdfd,0xcbd2d0)
    ],
    [
        (0xfffdfd,0xcbd2d0,0x0b3c49,0x731963),
        (0xcbd2d0,0xfffdfd,0x0b3c49,0x731963),
        (0xcbd2d0,0xfffdfd,0x731963,0x0b3c49),
        (0xfffdfd,0xcbd2d0,0x731963,0x0b3c49)
    ]
]


print('Picking palette')
palette_index, palette_orientation, palette = tenprint_gradient.get_random_palette(palettes)
print(f'Using palette {palette_index}/{palette_orientation} - {palette}')

print('Generating banner')
# This will generate a banner 31 cells wide, 11 cells tall, with each cell being 100 by 100 pixels, and with 0 margin
banner_image = tenprint_gradient.generate_gradiented_10print(31, 11, 100, 0, palette)

print('Getting banner bytes')
banner_bytes = None
with BytesIO() as output:
    banner_image.save(output, 'PNG')
    banner_bytes = output.getvalue()

print(f'Requesting banner update at {base_url}')
response = requests.patch(f'{base_url}/api/v1/accounts/update_credentials', files={
    'header': banner_bytes
}, headers={'Authorization': f'Bearer {OAUTH_TOKEN}'})

print('Response')
print(response.text)
