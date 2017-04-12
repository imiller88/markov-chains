"""Generate markov text from text files."""


from random import choice
import sys

file_path1 = sys.argv[1]
# file_path2 = sys.argv[2]

def open_and_read_file(file_path1):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here


    text1 = open(file_path1).read().split()
    # text2 = open(file_path2).read().split()

    text = text1

    return text



def make_chains(text_string):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
    """


    chains = {}
    for i in range(len(text_string) - 2):
        bigram = (text_string[i], text_string[i + 1])

        if bigram in chains.keys():
            words_after = chains[bigram]
            words_after.append(text_string[i + 2])
        else:
            words_after = []
            words_after.append(text_string[i + 2])

        chains[bigram] = words_after

    # your code goes here

    return chains


def make_text(chains):
    """Returns text from chains."""

    words = []
    # bigram = choice(chains.keys())
    upper_bigrams = []
    for bigram in chains:
        if bigram[0][0] == bigram[0][0].upper():
            upper_bigrams.append(bigram)


    bigram = choice(upper_bigrams)
    words.append(bigram[0])
    words.append(bigram[1])


    # your code goes here
    i = 1


    # for key in chains:
    while True:
        #if bigram doesn't exist, we need to break. else see below

        if bigram in chains.keys():
            words.append(choice(chains[bigram]))
            bigram = (words[i], words[i+1])
            i+=1
        else:
            # words.append(choice(chains[bigram]))
            break

    return " ".join(words)


# input_path1 = "could-i.txt"
# input_path2 = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(file_path1)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
