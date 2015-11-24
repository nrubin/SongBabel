# songbabel.gmusic@gmail.com
# !Q@W3e4r
from ghost import Ghost

ghost = Ghost()

page, extra_resources = ghost.open("http://jeanphi.fr")
assert page.http_Status==200 and 'jeanphix' in ghost.content