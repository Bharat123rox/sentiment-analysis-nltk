import tweepy
import re
from tweepy import RateLimitError,TweepError
from secretkeys import consumer_key,consumer_secret,access_token,access_token_secret
class TwitterClient(object):
	def __init__(self):
		try:
			self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
			self.auth.set_access_token(access_token, access_token_secret)
			self.api = tweepy.API(self.auth,parser=tweepy.parsers.JSONParser())
			self.tweet_list = []
		except:
			print('Error:Authentication Failed')
#Function to clean tweets for analysis by removing handles,hashtags and URLs
	def clean_tweet(self,strip_url=True,strip_hashtags=True,strip_handles=True):
		ll = len(self.tweet_list)
		for i in range(ll):
			if strip_url:
				self.tweet_list[i] = re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', self.tweet_list[i])
			if strip_hashtags:
				self.tweet_list[i] = re.sub(r'#(\w+)','',self.tweet_list[i])
			if strip_handles:
				self.tweet_list[i] = re.sub(r'@(\w+)','',self.tweet_list[i])
				self.tweet_list[i] = re.sub(r'RT @(\w+):','',self.tweet_list[i])
			self.tweet_list[i] = self.tweet_list[i].replace('\xa0','')
			self.tweet_list[i] = self.tweet_list[i].replace('&nbsp;','')
			self.tweet_list[i] = self.tweet_list[i].replace('\n','')
			self.tweet_list[i] = self.tweet_list[i].replace('\"','"')
			self.tweet_list[i] = self.tweet_list[i].replace("\'","'")
			self.tweet_list[i] = self.tweet_list[i].replace("&amp;","&")
		return self.tweet_list
	def get_tweet(self,query,count=20):
		try:
			res = self.api.search(q=query,rpp=count)
			ll = len(res['statuses'])
			for i in range(ll):
				tweet = res['statuses'][i].get('text')
				if tweet is None:
					pass 
				retweet = res['statuses'][i].get('retweeted_status')
				if retweet is None:
					pass
				else:
					retweet = retweet.get('text')
					if retweet is None:
						pass
				if (retweet is not None) and (retweet not in self.tweet_list):
					self.tweet_list.append(retweet)
				elif (tweet is not None) and (tweet not in self.tweet_list):
					self.tweet_list.append(tweet)
				else:
					pass
			self.clean_tweet()
			self.tweet_list = list(set(self.tweet_list)) #Removing any possible duplicate items/tweets after tweet processing/cleaning					
			return self.tweet_list
		except RateLimitError:
			print('API Rate Limit Exceeded.Please try after 15 minutes.`')
		except TweepError as e:	
			print(e.message[0]['code'])