import urllib
import requests
if __name__ == '__main__':
	from song import Song

def search(query):
	escaped_query = urllib.quote(query)
	search_string = "https://api.spotify.com/v1/search?q=%s&type=track&market=us" % (escaped_query)
	r = requests.get(search_string)
	first_result = r.json()['tracks']['items'][0]
	title = first_result['name']
	artist = first_result['artists'][0]['name']
	album = first_result['album']['name']
	id = first_result['id']
	url = first_result['external_urls']['spotify']
	s = Song(title,artist,album)
	s.add_spotify_id(id)
	s.add_spotify_url(url)
	return s