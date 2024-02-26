import json

from pypresence import Presence
from time import time 

with open('config.json', mode='r', encoding='utf-8') as f:
    config = json.load(f)

#Чтобы сделать название приложения, нужно зайди в https://discord.com/developers/applications, создать приложение, назвать его и добавить картинки.
RPC = Presence(client_id=config['id']) 
RPC.connect()


buttons = [
    {
        'label': 'My Server',
        'url': 'https://discord.gg/********'
    },
    {
        'label': 'My Telegram',
        'url': 'https://t.me/********'
    }
]

RPC.update(
	state='State',
	details='Wow',
	start=time(),
	buttons=buttons,
	large_image='Large_image',
	small_image='Small_image',
	large_text='Your text',
	small_text='Small text'
)
''

while 1:
    time.sleep(15)