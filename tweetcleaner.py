"""Clean Trump tweets"""

def clean_tweets(filename):
    text = open(filename).read().split()

    for word in text:
        if word[0] == "@":
            text.remove(word)
        elif "http" in word:
            text.remove(word)
    

    return text

    #return text


# text = clean_tweets("trump-tweets.txt")