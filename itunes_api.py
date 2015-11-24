import requests
from song import Song
import urllib


def search(query):
	escaped_query = urllib.quote(query)
	search_string = "https://itunes.apple.com/search?lang=en-us&term=%s" % (escaped_query)
	r = requests.get(search_string)
	first_result = r.json()['results'][0]
	s = Song(first_result['trackName'], first_result['artistName'], first_result['collectionName'])
	s.add_itunes_url(first_result['trackViewUrl'])
	s.add_itunes_id(first_result['trackId'])	
	return s
