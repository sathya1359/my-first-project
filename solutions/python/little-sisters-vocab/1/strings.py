"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return "un" + word
    
def make_word_groups(words):
    pre = words[0]
    result = [pre]

    for word in words[1:]:
        result.append(pre + word)

    return " :: ".join(result)


def remove_suffix_ness(word):
    if word.endswith("iness"):
        return word[:-5] + "y"
    else:
        return word[:-4]


def adjective_to_verb(sentence, index):
    words = sentence.split()
    word = words[index]

    if word.endswith("."):
        word = word[:-1]

    return word + "en"

