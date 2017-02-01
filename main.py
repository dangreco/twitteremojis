import json, sys, os, tweepy, unicodedata, keys
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
from ISStreamer.Streamer import Streamer
from dictionary import getDictionary

# TWITTER API BUILDING
auth = OAuthHandler(keys.getCK(), keys.getCS())
auth.set_access_token(keys.getAT(), keys.getAS())
api = tweepy.API(auth)

# INITIALSTATE API BUILDING
streamer = Streamer(bucket_name = keys.getBN() , bucket_key = keys.getBK() , access_key = keys.getAK() )

# EMOJIS
emCodes = []
emNames = []
e = 'emojis'

emDict = getDictionary()
for key, value in emDict.iteritems():
  emCodes.append(value['code'])
  emNames.append(value['id'])

class MyListener(StreamListener):


    def on_data(self, data):
      d = json.loads(data)
      if 'text' in d:
        txt = d['text']

        for emoj in emCodes:
          if emoj in txt:
            streamer.log(e, emNames[emCodes.index(emoj)])
        # HANDLES LOCATION (IF ANY)
        if 'place' in d :
          if not d['place'] == None and 'bounding_box' in d['place']:
            if not d['place']['bounding_box'] == None and 'coordinates' in d['place']['bounding_box']:
              if not d['place']['bounding_box']['coordinates'] == None:
                arr = d['place']['bounding_box']['coordinates']
                coords = arr[0][0]
                loc = coords[1], coords[0]
                streamer.log('LONGLAT', loc)


    def on_error(self, status):
        print(status)
        return True

# --------------------------------------

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=e)
