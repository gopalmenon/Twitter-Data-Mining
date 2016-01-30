import json
import time
import twitter

CONSUMER_KEY = 'Ub652Z60kKk1eqpHHYdNxqJWc'
CONSUMER_SECRET ='nyBYuxu5vao9X1hAkCgqA4LC21QGI8b162dfRwJzWr5bHB6P0g'
OAUTH_TOKEN = '35655667-LdlEYBm7QGzit182RFM0geXcG7EkTfltUQmpt4qoi'
OAUTH_TOKEN_SECRET = 'q29nXjEHHDAV3Dl49GGrOH6PmffFKCYzcOS1dt5S7oJ9s'

SEARCH_QUERY_PREFIX = 'hillary clinton since:2015-12-16 since_id:'
SEED_TWEET_FILE = 'ClintonTweetsSeq13.txt'
SEED_TWEET_FILE_COUNTER_START = 13
SEED_TWEET_FILE_PREFIX = 'ClintonTweetsSeq'
SEED_TWEET_FILE_SUFFIX = '.txt'
NUMBER_OF_FILES_TO_COLLECT = 625

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)


# Retrieve max id from seed tweet file
candidate_tweets_json = []

for tweet_line in open(SEED_TWEET_FILE):
  try: 
    candidate_tweets_json.append(json.loads(tweet_line))
  except:
    print "Error!!!"
    pass

max_id_str = candidate_tweets_json[0]['search_metadata']['max_id_str']
search_query = SEARCH_QUERY_PREFIX + max_id_str
search_results = twitter_api.search.tweets(q = search_query, lang='en') 

for count in range (SEED_TWEET_FILE_COUNTER_START + 1, NUMBER_OF_FILES_TO_COLLECT + SEED_TWEET_FILE_COUNTER_START):

  #Generate file contents and save to disk
  output_file_name = SEED_TWEET_FILE_PREFIX + str(count) + SEED_TWEET_FILE_SUFFIX
  print "Generating file " + output_file_name
  output_file = open(output_file_name, 'w')
  output_file.write(json.dumps(search_results))
  output_file.close()
  print "Generated file " + output_file_name + ". Waiting for a minute."
  time.sleep(62)

  candidate_tweets_json = []

  for tweet_line in open(output_file_name):
    try: 
      candidate_tweets_json.append(json.loads(tweet_line))
    except:
      print "Error!!!"
      pass

  max_id_str = candidate_tweets_json[0]['search_metadata']['max_id_str']
  search_query = SEARCH_QUERY_PREFIX + max_id_str
  search_results = twitter_api.search.tweets(q = search_query, lang='en') 
  


