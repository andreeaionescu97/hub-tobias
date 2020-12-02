import twitter,json,csv
# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://developer.twitter.com/en/docs/basics/authentication/overview/oauth
# for more information on Twitter's OAuth implementation.
CONSUMER_KEY = 'xsrw61YDMWXc6EFdQrKOa3qub'
CONSUMER_SECRET = 'RqMB1sgSlINUjWYGtx8RItuR3DdFX9axkMykjVl5ErhxhVwCBj'
OAUTH_TOKEN = '1325581308026892288-YO7meaCyX11qW84y2vvceMgYcdyV27'
OAUTH_TOKEN_SECRET = 'RiEeH27s5mcx6oL3IhShkac95X6wLYv8BpmNtRWbn7VXF'
auth = twitter.oauth.OAuth(1325581308026892288-YO7meaCyX11qW84y2vvceMgYcdyV27, RiEeH27s5mcx6oL3IhShkac95X6wLYv8BpmNtRWbn7VXF,
                           xsrw61YDMWXc6EFdQrKOa3qub, RqMB1sgSlINUjWYGtx8RItuR3DdFX9axkMykjVl5ErhxhVwCBj)
twitter_api = twitter.Twitter(auth=auth)
# setup a file to write to
csvfile = open('brexit_tweets.csv', 'w')
csvwriter = csv.writer(csvfile)
# Query terms
q = "brexit" # Comma-separated list of terms
#  Using the String Formatting Operator https://www.tutorialspoint.com/python/python_strings.htm
print 'Filtering the public timeline for track="%s"' % (q,)
# Reference the self.auth parameter
twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)
# See https://dev.twitter.com/docs/streaming-apis
stream = twitter_stream.statuses.filter(track=q)
# For illustrative purposes, when all else fails, search for Justin Bieber
# and something is sure to turn up (at least, on Twitter)
for tweet in stream:
    csvwriter.writerow([tweet['user']['screen_name'].encode('utf-8'),tweet['text'].encode('utf-8')])
    print tweet['user']['screen_name'].encode('utf-8'), tweet['text'].encode('utf-8')
  # Save to a database in a particular collection
