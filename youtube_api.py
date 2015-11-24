from secrets import youtube_api_key
if __name__ == '__main__':
	from song import Song
	import urllib
	import requests

def search(query):
	escaped_query = urllib.quote(query)
	base_url = "https://www.googleapis.com/youtube/v3/search?type=video&order=relevance&part=snippet&key=" + youtube_api_key + "&q="
	search_string = base_url + escaped_query
	r = requests.get(search_string)
	first_result = r.json()['items'][0]
	title = first_result['snippet']['title']
	song_id = first_result['id']['videoId']
	s = Song(title,None, None)
	s.add_youtube_id(song_id)
	return s