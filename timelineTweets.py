import urlparse
import oauth2 as oauth
import simplejson
import cgitb
import cgi

consumer_key = 'fgPzVQVDu8pUn8tsz8ixog'
consumer_secret = 'MMEEaWtsEIY2CzYs8CXcgX981zext7y4kDv1Hvjfw'

consumer = oauth.Consumer(consumer_key, consumer_secret)

request_token_url = 'http://twitter.com/oauth/request_token'
access_token_url = 'http://twitter.com/oauth/access_token'
authorize_url = 'http://twitter.com/oauth/authorize'

def getTweets(query):
	token = oauth.Token("1008218550-g8WKidpCiwoxbyf2OsG6auJmI6oUdo2sI5grEUc".encode('utf-8'), "pYZdeU79HLOElzI3lcYloGSMsOvsK6MiuMtYjFaknU".encode('utf-8'))
	client = oauth.Client(consumer, token)
	timeline_url = "http://api.twitter.com/1/statuses/home_timeline.json"
	response, data = client.request(timeline_url.encode('utf-8'))
	resultDict = simplejson.loads(search.read())

	results = []
	if resultDict and "results" in resultDict.keys():	
		for result in resultDict["results"]:
			results.append(result)


	return results
	


def getWebPgTweets():
	tweets = getTweets(keyword)
	extractList = []

	for t in tweets:
		tempdic = dict()
		tempdic["text"] = t["text"]
		tempdic["from_user"] = t["from_user"]
		tempdic["from_user_name"] = t["from_user_name"]
		tempdic["profile_image_url"] = t["profile_image_url"]
		extractList.append(tempdic)

	keywordTweets[keyword] = extractList
	return json.dumps(keywordTweets)




#access_token = {}
#access_token['oauth_token'] = "1008218550-vwZ5SJHnHJEZ4Dlssx5YwAysJ3n5Vx9i4yc2QBo"
#access_token['oauth_token_secret'] = "7UjKn2hPtC1mFkWg0hWO5atoSfwPE3DhSahWGmjEWE"

# Step 1: Get a request token. This is a temporary token that is used for 
# having the user authorize an access token and to sign the request to obtain 
# said access token.

'''
form = cgi.FieldStorage()

request_token = {}

request_token['oauth_token'] = form.getvalue("oauth_token")
oauth_verifier = form.getvalue("oauth_verifier")
request_token['oauth_token_secret'] = ""



# Step 3: Once the consumer has redirected the user back to the oauth_callback
# URL you can request the access token the user has approved. You use the 
# request token to sign this request. After this is done you throw away the
# request token and use the access token returned. You should store this 
# access token somewhere safe, like a database, for future use.
token = oauth.Token(request_token['oauth_token'],
    request_token['oauth_token_secret'])

token.set_verifier(oauth_verifier)
client = oauth.Client(consumer, token)

resp, content = client.request(access_token_url, "POST")
access_token = dict(urlparse.parse_qsl(content))
'''



#response, data = client.request(timeline_url.encode('utf-8'))
#print data
#print response
#tweets = simplejson.loads(data)
#for tweet in tweets:
#    print tweet['text']



cgitb.enable()
print "Content-type: text/html\n\n"

token = oauth.Token("1008218550-g8WKidpCiwoxbyf2OsG6auJmI6oUdo2sI5grEUc".encode('utf-8'), "pYZdeU79HLOElzI3lcYloGSMsOvsK6MiuMtYjFaknU".encode('utf-8'))
client = oauth.Client(consumer, token)
timeline_url = "http://api.twitter.com/1/statuses/home_timeline.json"
response, data = client.request(timeline_url.encode('utf-8'))
tweets = simplejson.loads(data)
#tempdic = dict()
#tempdic["text"] = resultDict["text"]
#tempdic["from_user"] = resultDict["from_user"]
#tempdic["from_user_name"] = resultDict["from_user_name"]
#tempdic["profile_image_url"] = resultDict["profile_image_url"]

print simplejson.dumps(tweets)
for tweet in tweets:
	print "<p>"
	print tweet['text']
	print "</p>"

#print "Content-type: text/html\n\n"
#print getWebPgTweets