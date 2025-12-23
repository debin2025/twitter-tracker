import pymongo
import stanza

config = {
          'processors': 'tokenize,lemma,pos,depparse,ner',
          'lang': 'en',
          'use_gpu': False,
          'tokenize_pretokenized': True, # disable tokenization
          'tokenize_model_path': './twitter-stanza/saved_models/tokenize/en_tweet_tokenizer.pt',
          'lemma_model_path': './twitter-stanza/saved_models/lemma/en_tweet_lemmatizer.pt',
          "pos_model_path": './twitter-stanza/saved_models/pos/en_tweet_tagger.pt',
          "depparse_model_path": './twitter-stanza/saved_models/depparse/en_tweet_parser.pt',
          "ner_model_path": './twitter-stanza/saved_models/ner/en_tweet_nertagger.pt',
}

# Initialize the pipeline using a configuration dict
#stanza.download("en")
nlp = stanza.Pipeline(**config)

client = pymongo.MongoClient("mongodb+srv://debin:Kh4AXk%3Dt6_EnK%24%3E%7B@tweetdb1.kbwtapy.mongodb.net/test")
dbname = client["Tweets"]
collection = dbname["LeftWingTweets"]


def ner_gen(tweet):
    Entities = []
    doc = nlp(tweet)
    docdict = doc.to_dict()
    for ent in doc.ents:
        if ent != ' ' and ent != '"' and ent != ',':
            Entities.append(ent.text)

    for word in docdict[0]:
        if word["text"][0] == "@":
            Entities.append(word["text"])

    return Entities
def news_ner_gen(tweet):
    Entities = []
    doc = nlp(tweet)
    for ent in doc.ents:
        if ent != ' ' and ent != '"' and ent != ',':
            Entities.append(ent.text)
    return Entities
