class Song(object):
	def __init__(self,name, artist, album):
		self.name = name
		self.artist = artist
		self.album = album

	def add_spotify_id(self,an_id):
		self.spotify_id = an_id

	def add_spotify_url(self,url):
		self.spotify_url = url

	def add_itunes_id(self,an_id):
		self.itunes_id = an_id

	def add_itunes_url(self,url):
		self.itunes_url = url

	def __repr__(self):
		return self.name