print 'Importing libraries...'
from urllib2 import urlopen, HTTPError
from json import load
import csv
import time

# Setting up global variables
baseURL = 'https://api.foursquare.com/v2/venues/search?'
lat = 40.7
lon = -74
token = 'your token here'
version = 20160404
limit = 50

# Open base file
with open('Base_Points.csv', 'rb') as basePoints:
	reader = csv.reader(basePoints, delimiter = ',')
	baseList = list(reader)
# for point in baseList:
# 	print point

# Create output file
output = open('FoursquareVenues.csv', 'wb')
output.write('Name\tLatitude\tLongitude\tCategory\tCheckins\n')

# Building the request
for point in baseList[1:]:
	longitude = point[0]
	latitude = point[1]
	request = baseURL + 'll=' + str(latitude) + ',' + str(longitude) + '&oauth_token=' + token + '&v=' + str(version) + '&limit=' + str(limit)

	# Querying API
	try:
		response = urlopen(request)
		baseData = load(response)

		# Parsing the API
		response = baseData['response']
		venues = response['venues']
		for venue in venues:
			venueName = venue['name'].encode('utf-8')
			venueLat = venue['location']['lat']
			venueLon = venue['location']['lng']
			venueCategories = venue['categories']
			if len(venueCategories) > 0:
				venueCat = venueCategories[0]['name'].encode('utf-8')
			else:
				venueCat = 'None'
			venueStats = venue['stats']
			venueCheckins = venueStats['checkinsCount']
			print venueName + ', ' + str(venueLat) + ', ' + str(venueLon) + ', ' + venueCat + ', ' + str(venueCheckins)
			output.write(venueName + '\t' + str(venueLat) + '\t' + str(venueLon) + '\t' + venueCat + '\t' + str(venueCheckins) + '\n')
	except HTTPError:
		print 'There is a problem with the request...'
	time.sleep(0.5)

output.close()

print 'Done with everything...'
