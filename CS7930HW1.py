import twitter
import json

CONSUMER_KEY = 'Ub652Z60kKk1eqpHHYdNxqJWc'
CONSUMER_SECRET ='nyBYuxu5vao9X1hAkCgqA4LC21QGI8b162dfRwJzWr5bHB6P0g'
OAUTH_TOKEN = '35655667-LdlEYBm7QGzit182RFM0geXcG7EkTfltUQmpt4qoi'
OAUTH_TOKEN_SECRET = 'q29nXjEHHDAV3Dl49GGrOH6PmffFKCYzcOS1dt5S7oJ9s'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)

search_results = twitter_api.search.tweets(q = 'hillary clinton since:2015-12-16', lang='en') #geocode='37.87222, -91.21527778, 2157km'

print json.dumps(search_results) 
