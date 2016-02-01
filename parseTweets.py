import json
import MonthNumber
import UsaStatesCheck

from datetime import date
from os import listdir
from os.path import isfile, join

TWEETS_TO_COLLECT = 2500

last_election_results = ['red', 'red', 'red', 'red', 'blue', 'blue', 'blue', 'blue', 'blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red', 'red', 'red', 'blue', 'blue', 'blue', 'blue', 'blue', 'red', 'red', 'red', 'red', 'blue', 'blue', 'blue', 'blue', 'blue', 'red', 'red', 'blue', 'red', 'blue', 'blue', 'blue', 'red', 'red', 'red', 'red', 'red', 'blue', 'blue', 'blue', 'red', 'blue', 'red'];

# Retrieve tweets from text file
candidate_tweets_json = []

# List to hold parsed tweets
all_clinton_tweets = []
all_trump_tweets = []

# Template for parsed tweet
class tweet_details:
	pass

tweet_files = [f for f in listdir('.') if isfile(join('.', f)) and f.startswith('ClintonTweetsSeq')]

clintonTweetsCount = 0
for tweet_file in tweet_files:
  candidate_tweets_json = []
  for tweet_line in open(tweet_file):
    try: 
      candidate_tweets_json.append(json.loads(tweet_line))
    except:
      pass

  # Total number of tweets retrieved from text file
  number_of_tweets =  len(candidate_tweets_json[0]['statuses'])

  # Fill list with parsed tweets
  for count in range(0, number_of_tweets):
    current_tweet = tweet_details()
    user_location = candidate_tweets_json[0]['statuses'][count]['user']['location']
    inside_usa, state_code = UsaStatesCheck.isInOneOfUsaContiguousStates(user_location)
    if inside_usa == 'True':
      #print user_location + " in state " + state_code
      current_tweet.user_location = user_location
      current_tweet.state_code = state_code
      current_tweet.created_at = candidate_tweets_json[0]['statuses'][count]['created_at']
      current_tweet.id_str = candidate_tweets_json[0]['statuses'][count]['id_str']
      current_tweet.text = candidate_tweets_json[0]['statuses'][count]['text']
      current_tweet.user_screen_name = candidate_tweets_json[0]['statuses'][count]['user']['screen_name']
      current_tweet.user_id_str = candidate_tweets_json[0]['statuses'][count]['user']['id_str']
      current_tweet.place = candidate_tweets_json[0]['statuses'][count]['place']
      current_tweet.user_friends_count = candidate_tweets_json[0]['statuses'][count]['user']['friends_count']
      current_tweet.user_followers_count = candidate_tweets_json[0]['statuses'][count]['user']['followers_count']
      current_tweet.user_lang = candidate_tweets_json[0]['statuses'][count]['user']['lang']
      clintonTweetsCount += 1
      all_clinton_tweets.append(current_tweet)

      # Terminate if required count reached
      if clintonTweetsCount >= TWEETS_TO_COLLECT:
        break
  else:
    continue
  break

# Print parsed tweets
print 'Total clinton tweets found is ' + str(len(all_clinton_tweets))

# Tweets summarized by state
clinton_tweets_per_state = [0] * 50

# Summarize number of tweets by state
for count in range(0, len(all_clinton_tweets)):
  clinton_tweets_per_state[UsaStatesCheck.state_codes.index(all_clinton_tweets[count].state_code)] += 1

# Print results by state
for count in range(0, len(clinton_tweets_per_state)):
  print UsaStatesCheck.state_names[count] + '\t' + str(clinton_tweets_per_state[count])

# Stats for number of tweets per day starting from 12/16/2015
start_date = date(2015, 12, 16)
clinton_tweets_by_date = [0] * 50
clinton_tweet_hour = [0]*24
for count in range(0, len(all_clinton_tweets)):
  tweet_date_string = all_clinton_tweets[count].created_at
  tweet_date_components = tweet_date_string.split(' ')
  tweet_date = date(int(tweet_date_components[5]), MonthNumber.getMonthNumber(tweet_date_components[1]), int(tweet_date_components[2]))
  days_from_start = tweet_date - start_date
  clinton_tweets_by_date[days_from_start.days - 1] += 1
  tweet_time = tweet_date_components[3]
  clinton_tweet_hour[int(tweet_time[0:2])] += 1
print "Clinton tweets by date ",
print clinton_tweets_by_date
print "Clinton tweets by hour ",
print clinton_tweet_hour

###############################################################################################################################


tweet_files = [f for f in listdir('.') if isfile(join('.', f)) and f.startswith('TrumpTweetsSeq')]

trumpTweetsCount = 0
for tweet_file in tweet_files:
  candidate_tweets_json = []
  for tweet_line in open(tweet_file):
    try: 
      candidate_tweets_json.append(json.loads(tweet_line))
    except:
      pass

  # Total number of tweets retrieved from text file
  number_of_tweets =  len(candidate_tweets_json[0]['statuses'])

  # Fill list with parsed tweets
  for count in range(0, number_of_tweets):
    current_tweet = tweet_details()
    user_location = candidate_tweets_json[0]['statuses'][count]['user']['location']
    inside_usa, state_code = UsaStatesCheck.isInOneOfUsaContiguousStates(user_location)
    if inside_usa == 'True':
      #print user_location + " in state " + state_code
      current_tweet.user_location = user_location
      current_tweet.state_code = state_code
      current_tweet.created_at = candidate_tweets_json[0]['statuses'][count]['created_at']
      current_tweet.id_str = candidate_tweets_json[0]['statuses'][count]['id_str']
      current_tweet.text = candidate_tweets_json[0]['statuses'][count]['text']
      current_tweet.user_screen_name = candidate_tweets_json[0]['statuses'][count]['user']['screen_name']
      current_tweet.user_id_str = candidate_tweets_json[0]['statuses'][count]['user']['id_str']
      current_tweet.place = candidate_tweets_json[0]['statuses'][count]['place']
      current_tweet.user_friends_count = candidate_tweets_json[0]['statuses'][count]['user']['friends_count']
      current_tweet.user_followers_count = candidate_tweets_json[0]['statuses'][count]['user']['followers_count']
      current_tweet.user_lang = candidate_tweets_json[0]['statuses'][count]['user']['lang']
      trumpTweetsCount += 1
      all_trump_tweets.append(current_tweet)

      # Terminate if required count reached
      if trumpTweetsCount >= TWEETS_TO_COLLECT:
        break
  else:
    continue
  break

# Print parsed tweets
print 'Total trump tweets found is ' + str(len(all_trump_tweets))

# Tweets summarized by state
trump_tweets_per_state = [0] * 50

# Summarize number of tweets by state
for count in range(0, len(all_trump_tweets)):
  trump_tweets_per_state[UsaStatesCheck.state_codes.index(all_trump_tweets[count].state_code)] += 1

# Print results by state
for count in range(0, len(trump_tweets_per_state)):
  print UsaStatesCheck.state_names[count] + '\t' + str(trump_tweets_per_state[count])


# Stats for number of tweets per day starting from 12/16/2015
start_date = date(2015, 12, 16)
trump_tweets_by_date = [0] * 50
trump_tweet_hour = [0]*24

for count in range(0, len(all_trump_tweets)):
  tweet_date_string = all_trump_tweets[count].created_at
  tweet_date_components = tweet_date_string.split(' ')
  tweet_date = date(int(tweet_date_components[5]), MonthNumber.getMonthNumber(tweet_date_components[1]), int(tweet_date_components[2]))
  days_from_start = tweet_date - start_date
  trump_tweets_by_date[days_from_start.days - 1] += 1
  tweet_time = tweet_date_components[3]
  trump_tweet_hour[int(tweet_time[0:2])] += 1
print "Trump tweets by date ",
print trump_tweets_by_date
print "Trump tweets by hour ",
print trump_tweet_hour
