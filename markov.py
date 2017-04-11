"""Generate markov text from text files."""


from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    text = open(file_path).read().split()

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
    i = 0
    #j = i + 1


    #for text_string.index(text_string[j]) in enumerate(text_string):
    for i in range(1, len(text_string) - 1):
        words_after_j = []

        words_after_j.append(text_string[i+2])

        for i in range(len(text_string) - 1):
            bigram = (text_string[i], text_string[i+1])
            chains[bigram] = words_after_j

        i+=1
        #j+=1

    # your code goes here

    print chains


def make_text(chains):
    """Returns text from chains."""

    words = []

    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
#chains = make_chains(input_text)

# Produce random text
#random_text = make_text(chains)

#print random_text

