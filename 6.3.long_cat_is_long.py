import re

WORD_PATTERN = "[a-zA-Z]+"


def count_words(text):

    """
    Returns the words length in a given text
    :param text: The text to check the word lengths in it.
    :return: A dictionary where the keys are the words in the text (converted to lowercase) and the values
        are the length of the words.
    """

    # first - clean the text from non-letters chars.
    clean_txt = [re.match(WORD_PATTERN, word).group(0)
                 for line in text.split("\n") for word in line.split(" ")
                 if re.match(WORD_PATTERN, word)]

    return {word.lower(): len(word) for word in clean_txt}
