# This file is intended to explain about the implementation of 'bag of words'
# Bag of words is a methodology of machine learning that is used to count the frequency of the
# words used in a text. So, lets start with this!

# Here we import the module from sklearn that is responsible for read the words and create a bag of words:

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()

# Then, we can create or import our emails/texts/phrases to fill our bag of words

email1 = "Good morning, I would like to schedulle a meeting with you."
email2 = "Ok, we can meet saturday at 11 am, what do you think?"

list_of_emails = [email1, email2]

# Now, we will start to use the  count vectorizer to create a bag of words. 
# A bag of words is simply a frequency count for all the words used in your text.

# this line below will take each word in list of emails and put in the bag
bag_of_words = vectorizer.fit(list_of_emails)

# this one will generate all the counts/ words frequency for each word in the bag
bag_of_words = vectorizer.transform(list_of_emails)

# after this, I will have an output with a list of tuples (indicating the document number, word number) 
# and a list of integers indicating the word count
# just like this: (document number - in my case the variable email, word number - the word order inside the text) word frequency

# Data preprocessing: removing the stepwords (not important ones because they are very common in you vocabulary and does not mean a lot)
import nltk

# you will need to download the nltk (you can do it using command line)

from nltk.corpus import stopwords
sw = stopwords.words("english")