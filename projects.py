# The first step is to choose different songs (already in songs directory)
# After that I will preprocessing my data. That means that we will use stemming, remove punctuation and remove the stopwords

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



# this function iterates over my songs and preprocessing them
def iterate_over_songs(from_mj):
  all_word_songs = []
  singers = []
  for singer, song_path in [("mj", from_mj), ("cd", from_cd)]:
    for path in song:
      path = os.path.join('..', path[:-1])
      song = open(song_path, "r")
      song_ready = preprocessing_text(song)
      all_word_songs.append(song_ready)
      if singer=="mj":
        singers.append("0")
      if singer=="cd":
        singers.append("1")

      song.close()


# Now I will make the TfIdf representation. What this means?
# Tf stands for term frequency, and it is the same that we did above with count vectorizer:
# It will simply count the frequency of my term.
# Idf  stands for inverse document frequency and basically, it will give me the 'rare' words.
# This will help me to identify words (specific/technical vocabulary) that are used just for some person and not for others.
def tf_idf_representation(songs_from_artists):
  from sklearn.feature_extraction.text import TfidfVectorizer
  #the max_df means that if a word occurs more than 50% in my text, I will remove it because it has no strong meaning for me
  vectorizer = TfidfVectorizer(max_df=0.5, stop_words="english") # in this line I already remove all stop words without using nltk
  vectorizer.fit_transform(songs_from_artists)
  feature_selection()
  # now, my vector is already filled with all the words for all the songs! and everything is ready to start with my analysis


# This step also is part of my preprocessing step and it will select the variables or words that are more
# significant for my purpose
def feature_selection()
  from sklearn.feature_selection import SelectPercentile, f_classif
  # the select percentile will select just the 10% of the features - the 10% most important ones
  selector = SelectPercentile(f_classif, percentile=10)



def main():
  # here I will read different songs and return the words
  # songs from michael jackson
  from_mj = open("fromMJ", "r")
  # songs from celine dion
  from_cd = open("fromCD", "r")
  all_songs = iterate_over_songs(from_mj, from_cd)
  result_matrix = tf_idf_representation(all_songs)

if __name__ == '__main__':
  main()