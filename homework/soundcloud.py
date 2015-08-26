Soundcloud: Question: 

import soundcloud

client = soundcloud.Client(client_id=968035528374afb6797dca3eada16af5)

track = client.get('/resolve', url='http://soundcloud.com/forss/flickermood')

print track.id