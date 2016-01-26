import json

trump_tweets_json = []

for tweet_line in open('clintonTweets2.txt'):
  try: 
    trump_tweets_json.append(json.loads(tweet_line))
  except:
    pass

#print json.dumps(trump_tweets_json[0]['statuses'][0], indent = 5)
# This is the first tweet extracted
print trump_tweets_json[0]['statuses'][0]['created_at']
print trump_tweets_json[0]['statuses'][0]['id_str']
print trump_tweets_json[0]['statuses'][0]['text']
print trump_tweets_json[0]['statuses'][0]['user']['screen_name']
print trump_tweets_json[0]['statuses'][0]['user']['id_str']
print trump_tweets_json[0]['statuses'][0]['user']['location']
print trump_tweets_json[0]['statuses'][0]['place']
print trump_tweets_json[0]['statuses'][0]['user']['friends_count']
print trump_tweets_json[0]['statuses'][0]['user']['followers_count']
print trump_tweets_json[0]['statuses'][0]['user']['lang']
 

