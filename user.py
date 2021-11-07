import spotipy
from spotipy import SpotifyClientCredentials, SpotifyOAuth, SpotifyImplicitGrant
import unifyInfo
import misc

class User:
    """A spotify user account"""
    username = "EMPTY"
    password = "EMPTY"
    saved_tracks = []
    saved_albums = []
    followed_artists = []
    playlists = []
    top_artists = []
    top_tracks = []
    session = ""
    
    def __init__(self, un="EMPTY", pw="EMPTY"):
        self.username = un 
        self.password = pw

        # Have user authorize Unify to dig
        unify_auth = SpotifyOAuth(unifyInfo.id, unifyInfo.secret, unifyInfo.redirect, 
            scope=unifyInfo.scope, 
            username=un,
            open_browser=True)
        #unify_auth = spotipy.util.prompt_for_user_token(un, unifyInfo.scope, unifyInfo.id, unifyInfo.secret, unifyInfo.redirect)
        sp = spotipy.Spotify(auth_manager=unify_auth)

        # Collect saved_albums
        results = sp.current_user_saved_albums()
        temp = misc.grabAll(results, sp)

        for a in temp:
            self.saved_albums.append(misc.albumToName(a))

        # Collect saved_tracks
        results = sp.current_user_saved_tracks()
        temp = misc.grabAll(results, sp) 

        for t in temp:
            self.saved_tracks.append(misc.trackToName(t))

        # Collect followed_artists
        results = sp.current_user_followed_artists()
        temp = misc.grabAllArtists(results, sp)

        for a in temp:
            self.followed_artists.append(misc.artistToName(a))

        # Collect playlist
        results = sp.current_user_playlists()
        temp = misc.grabAll(results, sp)

        for pl in temp:
            self.playlists.append(misc.playlistToName(pl))


        # Collect top_artists
        results = sp.current_user_top_artists()
        temp = misc.grabAll(results, sp)

        for a in temp:
            self.top_artists.append(misc.artistToName(a))

        # Collect top_songs
        results = sp.current_user_top_tracks()
        temp = misc.grabAll(results, sp)

        for t in temp:
            self.top_tracks.append(misc.artistToName(t))



#def test():
#    user1 = User("rribbsauce", "Hooplight1!")
#
#    for i in user1.top_tracks:
#       print(i)