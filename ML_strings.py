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

# there are some limitations with bag of words. One of them is that many words can be different if analysed letter by letter
# but they may transmit the same idea: love, loves, loved.
# To put together all this words, there is a process called stemming that will find the word stem and put all the words
# together. How can we do this? like shown below:

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")

# Example for the word responsiveness - the stem is respons
stemmer.stem("responsiveness")


# the preprocessing stemming is made before to compute the bag of words - because is the only way to condense the words.
# using this idea, we can now create a preprocessing and training a robot to tell us who wrote each email that we receive.
# So, in this project I will  develop a robot to identify the author of different songs.

# The first step is to choose different songs
# After that I will preprocessing my data. That means that I will need stem the songs I want to evaluate

# PREPROCESSING METHOD

import string
def preprocessing_text(file):
  file.seek(0) # go back to the position 0 of my file
  all_file_content = file.read()
  file_words = ""

  if len(all_file_content)>1:
    #the line below will remove the punctuation
    just_string = all_file_content[1].translate(string.maketrans("", ""), string.punctuation)

    #now, the process of stemming:
    stemmer = SnowballStemmer("english")
      for word in text_string.split():
        words += stemmer.stem(word) + " "

  return words


def main():
  # here I will read different songs and return the words
  pass

if __name__ == '__main__':
  main()