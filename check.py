##did not make this lol
    
import os
import requests
os.environ['STDLIB_SECRET_TOKEN'] = 'MTEwMTA5MjIwMTY2MTk4ODkyNQ.GeMaSh.bhVqTh3kAeanO0KjKpQl3oQfwfFhMDuKZCUO6o'

headers = {
    'Authorization': f'Bearer {os.environ["STDLIB_SECRET_TOKEN"]}',
    'Content-Type': 'application/json'
}

payload = {
    'channel_id': 1101092440968011826/1101092440968011830,
    'content': '',
    'tts': False,
    'embeds': [
        {
            'type': 'rich',
            'title': 'RezaGator - The Ultimate Hosting Solution',
            'description': 'Looking for a hosting service that doesn\'t make you choose between speed, security, and affordability? Rezagator has got your back! Our services are optimized to give you the best of all worlds. Your website will run like a cheetah on caffeine, while our security measures keep you and your data safe from harm. And with plans that fit any budget, you won\'t have to sell a kidney to afford it.\n\nOur support team is made up of hosting gurus who are available 24/7 to help with any questions you may have. They\'re like your own personal IT department, but without the awkward water cooler conversations.\n\nSo why settle for mediocre hosting when you can have it all with Rezagator? Upgrade today and let your website be the envy of the internet!',
            'color': 0xff00e6,
            'image': {
                'url': 'https://media.discordapp.net/attachments/1097087296978825306/1101088779177054260/standard_1.gif',
                'height': 0,
                'width': 0
            },
            'footer': {
                'text': 'Visit RezaGator.Cloud',
                'icon_url': 'https://media.discordapp.net/attachments/963381981213786132/1085796822716518411/party.png'
            },
            'url': 'http://rezagator.cloud/'
        }
    ]
}
channel_id = 1101092440968011826/1101092440968011830
response = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages'.format(payload['channel_id']), headers=headers, json=payload)
response.raise_for_status()
