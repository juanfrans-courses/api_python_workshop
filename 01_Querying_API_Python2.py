print 'Importing libraries...'
from urllib2 import urlopen, HTTPError
from json import load

# Setting up global variables
baseURL = 'https://api.foursquare.com/v2/venues/search?'
lat = 40.7
lon = -74
token = 'your token here'
version = 20161016
limit = 50

# Building the request
request = baseURL + 'll=' + str(lat) + ',' + str(lon) + '&oauth_token=' + token + '&v=' + str(version) + '&limit=' + str(limit)

# Querying API
try:
	response = urlopen(request)
	baseData = load(response)

	# Parsing the API
	response = baseData['response']
	venues = response['venues']
	for venue in venues:
		venueName = venue['name'].encode('utf-8')
		print venueName
except HTTPError:
	print 'There is a problem with the request...'

print 'Done with everything...'
