#Read the tweets one by one and process it
import prepr
import filtering
import csv
import nltk.classify.util


#start extract_features
def extract_features(tweet):
   tweet_words = set(tweet)
   features = {}
   for word in featureList:
       features['contains(%s)' % word] = (word in tweet)
   return features
#end


inpTweets = csv.reader(open('ALLTWEETS.csv', 'rb'), delimiter=',', quotechar='|')
stopWords = filtering.getStopWordList('stopwords.txt')
featureList = ['i','me','myself','we','us','our','my,','self','you','your','yours','ours','yourself','yourselves','oh','wow','whoa','!','!!','!!!','!!!!','!!!!!','god','phew','omg','very','really','so','such','few','extremely','extreme','awful','awesome','could','would','should','might','must','may',
'maybe','wouldn\'t','shouldn\'t','couldn\'t','cud','shud','wud','v','?','??','???']

# Get tweet words
tweets = []
for row in inpTweets:
    sentiment = row[0]
    tweet = row[1]
    processedTweet = filtering.processTweet(tweet)
    featureVector = filtering.getFeatureVector(processedTweet)
    featureList.extend(featureVector)
    tweets.append((featureVector, sentiment));
#end loop
print "This is ****************************************************************************************************************************************************************"
print tweets

print "*************************************************************************************"
# Remove featureList duplicates
featureList = list(set(featureList))
print featureList
print "**************************************************************************************"
# Extract feature vector for all tweets in one shot
training_set = nltk.classify.util.apply_features(extract_features,tweets)
print "*************************************************************************************"
#print training_set



# Train the classifier
NBClassifier = nltk.NaiveBayesClassifier.train(training_set)

# Test the classifier
testTweet = raw_input("Enter the tweet to classify:")
processedTestTweet = filtering.processTweet(testTweet)
print "This above tweet belongs to "
x = extract_features(filtering.getFeatureVector(processedTestTweet))
print NBClassifier.classify(x)

print NBClassifier.show_most_informative_features(10)


