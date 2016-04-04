print 'Importing libraries...'
from urllib2 import urlopen
from json import load
import codecs

# Setting up global variables
clientID = '411CO5A2O0VN4ESDKMXEWIXD2XDY2SO2ZSPZVHW42L5IS2VX'
baseURL = 'https://api.foursquare.com/v2/venues/search?'
lat = 40.7
lon = -74
token = '2PESPAGVZLIA1QEKCQOGD0C1TLG1YI2ZWCWHHKCMJX2F1UQ0'
version = 20160404
limit = 50

# Building the request
request = baseURL + 'll=' + str(lat) + ',' + str(lon) + '&oauth_token=' + token + '&v=' + str(version) + '&limit=' + str(limit)

# Querying API
response = urlopen(request)
baseData = load(response)

# Parsing the API
response = baseData['response']
venues = response['venues']
for venue in venues:
	venueName = venue['name'].encode('utf-8')
	print venueName

print 'Done with everything...'