from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from urllib2 import urlopen
from collections import Counter
from string import punctuation
from string import digits
from time import time
import sys
def proper_nouns(reduced_sentence):	
	tagged_sent = pos_tag ( reduced_sentence ) #NLT Library to identify nouns, verbs etc.
	propernouns = [word for word,pos in tagged_sent if pos == "NNP"] #NNP Stands for proper noun
	print "The Proper Nouns & important identified are: "
	propernouns = set ( propernouns ) #Remove duplicates
	for word in sorted(propernouns):
		print word
	print "Number of proper nouns:",
	print len(propernouns)


def freq_dist(data):
    """
    :param data: A string with sentences separated by '\n'
    :type data: str
	returns a dictionary with frequency of each word.
    """
    d = {}
    punc = punctuation.encode('utf-8')
    words = (word for line in data for word in line.translate(None, punc).decode('utf-8').split())
    for word in words:
        d[word] = d.get(word, 0) + 1
    return d




url = 'http://www.textfiles.com/conspiracy/italy.txt'
f=urlopen(url).read() # Read File and Input from url
example_sent = f.replace("*","") 
example_sent = example_sent.replace('[','')
stop_words = set(stopwords.words('english')) #Inbuilt list of stopwords

# Add some seperaters
stop_words.add('')
stop_words.add('=')
stop_words.add('[')
stop_words.add(']')
stop_words.add('*')
stop_words.add(',')
stop_words.add('(')
stop_words.add('\'\'')
stop_words.add('``')
stop_words.add(')')
example_sent = example_sent.translate(None,digits)
#Inbuilt Function to tokenize the data
word_tokens = word_tokenize(example_sent)

#Filter All Except Period (.) 
filtered_sentence = [w for w in word_tokens if not w in stop_words]
#Print Propernouns and important words
proper_nouns(filtered_sentence)
#Now Remove Period too
stop_words = set('.')
filtered_sentence = [w for w in filtered_sentence if not w in stop_words]


#Frequency Analysis after removal of stopwords
word_dist = freq_dist(filtered_sentence)
for Word,Freq in sorted(word_dist.items()):
	print Word,Freq
