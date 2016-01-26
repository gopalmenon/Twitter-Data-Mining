import twitter
import json

CONSUMER_KEY = 'Ub652Z60kKk1eqpHHYdNxqJWc'
CONSUMER_SECRET ='nyBYuxu5vao9X1hAkCgqA4LC21QGI8b162dfRwJzWr5bHB6P0g'
OAUTH_TOKEN = '35655667-LdlEYBm7QGzit182RFM0geXcG7EkTfltUQmpt4qoi'
OAUTH_TOKEN_SECRET = 'q29nXjEHHDAV3Dl49GGrOH6PmffFKCYzcOS1dt5S7oJ9s'
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)
print twitter_api

WORLD_WOE_ID = 1
US_WOE_ID = 23424977

# Prefix ID with the underscore for query string parameterization.
# Without the underscore, the twitter package appends the ID value
# to the URL itself as a special case keyword argument.

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)

world_trends_set = set([trend['name'] for trend in world_trends[0]['trends']])
us_trends_set = set([trend['name'] for trend in us_trends[0]['trends']])
common_trends = world_trends_set.intersection(us_trends_set)

print world_trends
#print us_trends
#print common_trends
