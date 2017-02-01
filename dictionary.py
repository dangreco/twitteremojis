# Dictionary to handle the emojis and their codes. Needs different number for each emoji as python dictionary keys can't be the same. (Ends up only using the last one.)

emojiDictionary = {
  "1":{"id":":joy:", "code":u"\U0001F602"},
  "2":{"id":":sob:", "code":u"\U0001F62D"},
  "3":{"id":":rage:", "code":u"\U0001F621"},
  "4":{"id":":grimacing:", "code":u"\U0001F62C"},
  "5":{"id":":grin:", "code":u"\U0001F601"},
  "6":{"id":":grinning:", "code":u"\U0001F600"},
  "7":{"id":":rofl:", "code":u"\U0001F923"},
  "8":{"id":":smiley:", "code":u"\U0001F603"},
  "9":{"id":":smile:", "code":u"\U0001F604"},
  "10":{"id":":sweat_smile:", "code":u"\U0001F605"},
  "11":{"id":":laughing:", "code":u"\U0001F606"},
  "12":{"id":":wink:", "code":u"\U0001F609"},
  "13":{"id":":blush:", "code":u"\U0001F60A"},
  "14":{"id":":yum:", "code":u"\U0001F60B"},
  "15":{"id":":sunglasses:", "code":u"\U0001F60E"},
  "16":{"id":":heart_eyes:", "code":u"\U0001F60D"},
  "17":{"id":":kissing_heart:", "code":u"\U0001F618"},
  "18":{"id":":kissing:", "code":u"\U0001F617"},
  "19":{"id":":kissing_closed_eyes:", "code":u"\U0001F619"},
  "20":{"id":":kissing_smiling_eyes:", "code":u"\U0001F61A"},
  "21":{"id":":relaxed:", "code":u"\U0000263A"},
  "22":{"id":":slight_smile:", "code":u"\U0001F642"},
  "23":{"id":":thinking:", "code":u"\U0001F914"},
  "24":{"id":":neutral_face:", "code":u"\U0001F610"},
  "25":{"id":":expressionless:", "code":u"\U0001F611"},
  "26":{"id":":no_mouth:", "code":u"\U0001F636"},
  "27":{"id":":rolling_eyes:", "code":u"\U0001F644"},
  "28":{"id":":smirk:", "code":u"\U0001F60F"},
  "29":{"id":":tired_face:", "code":u"\U0001F625"},
  "30":{"id":":angry:", "code":u"\U0001F620"}
}

# Primary fucntion used in order to pull the dictionary from this file.

def getDictionary():
  return emojiDictionary
