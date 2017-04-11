def make_chains(text_string):
    chains = {}
    i = 0


    #for text_string.index(text_string[j]) in enumerate(text_string):
    while i < len(text_string) - 2:
        for i in range(len(text_string) - 1):
            bigram = (text_string[i], text_string[i + 1])

            words_after = []
            words_after.append(text_string[i+2])

        i += 1

        if bigram not in chains:
            words_after = []

        for i in range(len(text_string) - 2):
            
            j = i + 1

            words_after_j.append(text_string[j + 1])


            
        chains[bigram] = words_after_j



    print chains


if bigram[1] in enumerate(text_string):
    words_after.append(text_string[text_string.index(bigram[1]) + 1)


chains[bigram] = text_string[i+2]

for i in range(len(text) - 1):
    bigram = (text[i], text[i + 1])

    words_after = []
    words_after.append(text[i+2])





chains = {}
for i in range(len(text) - 2):
    bigram = (text[i], text[i + 1])

    if bigram in chains.keys():
        words_after = chains[bigram]
        words_after.append(text[i + 2])
    else:
        words_after = []
        words_after.append(text[i + 2])

    chains[bigram] = words_after