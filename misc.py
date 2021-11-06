import spotipy

def grabAll(results, session):
    if not 'items' in results:
        print("Tried to grabAll of something that isn't there")
        return results
    retval = results['items']

    if not 'next' in results:
        print("Parameter has only 1 page")
    while results['next']:
        results = session.next(results)
        retval.extend(results['items'])

    return retval

def grabAllArtists(results, session):
    if not 'artists' in results:
        print("grabAllArtists called on something weird")
        return results
    retval = results['artists']['items']

    if not 'next' in results:
        return retval
    while results['next']:
        results = session.next(results)
        retval.extend(results['artists']['items'])

    return retval

    

def albumToName(album):
    return album['album']['name']

def trackToName(album):
    return album['track']['name']

def artistToName(album):
    return album['name']

def playlistToName(pl):
    return pl['name']