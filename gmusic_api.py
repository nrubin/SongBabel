if __name__ == "__main__":
    import pprint

from gmusicapi import Mobileclient
from secrets import username, password
from song import Song

api = Mobileclient()
logged_in = api.login(username, password, Mobileclient.FROM_MAC_ADDRESS)
if not logged_in:
    raise Exception('Bad gmail credentials')

def search(query):

    result = api.search_all_access('lil dicky')['song_hits'][0]['track']
    s = Song(result['title'], result['artist'], result['album'])
    s.add_gmusic_id(result['nid'])
    s.add_gmusic_video_id(result['primaryVideo']['id'])
    return s

if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)
    s = search("Lemme Freak")
    print s.gmusic_video_id
    print s.gmusic_id
    print s.get_gmusic_url()