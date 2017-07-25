import string
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from TweetFetcher import TwitterClient
tc = TwitterClient()
#The API fetches only 15 tweets at a time, hence this workaround 
def senti_score(query,count=20):
    if count >= 15:
        while count >= 0:
            ob = tc.get_tweet(query,count)
            count = count - 15
    sentiments = []
    sid = SentimentIntensityAnalyzer()
    for sentence in ob:
        scores = {}
        ss = sid.polarity_scores(sentence)
        scores['Sentence'] = sentence
        scores['Positive'] = ss['pos']
        scores['Negative'] = ss['neg']
        scores['Neutral'] = ss['neu']
        scores['Overall'] = ss['compound']
        sentiments.append(scores)
    ll = len(sentiments)
    pos_tweets = sorted(sentiments,key=lambda x:x['Overall'],reverse=True)
    neg_tweets = sorted(sentiments,key=lambda x:x['Overall'])
    tweet_qty = min(10,ll//2)
    print("The top "+str(tweet_qty)+" strongly positive tweets are: "+'\n')
    for x in range(tweet_qty):
        if pos_tweets[x]['Overall'] != 0:
            print("{0}\nPositive score is {1},Negative score is {2},Neutral score is {3},Overall Tweet Sentiment is {4}".format(pos_tweets[x]['Sentence'],pos_tweets[x]['Positive'],pos_tweets[x]['Negative'],pos_tweets[x]['Neutral'],pos_tweets[x]['Overall']),sep='\n')
        else:
            print("{}\nNeutral tweet with not much emotion".format(pos_tweets[x]['Sentence']),sep='\n') 
    print("The top "+str(tweet_qty)+" strongly negative tweets are: "+'\n')
    for x in range(tweet_qty):
        if neg_tweets[x]['Overall'] != 0:
            print("{0}\nPositive score is {1},Negative score is {2},Neutral score is {3},Overall Tweet Sentiment is {4}".format(neg_tweets[x]['Sentence'],neg_tweets[x]['Positive'],neg_tweets[x]['Negative'],neg_tweets[x]['Neutral'],neg_tweets[x]['Overall']),sep='\n')
        else:
            print("{}\nNeutral tweet with not much emotion".format(pos_tweets[x]['Sentence']),sep='\n')
try:        
    s1 = input('Enter Search Query for tweets:')
    s2 = input('Enter no.of tweets to be analyzed(default is 20),Press Enter Key without any number to accept default:')
    if not s1:
        print('No results for empty input')
    elif not s2:
        sentiscore = senti_score(s1)
    else:
        s2 = int(s2)
        sentiscore = senti_score(s1,s2)
except ValueError:
    print('Invalid input.')