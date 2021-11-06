import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

client_id = "b1ea5a3ed14042f0a469349ffde84652"
client_secret = "0459a4f8100746ddb52ac4eab93725f6"
redirect_uri = "http://localhost:8888/callback"
saba_uri= "spotify:artist:7Hjbimq43OgxaBRpFXic4x"
scope = "user-library-read"
client_credentials_man = SpotifyClientCredentials(client_id, client_secret)
auth_manager = SpotifyOAuth(client_id, client_secret, redirect_uri, scope=scope)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_man, auth_manager=auth_manager)
results = sp.current_user_saved_albums()
my_albums = results['items']

# Since current_user_saved_albums() can only return x amount of 
# items at a time, it stores a 'next' item that holds the url
# of the 'next page' of items
while results['next']:
    results = sp.next(results)
    my_albums.extend(results['items'])

for a in my_albums:
    print(a['album']['name'])

resuls = sp.cur

#saba = sp.artist(saba_uri)
#print("The artist", saba["name"], "has released the following albums:")
#results = sp.artist_albums(saba_uri, album_type='album')
#saba_albums = results["items"]
#
#while results['next']:
#    results = sp.next(results)
#    saba_albums.extend(results['items'])
#
#for a in saba_albums:
#    print(a['name'])
