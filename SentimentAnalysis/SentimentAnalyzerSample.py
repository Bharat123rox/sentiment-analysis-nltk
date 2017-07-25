import random
import nltk
from nltk.corpus import movie_reviews
print(movie_reviews)
docs = [(list(movie_reviews.words(fileid)),category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]
random.shuffle(docs)
#print(docs)
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words)[:5000]
def doc_features(document):
	document_words = set(document)
	features = {}
	for word in word_features:
		features['word considered is ({})'.format(word)] = (word in document_words)
	return features
featuresets = [(doc_features(d),c) for (d,c) in docs]
train_set, test_set = featuresets[1000:],featuresets[:1000]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier,test_set))