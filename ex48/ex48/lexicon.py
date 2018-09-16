directions = set(['north', 'south', 'east', 'west', 'down', 'up', 'left',
                  'right', 'back'])
verbs = set(['go', 'stop', 'kill', 'eat'])
stopwords = set(['the', 'in', 'of', 'from', 'at', 'it'])
nounwords = set(['door', 'bear', 'princess', 'cabinet'])


def scan(listofwords):
    """Takes a string, which can be multiple words separated by spaces,
    and returns a list of tuples that contains type of word and the word"""
    words = []
    for item in listofwords.split():
        if convert_number(item):
            words.append(('number', int(item)))
        else:
            words.append((check_type_of_word(item), item))
    return words


def check_type_of_word(word):
    """Takes a string and returns what type of word it is"""
    if word in directions:
        return 'direction'
    elif word in verbs:
        return 'verb'
    elif word in stopwords:
        return 'stop'
    elif word in nounwords:
        return 'noun'
    else:
        return 'error'


def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
