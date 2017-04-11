print ('Importing libraries...')
from urllib.request import urlopen, HTTPError
import json
import csv
import time

# Setting up the global variables
clientID = 'your client id here'
clientSecret = 'your client secret here'
lat = 40.7
lon = -74
version = 20161016
baseURL = 'https://api.foursquare.com/v2/venues/search?'
limit = 50

# Open the base CSV file
with open('Base_Points.csv', 'r') as basePoints:
	reader = csv.reader(basePoints, delimiter=',')
	baseList = list(reader)

# Create the output file
output = open('FoursquareVenues.csv', 'w')
output.write('Name\tLatitude\tLongitude\tCategory\tCheckins\n')

# Building the request
for point in baseList[1:]:
	longitude = point[0]
	latitude = point[1]
	request = baseURL + 'v=' + str(version) + '&ll=' + str(latitude) + ',' + str(longitude) + '&limit=' + str(limit) + '&client_id=' + clientID + '&client_secret=' + clientSecret

	# Querying the API
	try:
		response = urlopen(request)
		readResponse = response.read()
		decodedResponse = readResponse.decode('utf-8')
		baseData = json.loads(decodedResponse)

		# Parsing the API
		content = baseData['response']
		venues = content['venues']
		for venue in venues:
			venueName = venue['name']
			venueLat = venue['location']['lat']
			venueLon = venue['location']['lng']
			venueCategories = venue['categories']
			if len(venueCategories) > 0:
				venueCat = venueCategories[0]['name']
			else:
				venueCat = 'None'
			venueStats = venue['stats']
			venueCheckins = venueStats['checkinsCount']
			print (venueName + ', ' + str(venueLat) + ', ' + str(venueLon) + ', ' + venueCat + ', ' + str(venueCheckins))
			output.write(venueName + '\t' + str(venueLat) + '\t' + str(venueLon) + '\t' + venueCat + '\t' + str(venueCheckins) + '\n')
	except HTTPError:
		print('There is a problem with the request...')
	time.sleep(1)

print ('All done...')
