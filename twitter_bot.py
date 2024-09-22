import tweepy

# Twitter API credentials
API_KEY = 'Your API Key here'
API_SECRET_KEY = 'Your Secret Key here'
ACCESS_TOKEN = 'Access Token here'
ACCESS_TOKEN_SECRET = 'Access Token Secret here'

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Upload a tweet
def post_tweet(message):
    try:
        api.update_status(message)
        print("Tweet posted successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


tweet_message = "This is a test tweet using Python!"
post_tweet(tweet_message)
