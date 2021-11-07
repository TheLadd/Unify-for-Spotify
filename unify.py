import user

class Unify:
    """An object class that finds the similarities"""
    user1 = None
    user2 = None

    def __init__(self, u1, u2):
        self.user1 = u1
        self.user2 = u2

    def sharedFavoriteArtists():
        retval = {}     # Using a dict so that O(n^2) instead of O(n^3)
        for i in self.user1.top_artists:
            for j in self.user2.top_artists:
                if i == j and i not in retval: retval[i] = i
        return retval

    def sharedFavoriteTracks():
        retval = {}     
        for i in user1.top_tracks:
            for j in user2.top_tracks:
                if i == j and i not in retval: retval[i] = i
        return retval
    
    def weightedArtist(boo):
        """
        Where parameter is a boolean;
                true: weight user1's favorite
                false: weight user2's favortie
        """
        retval = {}

        if boo: 
            favor = self.user1
            unfavor = self.user2
        else: 
            favor = self.user2
            unfavor = self.user1

        for i in favor.top_artists:
            for j in unfavor.artists: 
                if i == j and i not in retval: retval[i] = 1
        return retval

    def weightedTracks(boo):
        """
        Where parameter is a boolean;
                true: weight user1's favorite
                false: weight user2's favortie
        """
        retval = {}

        if boo: 
            favor = self.user1
            unfavor = self.user2
        else: 
            favor = self.user2
            unfavor = self.user1

        for i in favor.top_tracks:
            for j in unfavor.saved_tracks: 
                if i == j and i not in retval: retval[i] = 1
        return retval

    def shared_artists(self):
        retval = {}
        for i in self.user1.followed_artists:
            for j in self.user2.followed_artists: 
                if i == j: 
                    retval[i] = 1
        return retval

