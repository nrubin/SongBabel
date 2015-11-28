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

	def add_youtube_id(self,an_id):
		self.youtube_id = an_id
	
	def add_gmusic_id(self,an_id):
		self.gmusic_id = an_id

	def get_gmusic_url(self):
		return 'https://play.google.com/music/m/' + self.gmusic_id

	def add_gmusic_video_id(self,an_id):
		self.gmusic_video_id = an_id

	def __repr__(self):
		return self.name

	def serialize(self):
		return {
			'name' : self.name,
			'artist' : self.artist,
			'album' : self.artist,
			'spotify_data' : {
				'id':self.__dict__.get('spotify_id',''),
				'url':self.__dict__.get('spotify_url','')
			},
			'itunes_data' : {
				'id':self.__dict__.get('itunes_id',''),
				'url':self.__dict__.get('itunes_url','')
			},
			'youtube_data' : {
				'id':self.__dict__.get('youtube_id','')
			},
			'gmusic_data' : {
				'id':self.__dict__.get('gmusic_id',''),
				'url':self.get_gmusic_url(),
				'video_id':self.__dict__.get('gmusic_video_id','')
			}
		}