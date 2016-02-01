import UsaStatesCheck

NUMBER_OF_STATES = 50
DEMOCRAT_STATE = 'blue'
REPUBLICAN_STATE = 'red'
UNDECIDED_STATE = 'white'

clinton_tweets_by_state = [31,6,53,22,313,36,17,14,171,66,17,16,80,81,43,27,23,20,13,22,44,68,31,21,47,6,21,45,11,52,20,233,51,0,66,27,55,77,5,22,1,27,216,11,4,47,190,5,26,0];

trump_tweets_by_state = [];

electoral_votes_by_state = [9,3,11,6,55,9,7,3,29,16,4,4,20,11,6,6,8,8,4,10,11,16,10,6,10,3,5,6,4,14,5,29,15,3,18,7,7,20,4,9,3,11,38,6,3,13,12,5,10,3];

# Red = state goes to Trump, blue = state goes to clinton
state_colors = [''] * NUMBER_OF_STATES;

clinton_state_votes = [0] * 50
trump_state_votes = [0] * 50

# Loop through tweets by state and find winner. Assign color to the state and the corresponding electoral votes
for count in range(0, NUMBER_OF_STATES):

  if clinton_tweets_by_state[count] > trump_tweets_by_state[count]:
    clinton_state_votes[count] = electoral_votes_by_state[count]
    state_colors[count] = DEMOCRAT_STATE
  elif trump_tweets_by_state[count] > clinton_tweets_by_state[count]:
    trump_state_votes[count] = electoral_votes_by_state[count]
    state_colors[count] = REPUBLICAN_STATE
  else:
    clinton_state_votes[count] = electoral_votes_by_state[count] / 2
    trump_state_votes[count] = electoral_votes_by_state[count] / 2
    state_colors[count] = REPUBLICAN_STATE

clinton_electoral_votes = sum(clinton_state_votes)
trump_electoral_votes = sum(trump_state_votes)

if clinton_electoral_votes > trump_electoral_votes:
  print "Clinton projected to win by " + clinton_electoral_votes + " to " + trump_electoral_votes
elif trump_electoral_votes > clinton_electoral_votes:
  print "Trumpo projected to win by " + trump_electoral_votes + " to " + clinton_electoral_votes
else:
  print "Both candidates projected to tie with " + trump_electoral_votes + " votes each"

# Print the colors for the states
print '['
for count in range(0, NUMBER_OF_STATES):
  print "'" + state_colors[count] + "', "
print ']'

