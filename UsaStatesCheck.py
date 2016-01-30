# State postal codes in lower case
state_codes = ['al','ak','az','ar','ca','co','ct','de','fl','ga','hi','id','il','in','ia','ks','ky','la','me','md','ma','mi','mn','ms','mo','mt','ne','nv','nh','nj','nm','ny','nc','nd','oh','ok','or','pa','ri','sc','sd','tn','tx','ut','vt','va','wa','wv','wi','wy'];

#State names in lower case
state_names =  ['alabama','alaska','arizona','arkansas','california','colorado','connecticut','delaware','florida','georgia','hawaii','idaho','illinois','indiana','iowa','kansas','kentucky','louisiana','maine','maryland','massachusetts','michigan','minnesota','mississippi','missouri','montana','nebraska','nevada','new hampshire','new jersey','new mexico','new york','north carolina','north dakota','ohio','oklahoma','oregon','pennsylvania','rhode island','south carolina','south dakota','tennessee','texas','utah','vermont','virginia','washington','west virginia','wisconsin','wyoming'];

# Check if Twitter user profile is inside one of the states in USA
def isInOneOfUsaContiguousStates(user_location):
	
	# Return false user location is empty
	if not user_location or user_location.isspace():
		return 'False', ' '

	# Convert user location string to 
	user_location_lower_case = user_location.lower()
	for count in range(0, len(state_names)):
		if state_names[count] in user_location_lower_case:
			return 'True', state_codes[count]

	# Since state name is not found check if state code is found in user location
	for count in range(0, len(state_codes)):

  		padded_state_code = ' ' + state_codes[count] + ' '
		if padded_state_code in user_location_lower_case:
			return 'True', state_codes[count]

		padded_state_code = ',' + state_codes[count] + ' '
		if padded_state_code in user_location_lower_case:
			return 'True', state_codes[count]

		# Check if location ends with state code
  		padded_state_code = ' ' + state_codes[count]
		if user_location_lower_case.endswith(padded_state_code):
			return 'True', state_codes[count]

		padded_state_code = ',' + state_codes[count]
		if user_location_lower_case.endswith(padded_state_code):
			return 'True', state_codes[count]

		# Check if location starts with state code
  		padded_state_code = state_codes[count] + ' '
		if user_location_lower_case.startswith(padded_state_code):
			return 'True', state_codes[count]

		padded_state_code = state_codes[count] + ','
		if user_location_lower_case.startswith(padded_state_code):
			return 'True', state_codes[count]

	return 'False', ' '

