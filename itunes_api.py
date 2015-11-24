import requests

r = requests.get("https://itunes.apple.com/search?lang=en-us&term=jack%20johnson")

print r.text