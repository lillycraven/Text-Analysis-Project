import urllib.request
import nltk
import string
import gensim
from gensim import corpora

##from wordcloud import WordCloud
#This was from a failed attempt to use word cloud, i couldnt get the above code to run event after installing word cloud and chat GPT didnt have many ideas for me
import matplotlib.pyplot as plt


# nltk.download('stopwords')
# nltk.download('vader_lexicon')
# nltk.download('punkt')

from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.sentiment.vader import SentimentIntensityAnalyzer



url = 'https://www.gutenberg.org/cache/epub/37106/pg37106.txt'
with urllib.request.urlopen(url) as f:
    text = f.read().decode('utf-8')
    # print(text) # for testing





def clean_text(text):
    ''' this function works to clean the text so it can be further analyzed - ChatGPT instructed how I could also 
    remove the punctuation because I got stuck after removing the stop words'''
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Convert to lowercase
    text = text.lower()

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    words = [word for word in words if word not in stop_words]

    return words


def get_most_common_words(url, num_words=30):
    ''' This function finds the thirty most common words from each text'''
    # Fetch the text from the specified URL
    with urllib.request.urlopen(url) as f:
        text = f.read().decode('utf-8')

    # Clean the text
    words = clean_text(text)

    # Create a frequency distribution of the remaining words
    freq_dist = FreqDist(words)

    # Retrieve the most common words
    most_common_words = freq_dist.most_common(num_words)

    # Print the sentiment scores
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)
    print(score)

    # Return the most common words
    return most_common_words


def get_topics(url, num_topics=5, num_words=10):
    ''' Chat GPT helped me with this function, they gave me about 5 different recommendations of ways I could analyze the text
    and I found this one to be the most interesting when combined with the most frequent words. It works to find the most common topics from the texts
     and words that fall under that said topic '''
    # Fetch the text from the specified URL
    with urllib.request.urlopen(url) as f:
        text = f.read().decode('utf-8')

    # Clean the text
    words = clean_text(text)

    # Create a dictionary from the words in the text
    dictionary = corpora.Dictionary([words])

    # Create a corpus from the text
    corpus = [dictionary.doc2bow([word]) for word in words]

    # Apply Latent Dirichlet Allocation to the corpus
    lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics, random_state=42)

    # Retrieve the most significant topics and their corresponding words
    topics = lda.print_topics(num_words=num_words)

    # Print the topics with nicer formatting
    print("Top {} topics from the text:\n".format(num_topics))
    for i, topic in enumerate(topics):
        topic_num = i + 1
        words = topic[1].split("+")
        words = [word.split("*")[1].replace('"', '').strip() for word in words]
        print("Topic {}: {}\n".format(topic_num, ", ".join(words)))





# def generate_word_cloud(url):
#     '''This function was found by chat GPT to help visualize the code using word cloud but I was having trouble getting it to work'''
#     # Fetch the text from the specified URL
#     with urllib.request.urlopen(url) as f:
#         text = f.read().decode('utf-8')

#     # Clean the text
#     words = clean_text(text)

#     # Generate a word cloud image
#     wordcloud = WordCloud(width=800, height=800, background_color='white', stopwords=STOPWORDS).generate(' '.join(words))

#     # Display the word cloud
#     plt.figure(figsize=(8, 8), facecolor=None)
#     plt.imshow(wordcloud)
#     plt.axis("off")
#     plt.tight_layout(pad=0)

#     plt.show()


def plot_scatter(url):
    # Fetch the text from the specified URL
    with urllib.request.urlopen(url) as f:
        text = f.read().decode('utf-8')

    # Tokenize the text
    words = word_tokenize(text.lower())

    # Define the target words to look for
    target_words = ["beth", "jo", "amy", "meg"]

    # Create a dictionary to hold the frequencies of each target word
    word_freqs = {word: 0 for word in target_words}

    # Count the frequencies of the target words
    for word in words:
        if word in target_words:
            word_freqs[word] += 1

    # Create a scatter plot of the word frequencies
    x_vals = list(range(len(target_words)))
    y_vals = [word_freqs[word] for word in target_words]

    fig, ax = plt.subplots()
    ax.scatter(x_vals, y_vals)

    # Label the x-axis with the target words
    ax.set_xticks(x_vals)
    ax.set_xticklabels(target_words)

    # Set the y-axis label and title
    ax.set_ylabel("Frequency")
    ax.set_title("Occurences of each of the four sisters")

    plt.show()

url = 'https://www.gutenberg.org/cache/epub/37106/pg37106.txt'
most_common_words = get_most_common_words(url, num_words=30)
print(most_common_words)


url2 = 'https://www.gutenberg.org/files/1260/1260-0.txt'
with urllib.request.urlopen(url2) as f:
    text = f.read().decode('utf-8')
    # print(text) # for testing

url2 = 'https://www.gutenberg.org/files/1260/1260-0.txt'
most_common_words2 = get_most_common_words(url2, num_words=30)
print(most_common_words2)


url = 'https://www.gutenberg.org/cache/epub/37106/pg37106.txt'
plot_scatter(url)

topics = get_topics(url, num_topics=5, num_words=10)
for topic in topics:
    print(topic)



