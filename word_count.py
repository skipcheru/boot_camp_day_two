#  Function counts the number times a word occurs in a sentence

def words(sentence):

    split_words = str(sentence).split()
    word_dict = dict()

    # loop through the list and check if it exists

    for word in split_words:
        if word.isdigit() is True:

            word = int(word)  # cast to integer if is a digit

        # add values as keys to the dictionary while checking if they exist

        if word not in word_dict:
            word_dict[word] = 1 # value is one if it doesnt exist
        else:
            word_dict[word] += 1 # increment value by one if they exist

    return word_dict
