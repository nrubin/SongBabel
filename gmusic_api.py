if __name__ == "__main__":
    import pprint

from gmusicapi import Mobileclient
from secrets import username, password

api = Mobileclient()
logged_in = api.login(username, password, Mobileclient.FROM_MAC_ADDRESS)
if not logged_in:
    raise Exception('Bad gmail credentials')

def search(query):
    song_results = api.search_all_access('lil dicky')['song_hits']
    return song_results[0]

if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(search("Lil Dicky"))