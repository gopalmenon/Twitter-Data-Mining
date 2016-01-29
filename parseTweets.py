import json
import UsaStatesCheck

# Retrieve tweets from text file
trump_tweets_json = []

for tweet_line in open('clintonTweets2.txt'):
  try: 
    trump_tweets_json.append(json.loads(tweet_line))
  except:
    pass

# List to hold parsed tweets
all_tweets = []

# Template for parsed tweet
class tweet_details:
	pass

# Total number of tweets retrieved from text file
number_of_tweets =  len(trump_tweets_json[0]['statuses'])

# Fill list with parsed tweets
for count in range(0, number_of_tweets):
	current_tweet = tweet_details()
	user_location = trump_tweets_json[0]['statuses'][count]['user']['location']
	inside_usa, state_code = UsaStatesCheck.isInOneOfUsaContiguousStates(user_location)
	if inside_usa == 'True':
		print user_location + " in state " + state_code
		current_tweet.user_location = user_location		
		current_tweet.created_at = trump_tweets_json[0]['statuses'][count]['created_at']
		current_tweet.id_str = trump_tweets_json[0]['statuses'][count]['id_str']
		current_tweet.text = trump_tweets_json[0]['statuses'][count]['text']
		current_tweet.user_screen_name = trump_tweets_json[0]['statuses'][count]['user']['screen_name']
		current_tweet.user_id_str = trump_tweets_json[0]['statuses'][count]['user']['id_str']
		current_tweet.place = trump_tweets_json[0]['statuses'][count]['place']
		current_tweet.user_friends_count = trump_tweets_json[0]['statuses'][count]['user']['friends_count']
		current_tweet.user_followers_count = trump_tweets_json[0]['statuses'][count]['user']['followers_count']
		current_tweet.user_lang = trump_tweets_json[0]['statuses'][count]['user']['lang']
		all_tweets.append(current_tweet)
	else:
		print user_location + " not in usa"

# Print parsed tweets
print len(all_tweets)

