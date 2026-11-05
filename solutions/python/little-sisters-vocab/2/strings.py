
def add_prefix_un(word):
    """Add the prefix un to a word."""
    return "un" + word


def make_word_groups(words):
    """Add the prefix to each word and join the results."""
    pre = words[0]
    result = [pre]

    for word in words[1:]:
        result.append(pre + word)

    return " :: ".join(result)


def remove_suffix_ness(word):
    """Remove ness from a word and replace iness with y."""
    if word.endswith("iness"):
        return word[:-5] + "y"
    return word[:-4]


def adjective_to_verb(sentence, index):
    """Convert an adjective into a verb by adding en."""
    words = sentence.split()
    word = words[index]

    if word.endswith("."):
        word = word[:-1]

    return word + "en"
