# export TWITTER="twitter.txt"

from nltk.twitter import Twitter, Query, Streamer, credsfromfile
import pickle
from pprint import pprint

__author__ = 'kongaloosh'

import json
from pprint import pprint

with open('data/investments.json') as data_file:
# with open('data.json') as data_file:
    oauth = credsfromfile()
    data = json.load(data_file)
    tw = Twitter()
    client = Query(**oauth)

    for i in range(len(data['investments'])):
            if type(dict(data['investments'][i])):
                tweets = client.search_tweets(keywords=data['investments'][i]['name'], limit=100)
                tweets = list(tweets)
                data['investments'][i]['tweets'] = tweets

    with open('data_pickle.pkl', 'w') as outfile:
        pickle.dump(data, outfile)

f = pickle.load(open('data_pickle.pkl', 'r'))
print(f)