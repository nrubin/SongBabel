import requests
import json
import os
from flask import Flask, Response, request, jsonify


import spotify_api as spotify

app = Flask(__name__, static_url_path='', static_folder='.')
app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))



@app.route('/spotify_search', methods=['POST'])
def spotify_search():
	query = request.form['query']
	print query
	result = spotify.search(query)
	return jsonify({'result':result})

if __name__ == '__main__':
    try:
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port, debug=True)
    except Exception as e:
        app.logger.debug("%s"%e)