featureList = ['i','me','myself','we','us','our','my,','self','you','your','yours','ours','yourself','yourselves','oh','wow','whoa','!','!!','!!!','!!!!','!!!!!','god','phew','omg','very','really','so','such','few','extremely','extreme','awful','awesome','could','would','should','might','must','may',
'maybe','wouldn\'t','shouldn\'t','couldn\'t','cud','shud','wud','v','?','??','???']

tweets= ["i me myself we us our my self",
	"hi there our life"]

print tweets

def extract_features(tweets):
	with open('output.csv','w') as outfile:
		outfile.write('tweetNo.,' + str(featureList)[1:-1]+'\n')
		for i, tweet in enumerate(tweets):
			#tweet = list(set(tweet))
			print 'tweet %d: ' % (i+1), tweet
			features = {}
			for word in featureList:
				features['contains(%s)' % word] = (word in tweet)
			outfile.write(str(i+1) + "," + str(map(int,features.values()))[1:-1]+'\n')
			print features
extract_features(tweets)

