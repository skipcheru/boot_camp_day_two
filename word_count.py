
"""Function counts the occurence of words in a string"""

def words(word):

    split_words = str(word).split()
    word_dict = dict()

    """loop through the list and check each if it exists"""

    for sw in split_words:
        if sw.isdigit() is True:

            sw = int(sw)  # cast to integer if is a digit

        """add values as keys to the dictionary while checking if they exist"""

        if sw not in word_dict:
            word_dict[sw] = 1 # value is one if it doesnt exist
        else:
            word_dict[sw] += 1 #increment value by one if they exist

    return word_dict
