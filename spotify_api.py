import urllib

def search(query):
	escaped_query = urllib.quote(query)
	search_string = "https://api.spotify.com/v1/search?q=%s&type=track&market=us" % (escaped_query)
	r = requests.get(search_string)
	return r.json()['tracks']['items'][0]['external_urls']['spotify']
